from pyecharts.charts import Bar,Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType

with open('1960-2019全球GDP数据.csv','r',encoding='GBK') as f:
    data_lines = f.readlines()
data_lines.pop(0)
data_dict = {}
for line in data_lines:
    line_list = line.split(',')
    year = int(line_list[0])
    country = line_list[1]
    gdp = float(line_list[2])
    try:
       data_dict[year].append([country,gdp])
    except KeyError:
       data_dict[year]=[]
       data_dict[year].append([country, gdp])

sorted_year_list = sorted(data_dict.keys())

timeline =Timeline()
for year in sorted_year_list:
    data_dict[year].sort(key=lambda x:x[1],reverse=True)
    sorted_gdp_list = data_dict[year][:8]
    x_data = []
    y_data = []
    for country_gdp in sorted_gdp_list:
        x_data.append(country_gdp[0])
        y_data.append(round(country_gdp[1]/100000000,2))
    bar = Bar()
    x_data.reverse()
    y_data.reverse()
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP(亿)",y_data,label_opts=LabelOpts(position='right'))
    bar.set_global_opts(
        title_opts=TitleOpts(title=f'{year}年全球前八GDP图')
    )
    bar.reversal_axis()


    timeline.add(bar,str(year))

timeline.add_schema(
    is_auto_play=True,
    play_interval=1000,
    is_timeline_show=True,
    is_loop_play=True
)
timeline.render('1960-2019全球GDP数据.html')