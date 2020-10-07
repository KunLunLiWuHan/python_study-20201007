# break和continue语句

"""
控制台输出：
1
2
"""
i = 1
while i <= 5:
    if i == 3:
        break
    print(i)
    i += 1
else:
    print('循环结束')

"""
输出：
2
4
5
6
循环结束
"""
i = 1
while i <= 5:
    # i自增放到这里，才可以在i==3成立的时候，继续增加，进而跳出循环
    i += 1
    if i == 3:
        continue
    print(i)
else:
    print('循环结束')

i = 0
if i < 5:
    # 这里的功能还没想好，只是简单的在这里保证程序的正常执行而已。
    pass
