# lambda表达式

# 第一种方式：定义函数的方式
def fn(a, b):
    return a + b


"""
1、语法
    lambda 参数列表 : 返回值
2、 匿名函数一般都是作为参数使用，其他地方一般不会使用
"""
# 输出：30
print((lambda a, b: a + b)(10, 20))

lst = [4, 5, 6]
r = filter(lambda i: i > 5, lst)
# 输出：[6]
print(list(r))

"""
1、map()
2、该函数可以对可跌倒对象中的所有元素做指定的操作，然后将其添加到一个新的对象中返回
"""
lst = [1, 2, 3, 4, 5]

r = map(lambda i: i * 2, lst)
# 输出:[2, 4, 6, 8, 10]
print(list(r))
