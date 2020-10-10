# 继承 super
class Animal:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


# 父类中的所有方法都会被子类继承，包括特殊方法（__init__），也可以重写特殊方法
class Dog(Animal):
    def __init__(self, name, age):
        """
        1、super() 可以用来获取当前类的父类，然后直接调用父类的__init__方法
            来初始化父类中定义的属性。
            并且通过super()返回对象调用父类方法时，不需要传递self
        """
        super().__init__(name)
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age


d = Dog('旺财', 18)
print(d.name)  # 旺财
print(d.age)  # 18
