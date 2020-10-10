# sort()和sorted()函数
"""
1、sort()该方法用来对列表中的元素进行排序。
2、sort()方法默认是直接比较列表中的元素的大小。
3、在sort()可以接收一个关键字参数 ， key
    key需要一个函数作为参数，当设置了函数作为参数，
    每次都会以列表中的一个元素作为参数来调用函数，
    并且使用函数的返回值来比较元素的大小。
4、会对原来的函数进行影响，在原来的基础上产生一个排序后的对象。
"""

lst = [2, 5, '1', 3, '6', '4']
# 按照int类型进行排序，首先将字符串转化为int类型
lst.sort(key=int)
# 输出：['1', 2, 3, '4', 5, '6']
print(lst)

"""
1、sorted()
2、该函数和sort()的用法基本一致，但是sorted()可以对任意的序列进行排序。
3、 并且使用sorted()排序不会影响原来的对象，而是返回一个新对象
"""
lst = [2, 5, '1', 3, '6', '4']

print('排序前:', lst)
# 输出：['1', 2, 3, '4', 5, '6']
print(sorted(lst, key=int))
print('排序后:', lst)