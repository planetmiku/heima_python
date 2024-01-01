my_dict = {"王力宏":99,"周杰伦":88,"林俊杰":77}

my_dict2 = {}

my_dict3 = dict()

print(my_dict,type(my_dict))
print(my_dict2,type(my_dict2))
print(my_dict3,type(my_dict3))

print(my_dict["王力宏"])
print(my_dict["周杰伦"])
print(my_dict["林俊杰"])

stu_score_dict = {
    "王力宏":{
        "语文":77,
        "数学":66,
        "英语":33,
    }, "周杰伦":{
        "语文":88,
        "数学":86,
        "英语":55
    },"林俊杰":{
        "语文":99,
        "数学":96,
        "英语":66
    }
}
print(stu_score_dict["王力宏"]["英语"])

#pop 删除元素
store = stu_score_dict.pop("周杰伦")
print(stu_score_dict)
print(store)

#clear 清空
stu_score_dict.clear()
print(stu_score_dict)

#keys 获取所有key
keys = my_dict.keys()
print(keys)
#遍历 方式1 keys方法
for i in keys:
    print(i)
    print(my_dict[i])
#方式2
for key in my_dict:
    print(key)
    print(my_dict[key])

dict = {
    "王力宏":{
        "部门":"科技部",
        "工资":3000,
        "级别":1
    },"周杰伦":{
        "部门":"市场部",
        "工资":5000,
        "级别":2
    },"林俊杰":{
        "部门":"市场部",
        "工资":7000,
        "级别":3
    },"张学友":{
        "部门":"科技部",
        "工资":4000,
        "级别":1
    },"刘德华":{
        "部门":"市场部",
        "工资":6000,
        "级别":2
    },
}

for key in dict:
    if dict[key]["级别"]==1:
        dict[key]["工资"]+=1000
        dict[key]["级别"]+=1

print(dict)