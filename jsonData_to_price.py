"""
Dify 代码节点：根据 pcb_data 计算 PCB 报价（分项 + 总价）。

入参：pcb_data（dict，或包在 arg1 / kwargs 中）
出参：total_price、price_breakdown、param_remarks（各字段中文说明）、area_m2、error

完整字段说明见常量 INPUT_PARAM_REMARKS、OUTPUT_PARAM_REMARKS。
"""

from __future__ import annotations

import json
from typing import Any

# ---------- 入参字段说明（供 Dify / 上游 LLM 对照填写）----------
INPUT_PARAM_REMARKS: dict[str, Any] = {
    "customer_demand": {
        "_说明": "客户需求，不参与报价计算，仅作订单信息",
        "delivery_date": "交期，如 2026-6-20",
        "remark": "客户备注",
    },
    "customer_info": {
        "_说明": "客户联系信息，不参与报价计算",
        "company": "公司名称",
        "contact": "联系人",
        "email": "邮箱",
        "phone": "电话",
    },
    "material": {
        "_说明": "材料相关，影响 PP、铜箔费用",
        "pp_type": "PP 型号：1080 / 2116 / 7628，单价 18 元/张",
        "pp_sheet_count": "PP 张数；不填则默认 layer_count-1",
        "copper_thickness": "成品铜厚：HOZ(0.5OZ) / 1OZ / 2OZ / 3OZ，按双面铜单价×面积",
        "copper_add_hoz_area_m2": "每额外增加 1HOZ 需计价的面积(㎡)，×42 元/㎡",
    },
    "pcb_base": {
        "_说明": "板子基础参数，决定面积、层数、压合与加工费档位",
        "product_name": "产品名称，不参与计算",
        "model": "型号/版本，不参与计算",
        "layer_count": "层数：1/2/4/6/8/10/12，决定压合单价与加工费区间",
        "quantity_pcs": "订单数量(片)，与 size_mm 一起可推算总面积",
        "size_mm": "[长mm, 宽mm] 单片尺寸；面积=长×宽×数量÷10⁶",
        "total_area_m2": "总面积(㎡)；>0 时优先使用，不再用尺寸推算",
        "board_type": "板材类型；含「无卤素」「高TG」时压合费+5%",
        "board_thickness_mm": "成品板厚(mm)；≥2.0 压合+5%，≥3.0 再+10%",
        "thickness_type": "板厚区间文字：<2.0 / >=2.0 / >=3.0，与 board_thickness_mm 二选一即可",
        "material_utilization": "板材利用率(%)，<78 且提供了板材单价时会加价",
        "board_material_price_per_m2": "板材单价(元/㎡)，按实际板材价格×面积；未填则板材项为 0",
    },
    "process": {
        "_说明": "工艺选项，大部分按 元/㎡ × 面积 计费",
        "secondary_press": "是否二次压合，true 则 +71 元/㎡",
        "press_layer": "保留字段，计价以 pcb_base.layer_count 为准，本字段可忽略",
        "special_press": "特殊压合备注，当前未单独计价",
        "route_length_inch": "锣程总长度(英寸)；>3000 时超出部分 ×0.0006×面积",
        "drill_hole_wan": "钻孔密度：万孔/㎡；>18 时超出部分 ×4 元/㎡×面积",
        "special_hole": "特殊孔工艺列表：树脂塞孔(70) / 电镀填平(70) / 电镀填孔(120) 元/㎡",
        "metal_edge": "金属包边，true 则 +30 元/㎡",
        "half_hole": "半孔：['单边'] +30元/㎡；含「四边」再 +30元/㎡",
        "solder_mask": "阻焊：['二次2-3OZ'] 20元/㎡；['二次4-6OZ'] 30元/㎡",
        "bevel": "斜边：['外斜边'] 30元/㎡；['内斜边'] 需外发询价不计价",
        "special_coating": "特殊涂层：['蓝胶'] 或 ['碳油'] 各 30元/㎡",
        "second_drill": "二钻，true 则约 12.5元/㎡(10–15 中值)",
        "second_route": "二锣，true 则约 12.5元/㎡(10–15 中值)",
        "chemical_selection": "选化工艺，true 则 +40 元/㎡",
        "surface_treatment": "表面处理：喷锡21 / 沉锡50 / 沉银55 / 沉金(需另填金价)",
        "gold_plating_percent": "沉金受镀面积占板面积百分比；≤20% 按 20% 计",
        "gold_plating_price_per_m2": "沉金单价(元/㎡)，沉金时必填",
        "special_type": "特殊板类型：['HDI'] 加工费+60元/㎡；['电镀填平'] 加工费+60元/㎡",
        "blind_via": "盲孔，true 则 +25 元/㎡(50万孔以内/㎡)",
        "buried_via": "埋孔，true 则 +10 元/㎡(10万孔以内/㎡)",
        "extra_layer": "多做一次线路，true 则 +45 元/㎡",
        "extra_plating": "多做一次电镀，true 则 +45 元/㎡",
    },
}

