def str_reverse(s):
    '''
    反转字符串
    :param s: 原来的字符串
    :return: 反转后的字符串
    '''
    return s[::-1]


def substr(s,x,y):
    '''
    对字符串进行切片
    :param s: 传入字符串
    :param x: 切片起始下标
    :param y: 切片终止下标
    :return: 切片后字符串
    '''
    sub_s = s[x:y]
    return sub_s

if __name__ == '__main__':
    s='红红火火'
    print(str_reverse(s))
    print( substr(s,1,3))