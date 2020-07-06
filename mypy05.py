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

# 可使用两个循环
cells = [(row, col) for row in range(10) for col in range(10)]
print(cells)

# 字典推导式

# 字典推导式
# 将key value 反转
dict1 = {"name": "howhy", "age": 12, "gender": "man"}
ret = {v: k for k, v in dict1.items()}
print(type(ret))
print(ret)


# 生成 集合
ret = {k for k, v in dict1.items()}
print(ret)
print(type(ret))


# 统计每个字符出现的次数
my_text = "i love you ,i love sxt , i love wangye"
char_count = {c: my_text.count(c) for c in my_text}
sorted(char_count)
print(char_count)
char_count = dict()
for c in my_text:
    char_count[c] = my_text.count(c)
print(char_count)

# 生成器推导式（生成元组）

# 生成器，可迭代对象,只可用一次
gnt = (x for x in range(1, 100) if x % 9 == 0)
print(type(gnt))
print(gnt)
# gnt = tuple(gnt)
print(gnt)
print(type(gnt))
for x in gnt:
    print(x, end=" ")

print()

for x in gnt:
    print(x, end="-")

print()

for x in gnt:
    print(x, end="-")