# ---------- 出参字段说明 ----------
OUTPUT_PARAM_REMARKS: dict[str, str] = {
    "error": "错误信息；空字符串表示计算成功",
    "area_m2": "参与计价的总面积(㎡)，字符串",
    "material_total": "材料合计(元)，字符串",
    "process_total": "工艺合计(元)，字符串",
    "total_price": "总价(元)，字符串",
    "price_breakdown": "分项明细 JSON 字符串（Dify 下一节点用 {{price_breakdown}} 引用）",
    "price_breakdown_summary": "分项报价简明文本，便于 LLM 直接阅读",
    "notes": "计算过程提示，如利用率不足、内斜边外发等",
    "param_remarks": "入参各字段中文说明(本字典的副本，便于下游展示)",
    "company": "客户名称，来自 customer_info.company",
    "contact": "联系人，来自 customer_info.contact",
    "email": "邮箱，来自 customer_info.email",
    "phone": "电话，来自 customer_info.phone",
    "product_name": "产品名称，来自 pcb_base.product_name",
    "layer_count": "层数，来自 pcb_base.layer_count",
    "delivery_date": "交期，来自 customer_demand.delivery_date",
}

BREAKDOWN_REMARKS: dict[str, str] = {
    "board_material": "一、板材：单价×面积；利用率<78% 可能加价",
    "pp": "二、PP片：18元/张×张数",
    "copper": "三、铜箔：双面铜单价×面积 + 每HOZ加价区×42",
    "press": "四、压合：按层数单价×面积；二次压合+71；无卤/高TG、厚板系数",
    "route": "五、锣程：超出3000英寸部分×0.0006×面积",
    "drill": "六、钻孔：超出18万孔/㎡部分×4×面积",
    "special_hole": "七、特殊孔：树脂塞孔/电镀填平/电镀填孔",
    "metal_edge_half_hole": "八、金属包边30 + 半孔(单边30、四边再加30) 元/㎡",
    "solder_mask": "九、阻焊：二次2-3OZ 或 4-6OZ",
    "bevel": "十、斜边：外斜边30元/㎡",
    "special_coating": "十一、特殊涂层：蓝胶/碳油 30元/㎡",
    "second_drill_route": "十二、二钻/二锣：各约10–15元/㎡",
    "chemical_selection": "十三、选化：40元/㎡",
    "surface_treatment": "十四、表面处理：喷锡/沉锡/沉银/沉金",
    "process_fee": "十五、加工费：按层数区间中值×面积；HDI/电镀填平各+60",
    "blind_buried_via": "十六、盲孔25 + 埋孔10 元/㎡",
    "extra_layer": "十七、额外线路层：45元/㎡",
    "extra_plating": "十八、额外电镀：45元/㎡",
}

# ---------- 常量 ----------
PP_PRICE_PER_SHEET = 18.0
PP_TYPES = frozenset({"1080", "2116", "7628"})

COPPER_PRICE_DOUBLE: dict[str, float] = {
    "HOZ": 35.04,
    "0.5OZ": 35.04,
    "17UM": 35.04,
    "1OZ": 70.08,
    "2OZ": 140.15,
    "3OZ": 210.23,
}
COPPER_ADD_PER_M2 = 42.0

PRESS_PRICE_PER_M2: dict[int, float] = {
    4: 110.0,
    6: 190.0,
    8: 300.0,
    10: 450.0,
    12: 650.0,
}
SECONDARY_PRESS_ADD = 71.0

ROUTE_BASE_INCH = 3000
ROUTE_EXTRA_PER_INCH_PER_M2 = 0.0006

DRILL_BASE_WAN = 18.0
DRILL_EXTRA_PER_WAN_PER_M2 = 4.0

SPECIAL_HOLE_PRICE: dict[str, float] = {
    "树脂塞孔": 70.0,  # 60–80 取中值
    "电镀填平": 70.0,
    "电镀填孔": 120.0,
}

METAL_EDGE_PER_M2 = 30.0
HALF_HOLE_SINGLE_PER_M2 = 30.0
HALF_HOLE_FOUR_SIDE_EXTRA_PER_M2 = 30.0

SOLDER_MASK_PRICE: dict[str, float] = {
    "二次2-3OZ": 20.0,
    "二次2-3oz": 20.0,
    "二次4-6OZ": 30.0,
    "二次4-6oz": 30.0,
}

BEVEL_OUTER_PER_M2 = 30.0
COATING_PER_M2 = 30.0

SECOND_DRILL_RANGE = (10.0, 15.0)
SECOND_ROUTE_RANGE = (10.0, 15.0)

CHEMICAL_SELECTION_PER_M2 = 40.0

SURFACE_PRICE: dict[str, float] = {
    "喷锡": 21.0,
    "沉锡": 50.0,
    "沉银": 55.0,
}

PROCESS_FEE_RANGE: dict[int, tuple[float, float]] = {
    1: (120.0, 120.0),
    2: (200.0, 230.0),
    4: (240.0, 260.0),
    6: (260.0, 300.0),
    8: (290.0, 400.0),
    10: (550.0, 650.0),
    12: (800.0, 1000.0),
}
HDI_PROCESS_ADD = 60.0
FILL_PLATING_PROCESS_ADD = 60.0

BLIND_VIA_PER_M2 = 25.0
BURIED_VIA_PER_M2 = 10.0
EXTRA_LAYER_PER_M2 = 45.0
EXTRA_PLATING_PER_M2 = 45.0

MATERIAL_UTILIZATION_THRESHOLD = 78.0
HIGH_TG_HALOGEN_FREE_FACTOR = 1.05
THICK_GE_2MM_FACTOR = 1.05
THICK_GE_3MM_FACTOR = 1.10

GOLD_PLATING_MIN_PERCENT = 20.0


