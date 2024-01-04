import json
from pyecharts.charts import Map
from pyecharts.options import *
map = Map()

with open('疫情.txt','r',encoding='UTF-8') as f:
    data = f.read()
    data = json.loads(data)
data = json.loads(data)
data = data['areaTree'][0]['children']

data_list = []
for province_data in data:
    name = province_data['name']
    confirm = province_data['total']['confirm']
    data_list.append((name,confirm))
for i in data_list:
    print(i)

map = Map()
map.add("各省份确诊人数",data_list,"china")

map.set_global_opts(
    title_opts=TitleOpts(title='全国疫情地图',pos_left='center',pos_bottom='1%'),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min":1,"max":499,"lable":"1-499人","color":'#CCFFFF'},
            {"min":500,"max":999,"lable":"500-999人","color":'#FFFF99'},
            {"min":1000,"max":1499,"lable":"1000-1499人","color":'#FF9966'},
            {"min":1500,"max":1999,"lable":"1500-1999人","color":'#FF6666'},
            {"min":2000,"max":2499,"lable":"2000-2499人","color":'#CC3333'},
            {"min":2500,"max":2999,"lable":"2500-2999人","color":'#990033'},
            {"min":3000,"lable":">3000人","color":'#6b0124'}
        ]
    )
)
map.render(path='china_map.html')