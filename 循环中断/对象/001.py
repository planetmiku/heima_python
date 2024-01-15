class Student:
    def __init__(self):
        i=1
        self.list = []
        while i < 2:
            print(f"当前录入第{i}位学生信息,总共需录入10位学生信息")
            self.name = input("请输入学生姓名")
            self.age = int(input("请输入学生年龄"))
            self.tel = input("请输入学生地址")
            print(f'学生{i}信息录入完成,信息为:【学生姓名：{self.name},年龄：{self.age}，地址：{self.tel}】')
            self.list.append([self.name,self.age,self.tel])
            i+=1
    # def __str__(self):
    #     return f'第一个学生的姓名是：{self.list[0][0]}'

stus = Student()
# print(stus)
# print(str(stus))
# class Man:
#     def __init__(self,age):
#         self.age = age
#
#     def __lt__(self, other):
#         return self.age < other.age
#
# man1 = Man(22)
# man2 = Man(15)
# print(man1 < man2)
# print(man1 > man2)