def _norm_copper_thickness(raw: str) -> str:
    s = (raw or "1OZ").strip().upper().replace(" ", "")
    if s in ("HOZ", "0.5OZ", "17UM", "17UM"):
        return "HOZ"
    if s.endswith("OZ") and s[:-2].isdigit():
        return f"{int(float(s[:-2]))}OZ" if s[0] != "0" else "HOZ"
    return s if s in COPPER_PRICE_DOUBLE else "1OZ"


def _press_tier(layer_count: int) -> int:
    tiers = sorted(PRESS_PRICE_PER_M2.keys())
    for t in tiers:
        if layer_count <= t:
            return t
    return tiers[-1]


def _process_fee_mid(layer_count: int) -> float:
    if layer_count <= 1:
        lo, hi = PROCESS_FEE_RANGE[1]
    elif layer_count == 2:
        lo, hi = PROCESS_FEE_RANGE[2]
    else:
        tier = _press_tier(layer_count)
        lo, hi = PROCESS_FEE_RANGE.get(tier, PROCESS_FEE_RANGE[12])
    return (lo + hi) / 2.0


def _calc_area_m2(pcb_base: dict[str, Any]) -> float:
    total = float(pcb_base.get("total_area_m2") or 0)
    if total > 0:
        return total
    size = pcb_base.get("size_mm") or []
    qty = int(pcb_base.get("quantity_pcs") or 0)
    if len(size) >= 2 and qty > 0:
        w, h = float(size[0]), float(size[1])
        return w * h / 1_000_000.0 * qty
    return 0.0


def _is_high_tg_or_halogen_free(board_type: str) -> bool:
    t = (board_type or "").strip()
    return "高TG" in t or "高tg" in t or "无卤" in t or "无卤素" in t


def _thickness_factors(board_thickness_mm: float, thickness_type: str) -> tuple[float, list[str]]:
    notes: list[str] = []
    factor = 1.0
    mm = float(board_thickness_mm or 0)
    tt = (thickness_type or "").strip()

    ge2 = mm >= 2.0 or tt in (">=2.0", "≥2.0", ">=2.0", "2.0-3.0", "≥2.0MM")
    ge3 = mm >= 3.0 or tt in (">=3.0", "≥3.0", ">=3.0", "≥3.0MM")

    if ge2:
        factor *= THICK_GE_2MM_FACTOR
        notes.append("板厚≥2.0MM +5%")
    if ge3:
        factor *= THICK_GE_3MM_FACTOR
        notes.append("板厚≥3.0MM +10%")
    return factor, notes


def _mid_range(lo: float, hi: float) -> float:
    return (lo + hi) / 2.0


_TOP_LEVEL_NUMERIC_KEYS = ("area_m2", "total_price", "material_total", "process_total")


def _strify_value(v: Any) -> Any:
    """将 int/float 转为字符串；bool、str、None 等保持不变。"""
    if isinstance(v, bool):
        return v
    if isinstance(v, int):
        return str(v)
    if isinstance(v, float):
        return str(v)
    if isinstance(v, dict):
        return {k: _strify_value(x) for k, x in v.items()}
    if isinstance(v, list):
        return [_strify_value(x) for x in v]
    return v


def _selected_label(value: str | list[str] | None, *, empty: str = "未选择") -> str:
    """格式：已选【沉锡】或 已选【树脂塞孔、碳油】。"""
    if isinstance(value, list):
        names = [str(x).strip() for x in value if str(x).strip()]
        return f"已选【{'、'.join(names)}】" if names else empty
    s = str(value or "").strip()
    return f"已选【{s}】" if s else empty


def _area_price_line(name: str, unit: float, area: float) -> str:
    return f"{_selected_label(name)}{unit}元/㎡×{area}㎡"


def _breakdown_line(key: str, block: dict[str, Any]) -> str:
    """单项摘要：展示实际选择项 + 计算公式，不用规则里的全部可选项。"""
    amount = block.get("amount", "")
    title = block.get("title") or BREAKDOWN_REMARKS.get(key, key)
    detail = block.get("calc_detail")
    if detail:
        return f"- {title}：{detail}，合计 {amount} 元"
    selected = block.get("selected")
    if selected:
        return f"- {title}：{_selected_label(selected)}，合计 {amount} 元"
    return f"- {title}：未选择，合计 {amount} 元"


def _breakdown_to_summary(breakdown: dict[str, Any]) -> str:
    """将分项 dict 转为多行文本，供 LLM 节点直接使用。"""
    if not breakdown:
        return ""
    lines: list[str] = []
    for key, block in breakdown.items():
        if isinstance(block, dict):
            lines.append(_breakdown_line(key, block))
    return "\n".join(lines)


def _format_dify_output(result: dict[str, Any]) -> dict[str, Any]:
    """Dify 代码节点出参：金额等为 string；price_breakdown 为 JSON 字符串。"""
    out = dict(result)
    for key in _TOP_LEVEL_NUMERIC_KEYS:
        v = out.get(key)
        if v is not None and not isinstance(v, str):
            out[key] = str(v)

    pb = out.get("price_breakdown")
    if pb is not None:
        if isinstance(pb, str):
            pb_dict: Any = json.loads(pb) if pb.strip().startswith("{") else {}
        else:
            pb_dict = _strify_value(pb)
        out["price_breakdown_summary"] = _breakdown_to_summary(pb_dict)
        out["price_breakdown"] = json.dumps(pb_dict, ensure_ascii=False, indent=2)

    for obj_key in ("param_remarks", "output_remarks", "notes"):
        v = out.get(obj_key)
        if v is not None and not isinstance(v, str):
            out[obj_key] = json.dumps(v, ensure_ascii=False)

    return out


