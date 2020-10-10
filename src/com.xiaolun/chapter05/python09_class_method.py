# 类中的属性和方法
class A(object):

    # 类属性
    count = 0

    def __init__(self):
        # 实例属性
        self.name = '孙悟空'

    # 实例方法
    def test(self):
        print('这是test方法~~~ ', self)

    # 类方法
    @classmethod
    def test_2(cls):
        print('这是test_2方法，他是一个类方法~~~ ', cls)
        print(cls.count)

    # 静态方法
    @staticmethod
    def test_3():
        print('test_3执行了~~~')


a = A()
# 实例属性，通过实例对象添加的属性属于实例属性
a.count = 10
# 输出：A , 0
print('A ,', A.count)
# 输出：A , 10
print('a ,', a.count)

# 等价于 A.test(a)
a.test()
# 等价于 a.test_2()
A.test_2()

# 静态方法的调用
A.test_3()
a.test_3()
