import json

data = [{"name": "老王", "age": 18}, {"name": "张三", "age": 20}]
print(data)
print(type(data))
# Python数据转换为json数据：
data = json.dumps(data,ensure_ascii=False)
print(data)
print(type(data))
# json数据转换为Python数据：
data = json.loads(data)
print(data)
print(type(data))
