# 列表通用操作

# 列表的拼接和乘法
my_list = [1, 2, 3] + [4, 5, 6]
# 输出：[1, 2, 3, 4, 5, 6]
print(my_list)
my_list = [1, 2, 3] * 2
# 输出：[1, 2, 3, 1, 2, 3]
print(my_list)

# in的用法
stus = ['孙悟空', '猪八戒', '沙和尚', '唐僧']
# 输出：True
print('牛魔王' not in stus)
print('牛魔王' in stus)

arr = [10, 1, 2, 5, 100, 77]
# 输出：1 100
print(min(arr), max(arr))

"""
1、index表示获取指定元素在列表中的第一次出现时索引。
index()的第二个参数，表示查找的起始位置， 
第三个参数，表示查找的结束位置。
2、如果要获取列表中没有的元素，会抛出异常。
"""
# 输出:2
print(stus.index('沙和尚'))
# 抛出异常：ValueError: '牛魔王' is not in list
# print(stus.index('牛魔王'))

# s.count() 统计指定元素在列表中出现的次数
# 输出：1
print(stus.count('沙和尚'))
