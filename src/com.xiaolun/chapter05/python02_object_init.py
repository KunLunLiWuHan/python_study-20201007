# 对象的初始化
class Person:

    # init会在对象创建以后离开执行
    # init可以用来向新创建的对象中初始化属性
    # 调用类创建对象时，类后边的所有参数都会依次传递到init()中
    def __init__(self, name):
        # 通过self向新建的对象中初始化属性
        self.name = name

    def say_hello(self):
        print('大家好，我是%s' % self.name)


"""
1、目前来讲，对于Person类来说name是必须的，并且每一个对象中的name属性基本上都是不同，
而我们现在是将name属性在定义为对象以后，手动添加到对象中，这种方式很容易出现错误。
2、我们希望，在创建对象时，必须设置name属性，如果不设置对象将无法创建，
并且属性的创建应该是自动完成的，而不是在创建对象以后手动完成。
"""
# 创建对象时为对象赋属性
p1 = Person('孙悟空')
p1.say_hello()
