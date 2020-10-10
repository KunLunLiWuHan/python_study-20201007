# 特殊方法
# 定义一个Person类
class Person():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # __str__（）这个特殊方法会在尝试将对象转换为字符串的时候调用
    # 它的作用可以用来指定对象转换为字符串的结果  （print函数）
    def __str__(self):
        return '__str__输出：Person [name=%s , age=%d]' % (self.name, self.age)

    # __repr__()这个特殊方法会在对当前对象使用repr()函数时调用
    # 它的作用是指定对象在 ‘交互模式’中直接输出的效果
    def __repr__(self):
        return 'Hello'


# __str__（）测试
# 创建一个Person类的实例
p1 = Person('孙悟空', 18)
"""
1、当我们打印一个对象时，实际上打印的是对象的中特殊方法 __str__()的返回值。
2、控制台输出：__str__输出：Person [name=孙悟空 , age=18]
"""
print(p1)

# __repr__()测试
print(repr(p1))
