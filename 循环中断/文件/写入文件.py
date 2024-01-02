# with open("text1.txt",'w',encoding='UTF-8') as f:
#     f.write('hello python')
#     f.flush()
#
# with open('text1.txt','a',encoding='UTF-8') as f:
#     f.write("\n222222")
#     f.flush()

with open('bill.txt','r',encoding='UTF-8') as f1:
    with open('bill.txt.back','w',encoding='UTF-8') as f2:
        for line in f1:
            if line.split(",")[-1]=="测试\n":
                continue
            f2.write(line)
