while True:
    a = input("请输入一个字符，q 或Q 时退出")
    if a == "q" or a == "Q":   #a.upper() == "Q"
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
