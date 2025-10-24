def isOdd(n):
    # 先判断是否为整数类型
    if not isinstance(n, int):
        return False
    # 再判断是否为奇数
    return n % 2 != 0
