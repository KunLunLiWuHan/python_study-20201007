# 文件的写入

file_name = 'demo2.txt'
with open(file_name, 'w', encoding='utf-8') as file_obj:
    file_obj.write('aaa\n')
    r = file_obj.write(str(123) + '123123\n')
    print(r)  # 10