def _with_breakdown_remark(key: str, block: dict[str, Any]) -> dict[str, Any]:
    """为分项明细附加 remark 字段。"""
    out = dict(block)
    out["remark"] = BREAKDOWN_REMARKS.get(key, "")
    return out


def _extract_pcb_summary(pcb_data: dict[str, Any]) -> dict[str, str]:
    """从 pcb_data 提取展示用字段（均为字符串，供 Dify 出参）。"""
    customer_info = pcb_data.get("customer_info") or {}
    customer_demand = pcb_data.get("customer_demand") or {}
    pcb_base = pcb_data.get("pcb_base") or {}
    layer = pcb_base.get("layer_count")
    return {
        "company": str(customer_info.get("company") or "").strip(),
        "contact": str(customer_info.get("contact") or "").strip(),
        "email": str(customer_info.get("email") or "").strip(),
        "phone": str(customer_info.get("phone") or "").strip(),
        "product_name": str(pcb_base.get("product_name") or "").strip(),
        "layer_count": "" if layer is None else str(layer).strip(),
        "delivery_date": str(customer_demand.get("delivery_date") or "").strip(),
    }


def _unwrap_pcb_data(raw: Any) -> dict[str, Any]:
    if raw is None:
        return {}
    if isinstance(raw, dict):
        if "pcb_data" in raw and isinstance(raw["pcb_data"], dict):
            return raw["pcb_data"]
        return raw
    return {}


