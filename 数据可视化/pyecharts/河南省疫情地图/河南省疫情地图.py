import json

from pyecharts.charts import Map
from pyecharts.options import TitleOpts, VisualMapOpts

f = open("E:\Axuexi\Python\资料\可视化案例数据\地图数据\疫情.txt", "r", encoding="utf-8")
data = f.read()
f.close()
data = json.loads(data)
data = data["areaTree"][0]["children"][3]["children"]
data_list = []
for i in data:
    if i["name"] == "济源示范区":
        data_name = "济源市"
    else:
        data_name = i["name"] + "市"
    data_total = i["total"]["confirm"]
    data_list.append((data_name, data_total))
print(data_list)
map = Map()
map.set_global_opts(
    title_opts=TitleOpts(title="河南省"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {min: 1, max: 10, "liable": "1~10", "color": ""},
        ]
    )
)
map.add("河南省疫情数据可视化地图", data_list, "河南")

map.render("河南省疫情地图.html")
