#list 列表
my_list =['tom','jam','jerry']
print(my_list[-1])
my_list1=[[1,2,3],[4,5,6]]
print(my_list1[-1][-3])

#列表的方法
#index 查找下标
index = my_list.index('jam')
print(index)
#修改 =
print(my_list)
my_list[0]='cherry'
print(my_list)
#插入 insert
my_list.insert(1,'tom')
print(my_list)
#追加 append
my_list.append('pop')
print(my_list)
#批量追加 exppend
my_list2= [1,2,3]
my_list.extend(my_list2)
print(my_list)
#删除 del ,pop ,move,clear
#del list[]
my_list =['tom','jam','jerry']
del my_list[2]
print(my_list)
#pop list.pop()
my_list =['tom','jam','jerry']
pop = my_list.pop(2)
print(pop,  my_list)
#remove list.remove('xx'),删除符合条件的第一个元素
my_list =['tom','jam','jerry','jerry']
my_list.remove('jerry')
print(my_list)
#clear 清空
my_list.clear()
print(my_list)
#统计 count
my_list =['tom','jam','jerry','jerry']
count = my_list.count('jerry')
print(count)
#len 计算元素数量
length = len(my_list)
print(length)