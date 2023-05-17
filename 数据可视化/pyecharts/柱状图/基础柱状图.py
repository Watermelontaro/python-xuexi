from pyecharts.charts import Bar

bar = Bar()
bar.add_xaxis(["英", "日", "美"])
bar.add_yaxis("柱状图", [10, 33, 22])
# 让柱状图的X轴和Y轴反转：
# bar.reversal_axis()
bar.render("基础柱状图.html")
