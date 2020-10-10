# python标准库
import os
import pprint
import sys

# sys.argv
# 获取执行代码时，命令行中所包含的参数
# 该属性是一个列表，列表中保存了当前命令的所有参数
# print(sys.argv)

# sys.modules
# 获取当前程序中引入的所有模块
# modules是一个字典，字典的key是模块的名字，字典的value是模块对象
# pprint.pprint(sys.modules)

# sys.path
# 他是一个列表，列表中保存的是模块的搜索路径
pprint.pprint(sys.path)

# 控制台输出:win32
print(sys.platform)

# os.environ
# 通过这个属性可以获取到系统的环境变量
pprint.pprint(os.environ['path'])

# 可以用来执行操作系统的名字
print("-----------------------")
os.system('dir')
