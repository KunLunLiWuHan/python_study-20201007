# 多重继承
class A(object):
    def test(self):
        print('A中的test()方法..........')


class B(object):
    def test(self):
        print('B中的test()方法.........')


# C类继承A，B两个类
class C(A, B):
    pass


# 类名.__bases__ 这个属性可以用来获取当前类的所有父类
# 输出：(<class '__main__.A'>, <class '__main__.B'>)
print(C.__bases__)
# 输出：(<class 'object'>,)
print(B.__bases__)
