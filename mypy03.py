b = [1]

# 表示当前是否是空
if b:
    print("这是什么呢")
c = "False"

if c:
    print("表示C不为空")

# 三元条件运算符
a = 5
print("a是小于10的数据" if a < 10 else "a是小于10的数字")

while a > 0:
    print(a, end="\t")
    a -= 1

sun = 0
num = 0
while num <= 100:
    sun = sun + num
    num += 1

print("1-100的累加和：", sun)

for n in range(1, 10):
    for m in range(1, n + 1):
        print("{0}*{1}={2}".format(m, n, n * m), end="\t")
    print("")

# 字典
r1 = dict(name="高小一", age=18, salary=30000, city="北京")
r2 = dict(name="高小二", age=19, salary=10000, city="上海")
r3 = dict(name="高小三", age=20, salary=15000, city="重庆")
tb = [r1, r2, r3]  # 列表
for user in tb:
    for key in user.keys():
        print("key={0},value={1}".format(key, user[key]), end="\t")
    for value in user.values():
        print(value, end="\t")
    print()
    if user["salary"] >= 15000:
        print(user)
