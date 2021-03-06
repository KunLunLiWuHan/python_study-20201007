# 集合

# 集合的创建
s = set()
# 输出：set()
print(s)
s = set('hello')
# 输出：{'o', 'l', 'e', 'h'}
print(s)
s = set([1, 2, 3, 4, 5])
print(s)
# 使用set()将字典转换为集合时，只会包含字典中的键
# 输出：{1, 2, 3, 4, 5}
s = set({'a': 1, 'b': 2, 'c': 3})
# 输出：{'a', 'b', 'c'}
print(s)

# 使用in和not in来检查集合中的元素
print('c' in s)

# 使用len()来获取集合中元素的数量
print(len(s))

# add() 向集合中添加元素
s.add(10)
# 输出：{'a', 'c', 10, 'b'}
print(s)


"""
1、update() 
    将一个集合中的元素添加到当前集合中，
    update()可以传递序列或字典作为参数，字典只会使用键。
"""
s2 = set('hello')
s.update(s2)
# 输出：{10, 'e', 'c', 'b', 'l', 'h', 'o', 'a'}
# 将 'hello' 字符串分成字符后插入
print(s)

s = set([1, 2, 3, 4, 5])
# remove()删除集合中的指定元素
s.remove(1)
print(s)

# clear()清空集合
s.clear()