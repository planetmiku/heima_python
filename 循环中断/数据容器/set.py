my_set = {"川川","秘密","漳州","川川"}
print(my_set)
#add 添加元素
my_set.add("海外")
print(my_set)
#remove 移除元素
my_set.remove("秘密")
print(my_set)
#pop 随机取出一个元素，并删除原集合中的该元素
set1 = my_set.pop()
print(set1,my_set)
#clear 清空集合
my_set.clear()
print(my_set)
#set1.difference(set2),取集合1有而且集合2的元素集合,集合1、2不变
set1 = {1,2,3,7}
set2 = {1,3,5,4}
set3 = set1.difference(set2)
print(set3)
#set1.difference_update(set2),在集合1内，删除和集合2相同的元素，集合1修改，集合2不变
set1.difference_update(set2)
print(set1)
#set1.union(set2),集合1和集合2的合集，集合1、2不改变
set3 = set1.union(set2)
print(set3)
#len()
#遍历
for i in set3:
    print(i)

my_set = set()
my_list=["黑马程序员","传智播客","黑马程序员","传智播客","itheima","itcast","itheima","itcast","cast"]
for i in my_list:
    my_set.add(i)
for i in my_set:
    print(i)