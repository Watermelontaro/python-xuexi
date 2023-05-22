from pyecharts.charts import Bar, Timeline
from pyecharts.options import *

with open("E:\Axuexi\Python\资料\可视化案例数据\动态柱状图数据\\1960-2019全球GDP数据.csv", "r", encoding="GB2312") as f:
    data_list = f.readlines()
    data_list.pop(0)
data_dict = {}
# s = 0
for i in data_list:
    year = int(i.split(",")[0])
    country = i.split(",")[1]
    gdp = float(i.split(",")[2])
    try:
        data_dict[year].append([country, gdp])
    except KeyError:
        data_dict[year] = []
        data_dict[year].append([country, gdp])
# 对年份进行排序
data_key = sorted(data_dict.keys())
# 获取时间线对象
timeline = Timeline()
# 对gdp进行排序
for s in data_dict:
    data_dict[s].sort(key=lambda e: e[1], reverse=True)
    data_s = data_dict[s][0:8]
    x_data = []
    y_data = []
    for gdp in data_s:
        x_data.append(gdp[0])
        y_data.append(gdp[1])
    # 构建树状图
    bar = Bar()
    x_data.reverse()
    y_data.reverse()
    bar.add_xaxis(x_data)
    # label_opts=LabelOpts(position="right"):让标签在右侧
    bar.add_yaxis("GDP(亿）", y_data, label_opts=LabelOpts(position="right"))
    bar.reversal_axis()
    # 每一年的图标的标题
    bar.set_global_opts(
        title_opts=TitleOpts(title=f"{s}年全球前八GDP数据")
    )
    # 创建时间线
    timeline.add(bar, str(s))
# 设置时间线自动播放
timeline.add_schema(
    # 时间线播放间隔
    play_interval=1000,
    # 时间线是否显示
    is_timeline_show=True,
    # 是否自动播放
    is_auto_play=True,
    # 是否循环播放
    is_loop_play=False
)
# 绘制
timeline.render("1960~2019全球GDP前八国家.html")
