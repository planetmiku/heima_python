import time

f = open('text.txt','r',encoding='UTF-8')
print(type(f))
#read 读取任意字节的数据
# print(f.read())

#readlines 读取所有数据，并将每行数据组合成一个列表
# print(f.readlines())

#readline 读取一行数据
#print(f.readline())

#for循环
# for line in f:
#     print(line)


# f.close()
#with open :
# with open("text.txt",'r',encoding="UTF-8") as f:
#     lines = f.readlines()
#     print(lines)

# with open("text.txt",'r',encoding='UTF-8') as f:
#     content = f.read()
#     count = content.count("itheima")
#     print(count)

with open("text.txt",'r',encoding='UTF-8') as f:
    count = 0
    for line in f:
        words = line.strip('\n').split(" ")
        print(words)
        count += words.count("itheima")
    print(count)