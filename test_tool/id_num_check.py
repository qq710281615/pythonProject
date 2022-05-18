# 递归
str_id = "62402819961016041"
# str_id = input("请输入身份证的前17位：")
Ai = [int(i) for i in str_id]
Wi = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
l = sum(list(map(lambda a: a[0]*a[1], list(zip(Ai, Wi))))) % 11
last_list = [1, 0, "X", 9, 8, 7, 6, 5, 4, 3, 2]
print(last_list[l])
sumNum = 0
for i in range(len(str_id)):
    sumNum = sumNum + Ai[i]*Wi[i]
print("最后一位是:", last_list[sumNum % 11])
print("身份证是:", str_id + str(last_list[sumNum % 11]))
