import json

fus = open("E:\Axuexi\Python\资料\可视化案例数据\折线图数据\美国.txt", "r", encoding="utf-8")
us_data = fus.read()
us_data = us_data.replace("jsonp_1629344292311_69436(", "")
us_data = us_data[:-2]
# 将json数据转换为Python数据
js_us = json.loads(us_data)
trend_key = js_us["data"][0]["trend"]
x_data = trend_key["updateDate"][:314]
print(x_data)
y_data = trend_key["list"][0]["data"][:314]
