import json

data =[{'name':"张大仙","age":11},{"name":"王大锤","age":13},{"name":"赵小虎","age":16}]

json_str = json.dumps(data,ensure_ascii=False)
print(type(json_str))
print(json_str)

s = '[{"name":"张大仙","age":11},{"name":"王大锤","age":13},{"name":"赵小虎","age":16}]'

python_ = json.loads(s)
print(type(python_))
print(python_)