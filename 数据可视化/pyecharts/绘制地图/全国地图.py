from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

map = Map()
data = [
    ("北京市", 99),
    ("辽宁省", 199),
    ("内蒙古省", 299),
    ("湖北省", 399),
    ("山东省", 499),
    ("上海市", 599),
    ("广东省", 699)
]
map.add("全国", data, "china")
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 9, "label": "1-9人", "color": "#ccffff"},
            {"min": 10, "max": 99, "label": "10-99人", "color": "#ffff99"},
            {"min": 100, "max": 999, "label": "100-999人", "color": "#ff9966"},
            {"min": 1000, "max": 9999, "label": "1000-9999人", "color": "#ff6666"},
            {"min": 10000, "max": 99999, "label": "10000-99999人", "color": "#ff3333"}
        ]
    )
)
map.render()
