# 文件的读取
import pprint

file_name = 'demo.txt'
try:  # 指定字符编码
    with open(file_name, encoding='utf-8') as file_obj:
        content = file_obj.read(6)
        print(content)  # hello
        print(len(content))  # 6
except FileNotFoundError:
    print(f'{file_name} 这个文件不存在！')

print("-----------------------------------")
# 读取大文件的方式
file_name = 'demo.txt'
try:
    with open(file_name, encoding='utf-8') as file_obj:
        # 定义一个变量，来保存文件的内容
        file_content = ''
        # 定义一个变量，来指定每次读取的大小
        chunk = 100
        # 创建一个循环来读取文件内容
        while True:
            # 读取chunk大小的内容
            content = file_obj.read(chunk)

            # 检查是否读取到了内容，如果是空串，会自动变成False。
            if not content:
                # 内容读取完毕，退出循环
                break

            # 输出内容，将空串换行改变。
            print(content, end='')
            file_content += content

except FileNotFoundError:
    print(f'{file_name} 这个文件不存在！')

print("-----------------一行一行读取------------------")
file_name = 'demo.txt'

with open(file_name, encoding='utf-8') as file_obj:
    # readline()
    # 该方法可以用来读取一行内容
    # print(file_obj.readline(), end='')

    # readlines()
    # 该方法用于一行一行的读取内容，它会一次性将读取到的内容封装到一个列表中返回
    r = file_obj.readlines()
    pprint.pprint(r[0])

    for t in file_obj:
        print(t)
