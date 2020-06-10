# 推导式创建

# 列表 [表达式  for  item in  可迭代对象]
a = [x for x in range(1, 5)]
print(a)

a = [x * 2 for x in range(5, 1, -1)]
print(a)

a = [x * 2 for x in range(1, 20) if x % 2 == 0]
print(a)
a = []
for x in range(1, 20):
    if x % 2 == 0:
        a.append(x * 2)
print(a)

cells = [(row, col) for row in range(10) for col in range(10)]
print(cells)

# 字典推导式

# 统计每个字符出现的次数
my_text = "i love you ,i love sxt , i love wangye"
char_count = {c: my_text.count(c) for c in my_text}
sorted(char_count)
print(char_count)
char_count = dict()
for c in my_text:
    char_count[c] = my_text.count(c)
print(char_count)

