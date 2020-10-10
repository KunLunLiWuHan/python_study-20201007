# 封装 使用注解

class Person:
    def __init__(self, name):
        self._name = name

    # property装饰器，用来将一个get方法，转换为对象的属性
    # 添加为property装饰器以后，我们就可以像调用属性一样使用get方法
    # 使用property装饰的方法，必须和属性名是一样的
    @property
    def name(self):
        print('get方法执行了~~~')
        return self._name

    # setter方法的装饰器：@属性名.setter
    @name.setter
    def name(self, name):
        print('setter方法调用了')
        self._name = name


p = Person('猪八戒')
# 使用的是setter方法
p.name = '孙悟空'
# 使用的是注解方法
print(p.name)
