import json
from pyecharts.charts import Map
from pyecharts.options import *
with open('疫情.txt','r',encoding='UTF-8') as f:
    data = f.read()

data = json.loads(data)
henan_data = data['areaTree'][0]['children'][3]['children']
henan_list = []
for city in henan_data:
    city_name = city['name'] + "市"
    city_confirm = city['total']['confirm']
    henan_list.append((city_name,city_confirm))
henan_list.append(('济源市',5))

map = Map()
map.add("河南省确诊人数",henan_list,"河南")
map.set_global_opts(
    title_opts=TitleOpts(title="河南省确诊地图",pos_left='center',pos_bottom='1%'),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min":1,"max":49,"lable":"1-499人","color":'#CCFFFF'},
            {"min":50,"max":99,"lable":"500-999人","color":'#FFFF99'},
            {"min":100,"max":149,"lable":"1000-1499人","color":'#FF9966'},
            {"min":150,"max":199,"lable":"1500-1999人","color":'#FF6666'},
            {"min":200,"max":249,"lable":"2000-2499人","color":'#CC3333'},
            {"min":250,"max":299,"lable":"2500-2999人","color":'#990033'},
            {"min":300,"lable":">3000人","color":'#6b0124'}
        ]
    )
)
map.render(path='henan_map.html')