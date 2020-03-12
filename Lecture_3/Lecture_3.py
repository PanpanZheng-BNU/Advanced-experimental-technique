# import zone
import numpy as np
# create a 1-100 mArr variable
mArr = np.array(range(1,101))
# calculate
s = np.sum(mArr)
print(s)


# sum 1-100 in for
c = 0
for x in range(1,101):
    c = x + c
print(c)


c1 = 0
for x in range(1,101):
    if x % 2 == 1:
        c1 = c1 + x
print(c1)


mScore = int(input("请输入考试成绩："))
if mScore >= 60:
    print('告诉学生，考试居然及格了！')
else:
    print('告诉学生，考试居然没及格！')


holiday_name = input('请输入今天什么节日？')
if holiday_name == '情人节':
    print('送玫瑰')
    print('看电影')
elif holiday_name == '生日':
    print('送口红')
    print('吃蛋糕')
else:
    print('送牛奶')


from numpy import *
c = array(range(1,11))
c = mean(c)
print(c)

sum_odd = 0
sum_even = 0
for i in range(1,101):
    if i%2 != 0:
        sum_odd += i
    else:
        sum_even += i
print(sum_odd,sum_even)


# 列表推导式
[type(item) for item in [True,1,"2",3.14]]

c = []
for item in [True,1,"2",3.14]:
    c.append(type(item))
c


numbers = [12,37,5,42,8,3]
even = []
odd = []
while len(numbers) > 0:
    number = numbers.pop()
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)
print(even,odd)


num = 0
scores = 0
while True:
    s = input("请输入学生成绩(输入Q或q结束)：")
    if s == 'q' or s== 'Q':
        break
    if eval(s) < 0:
        print("成绩应大于零，请重新输入！")
        continue
    num += 1
    scores += eval(s)
print("学生人数为{}，平均成绩为{}".format(num,scores/num))