def calculate_price(pcb_data: dict[str, Any]) -> dict[str, Any]:
    material = pcb_data.get("material") or {}
    pcb_base = pcb_data.get("pcb_base") or {}
    process = pcb_data.get("process") or {}

    area = _calc_area_m2(pcb_base)
    if area <= 0:
        return _format_dify_output(
            {
                "error": "无法计算面积：请提供 total_area_m2 或 size_mm + quantity_pcs",
                "area_m2": "0",
                "price_breakdown": {},
                "total_price": "0",
                "material_total": "0",
                "process_total": "0",
                "notes": [],
                "param_remarks": INPUT_PARAM_REMARKS,
                "output_remarks": OUTPUT_PARAM_REMARKS,
                **_extract_pcb_summary(pcb_data),
            }
        )

    layer_count = int(pcb_base.get("layer_count") or 2)
    breakdown: dict[str, Any] = {}
    notes: list[str] = []

    # 一、板材（可选单价；利用率<78% 加价）
    util = float(pcb_base.get("material_utilization") or 100)
    board_price_per_m2 = float(pcb_base.get("board_material_price_per_m2") or 0)
    board_cost = board_price_per_m2 * area
    util_surcharge = 0.0
    if util > 0 and util < MATERIAL_UTILIZATION_THRESHOLD and board_cost > 0:
        util_surcharge = board_cost * (MATERIAL_UTILIZATION_THRESHOLD / util - 1.0)
        notes.append(f"板材利用率{util}%<78%，材料加价")
    elif util > 0 and util < MATERIAL_UTILIZATION_THRESHOLD:
        notes.append(f"板材利用率{util}%<78%，需额外加价（未提供 board_material_price_per_m2）")
    board_type = str(pcb_base.get("board_type") or "").strip()
    board_detail = (
        f"板材类型【{board_type}】利用率{util}%"
        if board_type
        else f"利用率{util}%"
    )
    if board_price_per_m2 > 0:
        board_detail += f"，{board_price_per_m2}元/㎡×{area}㎡"
    else:
        board_detail += "，未提供板材单价"
    breakdown["board_material"] = _with_breakdown_remark(
        "board_material",
        {
            "amount": round(board_cost + util_surcharge, 2),
            "board_cost": round(board_cost, 2),
            "utilization_surcharge": round(util_surcharge, 2),
            "utilization_percent": util,
            "selected": board_type or None,
            "calc_detail": board_detail,
        },
    )

    # 二、PP片
    pp_type = (material.get("pp_type") or "1080").strip()
    pp_sheets = int(material.get("pp_sheet_count") or max(1, layer_count - 1))
    pp_unit = PP_PRICE_PER_SHEET if pp_type in PP_TYPES else PP_PRICE_PER_SHEET
    pp_cost = pp_unit * pp_sheets
    breakdown["pp"] = _with_breakdown_remark(
        "pp",
        {
            "amount": round(pp_cost, 2),
            "pp_type": pp_type,
            "sheet_count": pp_sheets,
            "unit_price": pp_unit,
            "selected": pp_type,
            "calc_detail": f"已选【{pp_type}】{pp_unit}元/张×{pp_sheets}张",
        },
    )

    # 三、铜箔
    copper_key = _norm_copper_thickness(material.get("copper_thickness") or "1OZ")
    copper_unit = COPPER_PRICE_DOUBLE.get(copper_key, COPPER_PRICE_DOUBLE["1OZ"])
    copper_cost = copper_unit * area
    add_area = float(material.get("copper_add_hoz_area_m2") or 0)
    copper_add_cost = COPPER_ADD_PER_M2 * add_area
    copper_parts = [f"双面铜{copper_unit}元/㎡×{area}㎡"]
    if copper_add_cost > 0:
        copper_parts.append(f"每HOZ加价区{add_area}㎡×42元/㎡")
    breakdown["copper"] = _with_breakdown_remark(
        "copper",
        {
            "amount": round(copper_cost + copper_add_cost, 2),
            "copper_cost": round(copper_cost, 2),
            "copper_add_cost": round(copper_add_cost, 2),
            "thickness": copper_key,
            "unit_price_double_per_m2": copper_unit,
            "area_m2": area,
            "selected": copper_key,
            "calc_detail": f"已选【{copper_key}】" + " + ".join(copper_parts),
        },
    )

    # 四、压合
    press_tier = _press_tier(layer_count)
    press_unit = PRESS_PRICE_PER_M2.get(press_tier, PRESS_PRICE_PER_M2[12])
    press_cost = press_unit * area
    if process.get("secondary_press"):
        press_cost += SECONDARY_PRESS_ADD * area
    press_factor, press_notes = 1.0, []
    if _is_high_tg_or_halogen_free(pcb_base.get("board_type") or ""):
        press_factor *= HIGH_TG_HALOGEN_FREE_FACTOR
        press_notes.append("高TG/无卤素 +5%")
    thick_factor, thick_notes = _thickness_factors(
        float(pcb_base.get("board_thickness_mm") or 0),
        str(pcb_base.get("thickness_type") or ""),
    )
    press_factor *= thick_factor
    press_notes.extend(thick_notes)
    press_cost *= press_factor
    press_selected: list[str] = [f"{layer_count}层压合"]
    if process.get("secondary_press"):
        press_selected.append("二次压合")
    if board_type and _is_high_tg_or_halogen_free(board_type):
        press_selected.append(board_type)
    press_formula = f"已选【{'、'.join(press_selected)}】{press_unit}元/㎡×{area}㎡"
    if process.get("secondary_press"):
        press_formula += f" + 二次压合71×{area}㎡"
    if press_factor != 1.0:
        press_formula += f" ×系数{press_factor}"
    breakdown["press"] = _with_breakdown_remark(
        "press",
        {
            "amount": round(press_cost, 2),
            "tier_layers": press_tier,
            "unit_price_per_m2": press_unit,
            "secondary_press": bool(process.get("secondary_press")),
            "factor": press_factor,
            "notes": press_notes,
            "selected": press_selected,
            "calc_detail": press_formula,
        },
    )

    # 五、锣程
    route_inch = float(process.get("route_length_inch") or 0)
    route_cost = 0.0
    if route_inch > ROUTE_BASE_INCH:
        route_cost = (route_inch - ROUTE_BASE_INCH) * ROUTE_EXTRA_PER_INCH_PER_M2 * area
    route_detail = (
        f"锣程{route_inch}英寸，超出{max(0.0, route_inch - ROUTE_BASE_INCH):.0f}英寸×0.0006×{area}㎡"
        if route_inch > ROUTE_BASE_INCH
        else f"锣程{route_inch}英寸（未超基准{ROUTE_BASE_INCH}）"
    )
    breakdown["route"] = _with_breakdown_remark(
        "route",
        {
            "amount": round(route_cost, 2),
            "route_length_inch": route_inch,
            "excess_inch": max(0.0, route_inch - ROUTE_BASE_INCH),
            "calc_detail": route_detail,
        },
    )

    # 六、钻孔（万孔/㎡）
    drill_wan = float(process.get("drill_hole_wan") or 0)
    drill_cost = 0.0
    if drill_wan > DRILL_BASE_WAN:
        drill_cost = (drill_wan - DRILL_BASE_WAN) * DRILL_EXTRA_PER_WAN_PER_M2 * area
    drill_detail = (
        f"钻孔{drill_wan}万孔/㎡，超出{max(0.0, drill_wan - DRILL_BASE_WAN):.0f}万孔×4×{area}㎡"
        if drill_wan > DRILL_BASE_WAN
        else f"钻孔{drill_wan}万孔/㎡（未超基准{DRILL_BASE_WAN}万孔/㎡）"
    )
    breakdown["drill"] = _with_breakdown_remark(
        "drill",
        {
            "amount": round(drill_cost, 2),
            "drill_hole_wan_per_m2": drill_wan,
            "excess_wan": max(0.0, drill_wan - DRILL_BASE_WAN),
            "calc_detail": drill_detail,
        },
    )

    # 七、特殊孔
    special_hole_cost = 0.0
    special_hole_items: list[dict[str, Any]] = []
    for name in process.get("special_hole") or []:
        key = str(name).strip()
        unit = SPECIAL_HOLE_PRICE.get(key)
        if unit is None:
            continue
        cost = unit * area
        special_hole_cost += cost
        special_hole_items.append({"name": key, "unit_per_m2": unit, "amount": round(cost, 2)})
    hole_names = [i["name"] for i in special_hole_items]
    hole_detail = (
        " + ".join(
            f"已选【{i['name']}】{i['unit_per_m2']}元/㎡×{area}㎡" for i in special_hole_items
        )
        if special_hole_items
        else "未选择"
    )
    breakdown["special_hole"] = _with_breakdown_remark(
        "special_hole",
        {
            "amount": round(special_hole_cost, 2),
            "items": special_hole_items,
            "selected": hole_names,
            "calc_detail": hole_detail,
        },
    )

    # 八、金属包边 / 半孔
    metal_cost = METAL_EDGE_PER_M2 * area if process.get("metal_edge") else 0.0
    half_holes = [str(x).strip() for x in (process.get("half_hole") or [])]
    half_cost = 0.0
    if "单边" in half_holes:
        half_cost += HALF_HOLE_SINGLE_PER_M2 * area
    if "四边" in half_holes:
        half_cost += HALF_HOLE_FOUR_SIDE_EXTRA_PER_M2 * area
    edge_parts: list[str] = []
    edge_selected: list[str] = []
    if process.get("metal_edge"):
        edge_selected.append("金属包边")
        edge_parts.append(f"已选【金属包边】30元/㎡×{area}㎡")
    if half_holes:
        edge_selected.extend(half_holes)
        edge_parts.append(f"已选【{'、'.join(half_holes)}半孔】")
        if "单边" in half_holes:
            edge_parts.append(f"单边30元/㎡×{area}㎡")
        if "四边" in half_holes:
            edge_parts.append(f"四边再加30元/㎡×{area}㎡")
    breakdown["metal_edge_half_hole"] = _with_breakdown_remark(
        "metal_edge_half_hole",
        {
            "amount": round(metal_cost + half_cost, 2),
            "metal_edge": round(metal_cost, 2),
            "half_hole": round(half_cost, 2),
            "selected": edge_selected,
            "calc_detail": " + ".join(edge_parts) if edge_parts else "未选择",
        },
    )

    # 九、阻焊
    solder_cost = 0.0
    solder_items: list[dict[str, Any]] = []
    for name in process.get("solder_mask") or []:
        key = str(name).strip()
        unit = SOLDER_MASK_PRICE.get(key) or SOLDER_MASK_PRICE.get(key.upper())
        if unit is None:
            continue
        cost = unit * area
        solder_cost += cost
        solder_items.append({"name": key, "unit_per_m2": unit, "amount": round(cost, 2)})
    solder_names = [i["name"] for i in solder_items]
    solder_detail = (
        " + ".join(
            f"已选【{i['name']}】{i['unit_per_m2']}元/㎡×{area}㎡" for i in solder_items
        )
        if solder_items
        else "未选择"
    )
    breakdown["solder_mask"] = _with_breakdown_remark(
        "solder_mask",
        {
            "amount": round(solder_cost, 2),
            "items": solder_items,
            "selected": solder_names,
            "calc_detail": solder_detail,
        },
    )

    # 十、斜边
    bevel_cost = 0.0
    bevel_list = [str(x).strip() for x in (process.get("bevel") or [])]
    if "外斜边" in bevel_list:
        bevel_cost = BEVEL_OUTER_PER_M2 * area
    if "内斜边" in bevel_list:
        notes.append("内斜边需外发询价，未计入金额")
    bevel_detail = (
        " + ".join(f"已选【{t}】30元/㎡×{area}㎡" for t in bevel_list if t == "外斜边")
        if "外斜边" in bevel_list
        else ("已选【内斜边】需外发询价" if "内斜边" in bevel_list else "未选择")
    )
    breakdown["bevel"] = _with_breakdown_remark(
        "bevel",
        {
            "amount": round(bevel_cost, 2),
            "types": bevel_list,
            "selected": bevel_list,
            "calc_detail": bevel_detail,
        },
    )

    # 十一、特殊涂层
    coating_cost = 0.0
    coating_items: list[str] = []
    for name in process.get("special_coating") or []:
        key = str(name).strip()
        if key in ("蓝胶", "碳油"):
            coating_cost += COATING_PER_M2 * area
            coating_items.append(key)
    coating_detail = (
        " + ".join(f"已选【{k}】30元/㎡×{area}㎡" for k in coating_items)
        if coating_items
        else "未选择"
    )
    breakdown["special_coating"] = _with_breakdown_remark(
        "special_coating",
        {
            "amount": round(coating_cost, 2),
            "items": coating_items,
            "selected": coating_items,
            "calc_detail": coating_detail,
        },
    )

    # 十二、二钻 / 二锣
    second_drill_cost = 0.0
    if process.get("second_drill"):
        second_drill_cost = _mid_range(*SECOND_DRILL_RANGE) * area
    second_route_cost = 0.0
    if process.get("second_route"):
        second_route_cost = _mid_range(*SECOND_ROUTE_RANGE) * area
    second_parts: list[str] = []
    second_selected: list[str] = []
    mid_drill = _mid_range(*SECOND_DRILL_RANGE)
    mid_route = _mid_range(*SECOND_ROUTE_RANGE)
    if process.get("second_drill"):
        second_selected.append("二钻")
        second_parts.append(f"已选【二钻】{mid_drill}元/㎡×{area}㎡")
    if process.get("second_route"):
        second_selected.append("二锣")
        second_parts.append(f"已选【二锣】{mid_route}元/㎡×{area}㎡")
    breakdown["second_drill_route"] = _with_breakdown_remark(
        "second_drill_route",
        {
            "amount": round(second_drill_cost + second_route_cost, 2),
            "second_drill": round(second_drill_cost, 2),
            "second_route": round(second_route_cost, 2),
            "selected": second_selected,
            "calc_detail": " + ".join(second_parts) if second_parts else "未选择",
        },
    )

    # 十三、选化
    chemical_cost = CHEMICAL_SELECTION_PER_M2 * area if process.get("chemical_selection") else 0.0
    breakdown["chemical_selection"] = _with_breakdown_remark(
        "chemical_selection",
        {
            "amount": round(chemical_cost, 2),
            "selected": "选化" if process.get("chemical_selection") else None,
            "calc_detail": (
                f"已选【选化】{CHEMICAL_SELECTION_PER_M2}元/㎡×{area}㎡"
                if process.get("chemical_selection")
                else "未选择"
            ),
        },
    )

    # 十四、表面处理
    surface_name = str(process.get("surface_treatment") or "").strip()
    surface_cost = 0.0
    if surface_name == "沉金":
        pct = float(process.get("gold_plating_percent") or 0)
        effective_pct = max(pct, GOLD_PLATING_MIN_PERCENT) / 100.0
        gold_unit = float(process.get("gold_plating_price_per_m2") or 0)
        surface_cost = gold_unit * effective_pct * area
        breakdown["surface_treatment"] = _with_breakdown_remark(
            "surface_treatment",
            {
                "amount": round(surface_cost, 2),
                "type": surface_name,
                "gold_percent": effective_pct * 100,
                "note": "3U金厚需另行计价" if not process.get("gold_plating_price_per_m2") else "",
                "selected": surface_name,
                "calc_detail": (
                    f"已选【沉金】受镀面积{effective_pct * 100:.0f}%"
                    f"×{gold_unit}元/㎡×{area}㎡"
                    if gold_unit
                    else "已选【沉金】需填写 gold_plating_price_per_m2"
                ),
            },
        )
    else:
        unit = SURFACE_PRICE.get(surface_name, 0.0)
        surface_cost = unit * area
        surface_detail = (
            f"已选【{surface_name}】{unit}元/㎡×{area}㎡"
            if surface_name
            else "未选择"
        )
        breakdown["surface_treatment"] = _with_breakdown_remark(
            "surface_treatment",
            {
                "amount": round(surface_cost, 2),
                "type": surface_name,
                "unit_per_m2": unit,
                "selected": surface_name or None,
                "calc_detail": surface_detail,
            },
        )

    # 十五、加工费
    process_unit = _process_fee_mid(layer_count)
    process_cost = process_unit * area
    special_types = [str(x).strip() for x in (process.get("special_type") or [])]
    process_addons: list[str] = []
    if "HDI" in special_types or "hdi" in [s.lower() for s in special_types]:
        process_cost += HDI_PROCESS_ADD * area
        process_addons.append("HDI +60元/㎡")
    if "电镀填平" in special_types:
        process_cost += FILL_PLATING_PROCESS_ADD * area
        process_addons.append("电镀填平加工费 +60元/㎡")
    fee_detail = f"已选【{layer_count}层板】{process_unit}元/㎡×{area}㎡"
    if process_addons:
        fee_detail += "；" + "；".join(process_addons)
    breakdown["process_fee"] = _with_breakdown_remark(
        "process_fee",
        {
            "amount": round(process_cost, 2),
            "layer_count": layer_count,
            "unit_mid_per_m2": process_unit,
            "addons": process_addons,
            "selected": special_types or [f"{layer_count}层"],
            "calc_detail": fee_detail,
        },
    )

    # 十六、盲埋孔
    blind_cost = BLIND_VIA_PER_M2 * area if process.get("blind_via") else 0.0
    buried_cost = BURIED_VIA_PER_M2 * area if process.get("buried_via") else 0.0
    via_parts: list[str] = []
    via_selected: list[str] = []
    if process.get("blind_via"):
        via_selected.append("盲孔")
        via_parts.append(f"已选【盲孔】25元/㎡×{area}㎡")
    if process.get("buried_via"):
        via_selected.append("埋孔")
        via_parts.append(f"已选【埋孔】10元/㎡×{area}㎡")
    breakdown["blind_buried_via"] = _with_breakdown_remark(
        "blind_buried_via",
        {
            "amount": round(blind_cost + buried_cost, 2),
            "blind_via": round(blind_cost, 2),
            "buried_via": round(buried_cost, 2),
            "selected": via_selected,
            "calc_detail": " + ".join(via_parts) if via_parts else "未选择",
        },
    )

    # 十七、额外线路层
    extra_layer_cost = EXTRA_LAYER_PER_M2 * area if process.get("extra_layer") else 0.0
    breakdown["extra_layer"] = _with_breakdown_remark(
        "extra_layer",
        {
            "amount": round(extra_layer_cost, 2),
            "selected": "额外线路层" if process.get("extra_layer") else None,
            "calc_detail": (
                f"已选【额外线路层】{EXTRA_LAYER_PER_M2}元/㎡×{area}㎡"
                if process.get("extra_layer")
                else "未选择"
            ),
        },
    )

    # 十八、额外电镀
    extra_plating_cost = EXTRA_PLATING_PER_M2 * area if process.get("extra_plating") else 0.0
    breakdown["extra_plating"] = _with_breakdown_remark(
        "extra_plating",
        {
            "amount": round(extra_plating_cost, 2),
            "selected": "额外电镀" if process.get("extra_plating") else None,
            "calc_detail": (
                f"已选【额外电镀】{EXTRA_PLATING_PER_M2}元/㎡×{area}㎡"
                if process.get("extra_plating")
                else "未选择"
            ),
        },
    )

    material_total = (
        breakdown["board_material"]["amount"]
        + breakdown["pp"]["amount"]
        + breakdown["copper"]["amount"]
    )
    process_total = sum(
        breakdown[k]["amount"]
        for k in (
            "press",
            "route",
            "drill",
            "special_hole",
            "metal_edge_half_hole",
            "solder_mask",
            "bevel",
            "special_coating",
            "second_drill_route",
            "chemical_selection",
            "surface_treatment",
            "process_fee",
            "blind_buried_via",
            "extra_layer",
            "extra_plating",
        )
    )
    total = material_total + process_total

    return _format_dify_output(
        {
            "error": "",
            "area_m2": round(area, 6),
            "material_total": round(material_total, 2),
            "process_total": round(process_total, 2),
            "total_price": round(total, 2),
            "price_breakdown": breakdown,
            "notes": notes,
            "param_remarks": INPUT_PARAM_REMARKS,
            "output_remarks": OUTPUT_PARAM_REMARKS,
            **_extract_pcb_summary(pcb_data),
        }
    )


