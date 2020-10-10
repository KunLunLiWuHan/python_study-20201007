# 继承
# 定义一个类 Animal（动物）
#   这个类中需要两个方法：run() sleep()
class Animal:
    def run(self):
        print('动物会跑~~~')

    def sleep(self):
        print('动物睡觉~~~')


# 子类继承父类
class Dog(Animal):
    def bark(self):
        print('汪汪汪~~~')

    """
    1、override
    如果在子类中如果有和父类同名的方法，则通过子类实例去调用方法时，
    会调用子类的方法而不是父类的方法，这个特点我们成为叫做方法的重写。
    """

    def run(self):
        print('狗跑~~~~')


d = Dog()
# 使用子类自己的方式，输出：狗跑~~~~
d.run()
# 输出：汪汪汪~~~
d.bark()

"""
1、issubclass() 
该函数用来检查一个类是否是另一个类的子类。
"""
# 输出：True
print(issubclass(Dog, Animal))

"""
1、isinstance()
该函数用来检查一个对象是否是一个类的实例。
如果这个类是这个对象的父类，也会返回True
"""
# 输出：True
print(isinstance(d, Dog))
