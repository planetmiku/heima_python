import random
from typing import Union

# var_1: int = 11
# var_2: str = "abc"
# var_3: bool = True
# class Student():
#     pass
# stu : Student = Student()
#
# my_list: list = [1,2,3]
# my_tuple: tuple = (1,2,3)
# my_dict: dict = {"pop":11}

my_list: list[int] = [1,2,3]
my_tuple: tuple[str,int,bool] = ('a',1,True)
my_dict: dict[str,int] = {"aaa":11}

var_1 = random.randint(1,10)   # type: int

#对函数注解
def add(x:int,y:int) -> int:
    return x + y
add(1,2)

def test(data:Union[list,dict]) -> Union[dict,str]:
    pass