def main(pcb_data: Any = None, arg1: Any = None, **kwargs: Any) -> dict[str, Any]:
    """
    Dify 入口：返回分项价格与总价。

    返回字段除金额外，还包含：
    - param_remarks：入参 pcb_data 各字段中文说明
    - output_remarks：出参顶层字段说明
    - price_breakdown.*.remark：各分项计价含义
    - company / contact / email / phone / product_name / layer_count / delivery_date：订单摘要
    - price_breakdown：JSON 字符串；简明版用 price_breakdown_summary
    """
    payload = pcb_data if pcb_data is not None else arg1
    if payload is None and kwargs:
        payload = kwargs.get("pcb_data") or next(
            (v for v in kwargs.values() if isinstance(v, dict)),
            None,
        )
    data = _unwrap_pcb_data(payload)
    if not data:
        return _format_dify_output(
            {
                "error": "pcb_data 为空",
                "area_m2": "0",
                "total_price": "0",
                "material_total": "0",
                "process_total": "0",
                "price_breakdown": {},
                "price_breakdown_summary": "",
                "notes": [],
                "param_remarks": INPUT_PARAM_REMARKS,
                "output_remarks": OUTPUT_PARAM_REMARKS,
                "company": "",
                "contact": "",
                "email": "",
                "phone": "",
                "product_name": "",
                "layer_count": "",
                "delivery_date": "",
            }
        )
    return _format_dify_output(calculate_price(data))


