# 递归

# 求任意数的阶乘
def factorial(n):
    # 基线条件 判断n是否为1，如果为1则此时不能再继续递归
    if n == 1:
        # 1的阶乘就是1，直接返回1
        return 1

    # 递归条件
    return n * factorial(n - 1)


print(factorial(3))
