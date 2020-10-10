# 文件的其他操作
import os
from pprint import pprint

r = os.listdir()
pprint(r)
r = os.getcwd()
# 输出：'D:\\03Enviroment\\02IDEA\\02Code\\Python-study-20201006\\src\\com.xiaolun\\chapter06'
pprint(r)
# os.chdir() 切换当前所在的目录 作用相当于 cd
os.chdir('c:/')

# 创建目录
# os.mkdir("aaa") # 在当前目录下创建一个名字为 aaa 的目录

# 删除目录
# os.rmdir('abc')

# 删除文件
# os.remove('aa.txt')

# os.rename('旧名字','新名字') 可以对一个文件进行重命名，也可以用来移动一个文件
# os.rename('aa.txt','bb.txt')
# os.rename('bb.txt', 'c:/users/lilichao/desktop/bb.txt')

# pprint(r)
