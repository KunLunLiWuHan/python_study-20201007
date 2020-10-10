# 装饰器

# 我们希望在不修改原函数的情况下，来对函数进行扩展
"""
1、 old 要扩展的函数对象。begin_end 装饰器
2、作用：用来对其他函数进行扩展，使其他函数可以在执行前打印开始执行，
执行后打印执行结束。
"""


def begin_end(old):
    # 创建一个新函数
    def new_function(*args, **kwargs):
        print('开始执行~~~~')
        # 调用被扩展的函数
        result = old(*args, **kwargs)
        print('执行结束~~~~')
        # 返回函数的执行结果
        return result

    # 返回新函数
    return new_function

@begin_end
def say_hello():
    print('使用say_hello~方法')


"""
输出： 
    开始执行~~~~
    使用say_hello~方法
    执行结束~~~~
"""
say_hello()
