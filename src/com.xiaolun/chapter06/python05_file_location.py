# 读取文件的位置

with open('demo.txt', 'rb') as file_obj:
    print(file_obj.read(100))  # 指定读取100个字符

    # seek() 可以修改当前读取的位置
    file_obj.seek(55)
    file_obj.seek(80, 0)
    file_obj.seek(-10, 2)
    # 输出：b'llo world.'，b指代二进制
    print(file_obj.read())
    # tell()报告位置，报告指针现在读到了那里，输出：当前读取到了 --> 12
    print('当前读取到了 -->', file_obj.tell())
