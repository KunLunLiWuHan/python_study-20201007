"""
逻辑运算符
逻辑运算符主要用来做一些逻辑判断。
1、not 逻辑非
    not可以对符号右侧的值进行非运算；
    对于布尔值，非运算会对其进行取反操作，True变False，False变True。
    对于非布尔值，非运算会先将其转换为布尔值，然后再取反。
2、and 逻辑与
    and可以对符号两侧的值进行与运算，与运算是找False的。
3、or 逻辑或
    or 可以对符号两侧的值进行或运算，或运算是找True的。
"""
a = 2
a = not a
# 输出：False
print(a)

result = 1 and 2  # 2
result = 1 and 0  # 0
result = 0 and 1  # 0
result = 0 and None  # 0

result = 1 or 2  # 1
result = 1 or 0  # 1
result = 0 or 1  # 1
result = 0 or None  # None

