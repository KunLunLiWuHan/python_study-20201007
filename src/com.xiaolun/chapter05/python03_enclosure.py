# 封装

"""
1、使用__开头的属性，实际上依然可以在外部访问，所以这种方式我们一般不用，
一般我们会将一些私有属性（不希望被外部访问的属性）以_开头，
一般情况下，使用_开头的属性都是私有属性，没有特殊需要不要修改私有属性。
"""


class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name


p = Person('孙悟空')
# 输出：孙悟空
print(p.get_name())
p.set_name("猪八戒")
# 输出：猪八戒
print(p.get_name())