# 多态

class A:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


class B:
    def __init__(self, name):
        self._name = name

    def __len__(self):
        return 10

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


a = A('孙悟空')
b = B('猪八戒')

#
# 对于say_hello()这个函数来说，只要对象中含有name属性，它就可以作为参数传递
#   这个函数并不会考虑对象的类型，只要有name属性即可
"""
1、定义一个函数,对于该函数来说，只要对象中含有name属性，它就可以作为参数传递。
    这个函数并不会考虑对象的类型，只要有name属性即可。
"""


def say_hello(obj):
    print('你好 %s' % obj.name)


# 执行
# 输出：你好 孙悟空
say_hello(a)
# 输出：你好 猪八戒
say_hello(b)

print("---------------------------------------------")
# len()
# 之所以一个对象能通过len()来获取长度，是因为对象中具有一个特殊方法__len__
# 换句话说，只要对象中具有__len__特殊方法，就可以通过len()来获取它的长度
"""
1、之所以一个对象能通过len()来获取长度，是因为对象中具有一个特殊方法__len__。
   换句话说，只要对象中具有__len__特殊方法，就可以通过len()来获取它的长度。
"""
l = [1, 2, 3]
s = 'hello'

print(len(l))
print(len(s))
