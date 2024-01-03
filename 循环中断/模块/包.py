# from my_package import my_module1
# from my_package import my_module2
#
# my_module1.test(1,2)
#
# my_module2.test1(3,1)

# from my_package import *
# my_module1.test(1,2)
# my_module2.test1(2,1)

from my_utils import str_util,file_util

s='abc'
print(str_util.str_reverse(s))
print(str_util.substr(s,1,2))

file_name = 'text.txt'
data = '翻译是把一种语言信息转变成另一种语言信息的行为。翻译是将一种相对陌生的表达方式，转换成相对熟悉的表达方式的过程。其内容有语言、文字、图形、符号和视频翻译。'

file_util.print_file_info(file_name)
# file_util.append_to_file(file_name,data)