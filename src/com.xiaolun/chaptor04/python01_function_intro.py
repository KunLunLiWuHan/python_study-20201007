# 函数介绍

"""
1、定义一个函数
    fn是函数对象  fn()调用函数。
2、定义函数时指定形参a,b。
"""


def fn(a, b):
    print(a, "+", b, "=", a + b)


#
#
"""
1、调用函数时，来传递实参
2、实参的传递方式
        位置参数就是将对应位置的实参复制给对应位置的形参，
        第一个实参赋值给第一个形参，第二个实参赋值给第二个形参。
3、输出：输出：10 + 20 = 30
4、函数在调用时，解析器不会检查实参的类型。
"""
fn(10, 20)

"""
1、定义函数时，可以为形参指定默认值。
指定了默认值以后，如果用户传递了参数则默认值没有任何作用；
如果用户没有传递，则默认值就会生效。
"""


def fn2(a, b=20):
    print('a =', a)
    print('b =', b)


"""
输出：
a = 1
b = 20
"""
fn2(1)
