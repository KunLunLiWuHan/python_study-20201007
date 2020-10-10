# 文件的打开和关闭

# 创建一个变量，来保存文件的名字
# 如果目标文件和当前文件在同一级目录下，则直接使用文件名即可
file_name = 'demo.txt'

"""
1、路径1
使用 \\ 来代替 \或者也可以使用原始字符串,需要在前面加个 r 。
2、路径2-相对路径
表示路径，可以使用..来返回一级目录。
3、路径2-绝对路径
如果目标文件距离当前文件比较远，此时可以使用绝对路径，
 绝对路径应该从磁盘的根目录开始书写。
"""
# file_name = 'hello\\demo.txt'
# file_name = r'hello\demo.txt'
# file_name = '../hello/demo.txt'
# file_name = r'C:\Users\lilichao\Desktop\hello.txt'

file_obj = open(file_name)  # 打开 file_name 对应的文件
print(file_obj)

print("---------------文件关闭-----------------------------")
try:
    with open(file_name) as file_obj:
        print(file_obj.read())
except FileNotFoundError:
    print(f'{file_name} 文件不存在~~')
