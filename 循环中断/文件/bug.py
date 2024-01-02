# try:
#     f = open('text3.txt','r',encoding='UTF-8')
#     f.close()
# except:
#     f = open('text3.txt','w',encoding='UTF-8')
#     f.close()

# try:
#     print(name)
# except NameError as e:
#     print("变量未定义")
#     print(e)

# try:
#     f = open('text3.txt','r',encoding='UTF-8')
# except Exception as e:
#     f = open('text3.txt','w',encoding='UTF-8')
# else:
#     print('很好,没有异常')
# finally:
#     print('这是finally')
#     f.close()

def func1():
    print('fun1开始')
    num = 2 / 0
    print('fun1结束')

def func2():
    print('fun2开始')
    func1()
    print('fun2结束')

def main():
    try:
        func2()
    except Exception as e:
        print(e)

main()