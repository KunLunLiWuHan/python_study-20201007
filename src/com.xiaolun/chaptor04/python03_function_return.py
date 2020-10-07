# 函数的返回值

"""
1、可以通过 return 来指定函数的返回值，也可以通过一个变量来接收函数的返回值。
2、return 后边跟什么值，函数就会返回什么值，
return 后边可以跟任意的对象，返回值甚至可以是一个函数。
3、return后的代码都不会执行，return 一旦执行函数自动结束。
"""


# 如果仅仅写一个return 或者 不写return，则相当于return None
def fn():
    a = 10
    return


# 这个函数的执行结果就是它的返回值
result = fn()
# 输出：None
print(result)
