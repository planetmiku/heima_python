# * 只能导入__all__变量的方法
__all__=['test']

def test(a,b):
    print(a+b)


def test1(a,b):
    print(a-b)


if __name__=='__main__':
    test(1,3)
