from pyecharts.charts import Line
from pyecharts.options import TitleOpts, ToolboxOpts, VisualMapOpts, LegendOpts

line = Line()
# x轴
line.add_xaxis(["中国", "美国", "英国"])
# y轴
line.add_yaxis("GDP", [30, 20, 10])
# 全局控制项
line.set_global_opts(
    title_opts=TitleOpts(title="GDP工具", pos_left="center", pos_bottom="1%"),
    toolbox_opts=ToolboxOpts(is_show=True),
    legend_opts=LegendOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True)

)
# 生成图像
line.render()
