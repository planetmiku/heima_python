money = 50000
def query(show_header):
    if show_header:
        print('--------查询余额--------')
    print(f'你好，你的余额为{money}')

def saving():
    print('--------存款--------')
    global money
    n = int(input('请输入存款金额：'))
    money +=n
    print(f"你好，存款{n}元成功")
    query(False)

def get_money():
    print('--------取款--------')
    global money
    n = int(input('请输入取款金额：'))
    if money >= n:
        money -=n
        print(f"你好，取款{n}元成功")
    else:
        print(f"你好，取款{n}元失败")
    query(False)


def exit():
    print("欢迎下次使用")





def main():
    print("--------主菜单--------")
    print('你好，欢迎来到银行，请操作')
    print('''查询余额   [请输入1]
存款      [请输入2]
取款      [请输入3]
退出      [请输入4]''')
    return input("请输入你的选择:")


while True:
    keyword_input=main()
    if keyword_input=="1":
        query(True)
        continue
    elif keyword_input=="2":
        saving()
        continue
    elif keyword_input=="3":
        get_money()
        continue
    else :
        print("下次光临")
        break