from pyecharts.charts import Bar,Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType
bar1 = Bar()
bar1.add_xaxis(['美国', '中国', '日本'])
bar1.add_yaxis('美日中GDP', [20, 30, 40], label_opts=LabelOpts(position='right'))
bar1.reversal_axis()

bar2 = Bar()
bar2.add_xaxis(['美国', '中国', '日本'])
bar2.add_yaxis('美日中GDP', [40, 70, 50], label_opts=LabelOpts(position='right'))
bar2.reversal_axis()

timeline = Timeline({'theme':ThemeType.LIGHT})
timeline.add(bar1,'2021')
timeline.add(bar2,'2022')

timeline.add_schema(
    is_auto_play=True,
    play_interval=1000,
    is_timeline_show=True,
    is_loop_play=True
)
timeline.render()