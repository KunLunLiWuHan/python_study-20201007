# 列表的切片

stus = ['孙悟空', '猪八戒', '沙和尚', '唐僧']

# 输出：['猪八戒', '沙和尚', '唐僧']
print(stus[1:])
# 输出：['孙悟空', '猪八戒', '沙和尚']
print(stus[:3])
# 输出：['孙悟空', '猪八戒', '沙和尚', '唐僧']
print(stus[:])
# 输出：['孙悟空', '猪八戒', '沙和尚', '唐僧']
print(stus)
# 输出：['孙悟空', '沙和尚']
print(stus[::2])