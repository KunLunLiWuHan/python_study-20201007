# 预引入的模块

# 定义的变量
a = 10
b = 2


# 定义的函数
def fn():
    print('Hello fn')


def fn2():
    print('Hello fn2')


def fn3():
    print('Hello fn3')
    5 / 0


# 编写测试代码，这部分代码，只要当当前文件作为主模块的时候才需要执行；
# 而当模块被其他模块引入时，不需要执行的，此时我们就必须要检查当前模块是否是主模块。
if __name__ == '__main__':
    fn()
