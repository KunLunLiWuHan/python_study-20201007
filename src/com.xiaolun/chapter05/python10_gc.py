# 垃圾回收
class A:
    def __init__(self):
        self.name = 'A类'

    # del是一个特殊方法，它会在对象被垃圾回收前调用
    def __del__(self):
        print('A()对象被删除了，', self)


a = A()
"""
1、将a设置为了None，此时没有任何的变量对A()对象进行引用，它就是变成了垃圾。
2、此时在程序运行过程中将会输出：A()对象被删除了， <__main__.A object at 0x000001A8A291B3C8>
"""
a = None
"""
1、在上面的基础上，我们又使用一个变量b，来引用a对应的对象（此时注释：a = None）。
    此时，a对象不会被gc删除
"""
b = a
input('回车键退出...')
