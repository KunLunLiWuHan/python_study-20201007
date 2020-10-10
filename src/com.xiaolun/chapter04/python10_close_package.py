# 闭包

# 闭包，求一个列表中的平均数
def make_averager():
    # 创建一个列表，用来保存数值，嵌套的函数可以访问该列表。
    nums = []

    # 创建一个函数，用来计算平均值
    def averager(n):
        # 将n添加到列表中
        nums.append(n)
        # 求平均值
        return sum(nums) / len(nums)

    return averager


# 获取闭包中的内部函数
average_fun = make_averager()
# 输出：10.0
print(average_fun(10))
# 输出：15.0
print(average_fun(20))
