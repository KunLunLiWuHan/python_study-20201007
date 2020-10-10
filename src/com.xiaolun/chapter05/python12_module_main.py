# 模块化
import module_assistant
# 为模块指定别名
import module_assistant as m

"""
输出结果如下：
__main__
10 2
Hello fn2
"""
print(__name__)
print(m.a, m.b)
m.fn2()

# 输出：10 2
print(module_assistant.a, module_assistant.b)