import random

money = 10000

for i in range(1,21):
    num = random.randint(1,10)
    if num <5 :
        print(f'{i}号绩效小于5，不发工资')
        continue
    money -= 1000
    print(f'{i}号绩效大于5，\n发放{i}号员工的工资,工资还剩余{money}')
    if money==0:
        print("工资已发放完毕")
        break