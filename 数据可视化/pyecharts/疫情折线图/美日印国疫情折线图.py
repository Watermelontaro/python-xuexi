import json

from pyecharts.charts import Line
from pyecharts.options import TitleOpts, ToolboxOpts, LegendOpts, LabelOpts

# 获取美国数据
fus = open("E:\Axuexi\Python\资料\可视化案例数据\折线图数据\美国.txt", "r", encoding="utf-8")
us_data = fus.read()
# 获取日本数据
fjp = open("E:\Axuexi\Python\资料\可视化案例数据\折线图数据\日本.txt", "r", encoding="utf-8")
jp_data = fjp.read()
# 获取印度数据
fin = open("E:\Axuexi\Python\资料\可视化案例数据\折线图数据\印度.txt", "r", encoding="utf-8")
in_data = fin.read()
# 去除不相关的数据
us_data = us_data.replace("jsonp_1629344292311_69436(", "")
us_data = us_data[:-2]
jp_data = jp_data.replace("jsonp_1629350871167_29498(", "")
jp_data = jp_data[:-2]
in_data = in_data.replace("jsonp_1629350745930_63180(", "")
in_data = in_data[:-2]
# 将json数据转换为Python数据
js_us = json.loads(us_data)
us_trend_key = js_us["data"][0]["trend"]
us_x_data = us_trend_key["updateDate"][:314]
us_y_data = us_trend_key["list"][0]["data"][:314]
# ```
js_jp = json.loads(jp_data)
jp_trend_key = js_jp["data"][0]["trend"]
jp_x_data = jp_trend_key["updateDate"][:314]
jp_y_data = jp_trend_key["list"][0]["data"][:314]
# ```
js_in = json.loads(in_data)
in_trend_key = js_in["data"][0]["trend"]
in_x_data = in_trend_key["updateDate"][:314]
in_y_data = in_trend_key["list"][0]["data"][:314]
# 生成折线图
line = Line()
line.set_global_opts(
    title_opts=TitleOpts(title="新冠确诊人数", pos_left="center", pos_bottom="1%"),
    toolbox_opts=ToolboxOpts(is_show=True),
    legend_opts=LegendOpts(is_show=True),
)
line.add_xaxis(us_x_data)
line.add_yaxis("美国的确诊人数", us_y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("日本的确诊人数", jp_y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("印度的确诊人数", in_y_data, label_opts=LabelOpts(is_show=False))
line.render()
fus.close()
fin.close()
fjp.close()
