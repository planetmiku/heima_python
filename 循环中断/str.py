my_str = "python heima"
#replace 替换字符串
new_str_str = my_str.replace("hei","bai")
print(my_str,new_str_str)

#split 切割字符串，变为列表
my_str = "hello python heima itcast"
split_my_str = my_str.split(" ")
print(my_str)
print(split_my_str)

#strip 规整（去除前后字符串）
my_str = " hello python heima itcast "
new_str_str = my_str.strip()
print(my_str)
print(new_str_str)

my_str = "12hello python heima itcast21"
new_str_str = my_str.strip("12")
print(my_str)
print(new_str_str)

for i in my_str:
    print(i)

my_str = "itheima itcast boxuegu"
count = my_str.count("it")
print(count)
new_str_str = my_str.replace(" ","|")
print(new_str_str)
my_str_list = new_str_str.split("|")
print(my_str_list)