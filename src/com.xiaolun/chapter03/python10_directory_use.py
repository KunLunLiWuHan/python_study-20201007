# 字典的使用
d = dict(name='孙悟空', age=18, gender='男')

# len() 获取字典中键值对的个数
# 输出：3
print(len(d))

"""
in 检查字典中是否包含指定的键
not in 检查字典中是否不包含指定的键
"""
# 输出：False
print('hello' in d)

print("----------------------------------------")
"""
1、需要根据键来获取值
2、语法
    d[key]
"""
d = dict(name='孙悟空', age=18, gender='男')
# 输出：孙悟空 18 男
print(d['name'], d['age'], d['gender'])
# 如果使用了字典中不存在的键，会报错:KeyError: 'hello'
# print(d['hello'])

"""
1、get(key[, default]) 该方法用来根据键来获取字典中的值。
    如果获取的键在字典中不存在，会返回None；
    也可以指定一个默认值，来作为第二个参数，这样获取不到值时将会返回默认值。
"""
# 输出：孙悟空
print(d.get('name'))
# 输出：默认值
print(d.get('hello', '默认值'))

"""
1、修改字典
    d[key] = value 
    如果key存在则覆盖，不存在则添加。
"""
d['name'] = 'sunwukong'
# 输出：{'name': 'sunwukong', 'age': 18, 'gender': '男'}
print(d)

"""
1、setdefault(key[, default]) 
    向字典中添加key-value，
    如果key已经存在于字典中，则返回key的值，不会对字典做任何操作，
    如果key不存在，则向字典中添加这个key，并设置value。
"""
result = d.setdefault('name', '猪八戒')
# 输出：sunwukong
print(result)

"""
1、update([other])
    将其他的字典中的key-value添加到当前字典中，
    如果有重复的key，则后边的会替换到当前的。
"""
d = {'a': 1, 'b': 2}
d2 = {'d': 4, 'e': 5}
d.update(d2)
# 输出：{'a': 1, 'b': 2, 'd': 4, 'e': 5}
print(d)

# 删除，可以使用 del 来删除字典中的 key-value
del d['a']

"""
1、pop(key[, default])
    根据key删除字典中的key-value，会将被删除的value返回。
    如果删除不存在的key，会抛出异常；如果指定了默认值，
    再删除不存在的key时，不会报错，而是直接返回默认值
"""
d = {'a': 1, 'b': 2}
result = d.pop('z', '这是默认值')
# 输出：这是默认值
print(result)

# clear()用来清空字典
d.clear()

"""
1、copy()
用于对字典进行浅复制，复制以后的对象，和原对象是独立，修改一个不会影响另一个；
浅复制会简单复制对象内部的值。
"""
d = {'a': 1, 'b': 2}
d2 = d.copy()
# 输出：{'a': 1, 'b': 2}
print(d2)

# 报错：AttributeError: 'str' object has no attribute 'copy'
d = "str"
d2 = d.copy()
print(d2)
