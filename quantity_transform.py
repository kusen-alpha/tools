QUANTITY_UNIT_NUM_DICT = {
    'w': 10000,
    '万': 10000,
    'k': 1000,
    'W': 10000,
    'K': 1000,
    '亿': 100000000,
    '千': 1000,
    '百': 100,
    '十': 10,
    '千万': 10000000,
    '百万': 1000000,

}


def quantity_transform_zh_to_arab(s, unit=None):
    """
    数量转换|中文转阿拉伯数字
    :param s: 需转换的文本
    :param unit: 单位
    :return: float
    """
    s = s.replace(' ', '')
    if unit:
        return float(s.split(unit)[0]) * QUANTITY_UNIT_NUM_DICT[unit]
    for unit in QUANTITY_UNIT_NUM_DICT:
        if unit in s:
            return float(s.split(unit)[0]) * QUANTITY_UNIT_NUM_DICT[unit]
