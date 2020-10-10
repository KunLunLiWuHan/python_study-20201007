# 高阶函数

# 创建一个列表
list_test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# 定义一个函数，用来检查一个任意的数字是否是偶数
def fn2(i):
    if i % 2 == 0:
        return True
    return False


# 该函数用来检查指定的数字是否大于5
def fn3(i):
    if i > 5:
        return True
    return False


#  lst：要进行筛选的列表
def fn4(func, lst):
    # 创建一个新列表
    new_list = []

    # 对列表进行筛选
    for n in lst:
        # 判断n的奇偶
        if func(n):
            new_list.append(n)
    # 返回新列表
    return new_list


# 输出：[2, 4, 6, 8, 10]
print(fn4(fn2, list_test))

"""
1、filter()
filter()可以从序列中过滤出符合条件的元素，保存到一个新的序列中
    参数：
        1.函数，根据该函数来过滤序列（可迭代的结构）
        2.需要过滤的序列（可迭代的结构）
    返回值：
      过滤后的新序列（可迭代的结构）
2、fn2是作为参数传递进filter()函数中，而fn2实际上只有一个作用，
就是作为filter()的参数，filter()调用完毕以后，fn2就已经没用。
"""
# 输出：<filter object at 0x00000221B178BA90>
print(filter(fn2, list_test))
# 输出：[2, 4, 6, 8, 10]
print(list(filter(fn2, list_test)))

