# 命名空间

"""
1、locals()用来获取当前作用域的命名空间。
2、如果在全局作用域中调用locals()则获取全局命名空间，如果在函数作用域中调用locals()则获取函数命名空间
返回的是一个字典。
"""
scope = locals()  # 当前命名空间，也就是全局命名空间
# 输出：{'__name__': '__main__', '__doc__':
print(scope)


def fn():
    a = 10
    scope = locals()  # 在函数内部调用locals()会获取到函数的命名空间
    # 输出：{'a': 10}
    print(scope)
    # scope['b'] = 20 # 可以通过scope来操作函数的命名空间，但是不建议这么做

    # globals() 函数可以用来在任意位置获取全局命名空间
    global_scope = globals()
    # 输出：{'__name__': '__main__', '__doc__':
    print(global_scope)
    # print(global_scope['a']) # 报错：KeyError: 'a'
    # global_scope['a'] = 30
    # print(global_scope['a'])# 可以执行


fn()
