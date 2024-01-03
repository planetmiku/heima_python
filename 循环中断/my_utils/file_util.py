def print_file_info(file_name):
    f = None
    try:
        f = open(file_name,'r',encoding='UTF-8')
        print(f.read())
    except Exception as e:
        print(e)
    finally:
        if f:
         f.close()


def append_to_file(file_name,data):
    f = open(file_name,'a',encoding='UTF-8')
    f.write(data)
    f.write('\n')
    f.close()

if __name__ == '__main__':
    # print_file_info('D:/code/heima/循环中断/文件/txxx.txt')
    append_to_file('D:/code/heima/循环中断/模块/text.txt','测试代码')