import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts,LabelOpts

def setdata(filename,str):
    with open(filename,'r',encoding='UTF-8') as f:
        content = f.read()
        content = content.replace(str,'')[:-2]
        dict = json.loads(content)

        trend_data = dict['data'][0]['trend']

        x_data = trend_data['updateDate'][:314]
        y_data = trend_data['list'][0]['data'][:314]
        return x_data,y_data

line = Line()
us_x_data,us_y_data = setdata('美国.txt','jsonp_1629344292311_69436(')
jp_x_data,jp_y_data = setdata('日本.txt','jsonp_1629350871167_29498(')
in_x_data,in_y_data = setdata('印度.txt','jsonp_1629350745930_63180(')
line.add_xaxis(us_x_data)
line.add_yaxis("美国确诊人数",us_y_data,label_opts=LabelOpts(is_show=False))
line.add_yaxis('日本确诊人数',jp_y_data,label_opts=LabelOpts(is_show=False))
line.add_yaxis("印度确诊人数",in_y_data,label_opts=LabelOpts(is_show=False))

line.set_global_opts(
    title_opts = TitleOpts(title="2020年美日印三国确诊人数对比折线图",pos_left='center',pos_bottom='1%')

)
line.render()