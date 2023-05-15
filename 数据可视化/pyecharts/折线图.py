from pyecharts.charts import Line

line = Line()
print(line)
line.add_xaxis(["中国", "美国", "英国"])
line.add_yaxis("GDP", [30, 20, 10])
line.render()