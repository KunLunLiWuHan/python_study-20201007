# 操作二进制文件
file_name = 'c:/Users/lilichao/Desktop/告白气球.flac'

with open(file_name, 'rb') as file_obj:
    # 将读取到的内容写出来
    # 定义一个新的文件
    new_name = 'aa.flac'

    with open(new_name, 'wb') as new_obj:

        # 定义每次读取的大小
        chunk = 1024 * 100

        while True:
            # 从已有的对象中读取数据
            content = file_obj.read(chunk)

            # 内容读取完毕，终止循环
            if not content:
                break
            # 将读取到的数据写入到新对象中
            new_obj.write(content)
