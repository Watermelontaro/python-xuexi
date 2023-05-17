# 从文件中获取数据
import json

from pyecharts.charts import Map
from pyecharts.options import TitleOpts, VisualMapOpts

f = open("E:\Axuexi\Python\资料\可视化案例数据\地图数据\疫情.txt", "r", encoding="utf-8")
data = f.read()
# 关闭文件
f.close()
data_dict = json.loads(data)
data_n = data_dict["areaTree"][0]["children"]

data_list = []
for i in data_n:
    if i["name"] == "上海" or i["name"] == "北京" or i["name"] == "天津" or i["name"] == "重庆":
        x = i["name"] + "市"
    elif i["name"] == "香港" or i["name"] == "澳门":
        x = i["name"] + "特别行政区"
    elif i["name"] == "内蒙古" or i["name"] == "西藏":
        x = i["name"] + "自治区"
    elif i["name"] == "新疆":
        x = i["name"] + "维吾尔自治区"
    elif i["name"] == "广西":
        x = i["name"] + "壮族自治区"
    else:
        x = i["name"] + "省"
    y = i["total"]["confirm"]
    data_list.append((x, y))
print(data_list)
maps = Map()
maps.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图", pos_left="center", pos_bottom="1%"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 9, "label": "1-9人", "color": "#ccffff"},
            {"min": 10, "max": 99, "label": "10-99人", "color": "#ffff99"},
            {"min": 100, "max": 999, "label": "100-999人", "color": "#ff9966"},
            {"min": 1000, "max": 9999, "label": "1000-9999人", "color": "#ff6666"},
            {"min": 10000, "label": "10000-99999人", "color": "#ff3333"}
        ]
    )

)
maps.add("全国疫情地图", data_list, "china")
maps.render("全国疫情地图.html")
