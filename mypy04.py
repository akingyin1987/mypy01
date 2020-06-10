while True:
    a = input("请输入一个字符，q 或Q 时退出")
    if a == "q" or a == "Q":  # a.upper() == "Q"
        print("循环结束")
        break
    else:
        print("请继续输入")

#  else 语句 及语句未被打断退出者会执行
sun = 0
for i in range(4):
    s = input("请输入")
    if s.upper() == "Q":
        break
    sun = sun + int(s)
else:
    print("正常输入4次执行else 语句")
print("总数：{0}".format(sun))

# 通过zip() 并行迭代

names = ("1", "2", "3", "4")
ages = (10, 20, 30, 40, 50)
jobs = ("100", "200", "300", "400", "500")


# zip()在最短的序列完成后结束
for age, name, job in zip(names, ages, jobs):
    print("name={0},age={1},job={2}".format(name, age, job))

for i in range(4):
    print("name={0},age={1},job={2}".format(names[i], ages[i], jobs[i]))

