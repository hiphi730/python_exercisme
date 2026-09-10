def rebase(input_base, digits, output_base):
    """Convert digits from one number base to another."""

    # if：条件判断。输入进制必须至少是 2。
    if input_base < 2:
        # raise：主动抛出异常；ValueError 表示“值不合法”。
        raise ValueError("input base must be >= 2")

    # for ... in ...：依次遍历列表 digits 中的每一个数字。
    for digit in digits:
        # or：只要任一条件成立，就认为这个数字不合法。
        if digit < 0 or digit >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")

    if output_base < 2:
        raise ValueError("output base must be >= 2")

    # 先把输入进制转换为普通整数（十进制数值）。
    decimal_value = 0

    for digit in digits:
        # 这是“位值制”的计算方式：
        # 旧值乘输入进制，再加上下一个数字。
        decimal_value = decimal_value * input_base + digit

    # 空列表或全 0 的结果都应返回 [0]。
    if decimal_value == 0:
        return [0]

    # 再把整数转换为目标进制。
    output_digits = []

    while decimal_value > 0:
        # %：取余数，得到当前最低位。
        output_digits.append(decimal_value % output_base)

        # //：整除，去掉已经处理过的最低位。
        decimal_value //= output_base

    # [::-1]：切片语法，步长为 -1，表示把列表倒序。
    return output_digits[::-1]