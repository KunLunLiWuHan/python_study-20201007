# 数值

# 在Python中所有的整数都是int类型
a = 10
print(a)

# 如果数字的长度过大，可以使用下划线作为分隔符
c = 123_456_789
print(c)

# d = 0123 10进制的数字不能以0开头
# 其他进制的整数，只要是数字打印时一定是以十进制的形式显示的
# 二进制 0b开头，输出为2
c = 0b10  # 二进制的10
print(c)
# 八进制 0o开头,输出为8
c = 0o10
print(c)
# 十六进制 0x开头，输出为16
c = 0x10
print(c)

# 浮点数（小数），在Python中所有的小数都是float类型
c = 1.23
print(c)

# 对浮点数进行运算时，可能会得到一个不精确的结果 0.30000000000000004
c = 0.1 + 0.2
print(c)