if __name__ == "__main__":
    import json
    import sys

    # 示例入参（字段含义见 INPUT_PARAM_REMARKS 或运行结果中的 param_remarks）
    sample = {
        "customer_demand": {
            "delivery_date": "2026-6-20",  # 交期，不计价
            "remark": "无",
        },
        "customer_info": {  # 客户信息，不计价
            "company": "爱尚云科技",
            "contact": "张三",
            "email": "aishangyun@163.com",
            "phone": "18538383839",
        },
        "material": {
            "pp_type": "1080",  # PP型号 1080/2116/7628
            "copper_thickness": "1OZ",  # 铜厚 HOZ/1OZ/2OZ/3OZ
            "copper_add_hoz_area_m2": 0,  # 每加1HOZ的加价面积(㎡)
            # "pp_sheet_count": 9,  # 可选，PP张数，默认 layer_count-1
        },
        "pcb_base": {
            "product_name": "智能控制板",
            "model": "V1.2",
            "layer_count": 10,  # 层数，决定压合/加工费档位
            "quantity_pcs": 1000,  # 数量(片)
            "size_mm": [200, 100],  # 长宽 mm，与数量算面积
            "total_area_m2": 0,  # 有值则直接用，不推算
            "board_type": "无卤素",  # 无卤/高TG 压合+5%
            "board_thickness_mm": 0,  # 板厚 mm
            "thickness_type": "<2.0",  # 或 >=2.0 / >=3.0
            "material_utilization": 80,  # 利用率%，<78 可能加价
            # "board_material_price_per_m2": 120,  # 可选，板材单价
        },
        "process": {
            "secondary_press": True,  # 二次压合 +71元/㎡
            "route_length_inch": 3000,  # 锣程(英寸)，超3000加价
            "drill_hole_wan": 10,  # 钻孔 万孔/㎡，超18加价
            "special_hole": ["树脂塞孔"],  # 特殊孔工艺列表
            "metal_edge": True,  # 金属包边
            "half_hole": ["单边", "四边"],  # 半孔
            "solder_mask": ["二次2-3OZ"],  # 阻焊
            "bevel": ["外斜边"],  # 斜边
            "special_coating": ["碳油"],  # 蓝胶/碳油
            "second_drill": False,
            "second_route": True,  # 二锣
            "chemical_selection": False,  # 选化
            "surface_treatment": "沉锡",  # 喷锡/沉锡/沉银/沉金
            "gold_plating_percent": 0,  # 沉金受镀面积%
            "special_type": ["电镀填平"],  # HDI 或 电镀填平(加工费+60)
            "blind_via": True,
            "buried_via": False,
            "extra_layer": True,  # 多做一次线路
            "extra_plating": True,  # 多做一次电镀
            "press_layer": 4,  # 可忽略，以 layer_count 为准
            "special_press": [],
        },
    }
    out = main({"pcb_data": sample})
    json.dump(out, sys.stdout, ensure_ascii=False, indent=2)
    print()
