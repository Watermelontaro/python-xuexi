from pyecharts.charts import Bar, Timeline
from pyecharts.globals import ThemeType
from pyecharts.options import LabelOpts

bar1 = Bar()
bar1.add_xaxis(["中国", "美国", "英国"])
bar1.add_yaxis("GDP", [50, 30, 20], label_opts=LabelOpts(position="right"))
bar1.reversal_axis()
bar2 = Bar()
bar2.add_xaxis(["中国", "美国", "英国"])
bar2.add_yaxis("GDP", [40, 50, 60], label_opts=LabelOpts(position="right"))
bar2.reversal_axis()
bar3 = Bar()
bar3.add_xaxis(["中国", "美国", "英国"])
bar3.add_yaxis("GDP", [100, 70, 50], label_opts=LabelOpts(position="right"))
bar3.reversal_axis()
# 时间线实例
timeline = Timeline({"theme": ThemeType.ROMANTIC})
# 添加时间线
timeline.add(bar1, "点1")
timeline.add(bar2, "点2")
timeline.add(bar3, "点3")
# 设置时间线模式
timeline.add_schema(
    # 自动播放的时间间隔
    play_interval=1000,
    # 是都在自动播放的时候显示时间线
    is_timeline_show=False,
    # 是否自动播放
    is_auto_play=True,
    # 是否循环播放
    is_loop_play=True
)

timeline.render("时间线柱状图.html")
