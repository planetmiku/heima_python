def user_info(name,age,gender='男'):
    print(f'名字是{name},年龄是{age}。性别是{gender}')

user_info("小明",15,"男")
user_info(age=16,gender="女",name="小红")
user_info("小军",gender="男",age=18)
user_info("小李",18)
def user(*args):
    print(type(args),args)

user(1,2,3,4,"tom","I")

def user(**kwargs):
    print(type(kwargs),kwargs)

user(name='小钱',age="17",gender="男")

def test(compute):
    result = compute(1,2)
    print(result)

def compute(x,y):
    return x+y
test(compute)
test(lambda x,y:x+y)