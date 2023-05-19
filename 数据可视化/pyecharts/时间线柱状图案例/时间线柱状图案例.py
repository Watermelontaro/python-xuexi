with open("E:\Axuexi\Python\资料\可视化案例数据\动态柱状图数据\\1960-2019全球GDP数据.csv", "r", encoding="GB2312") as f:
    data_list = f.readlines()
    data_list.pop(0)
data_dict = {}
s = 0
for i in data_list:
    year = int(i.split(",")[0])
    country = i.split(",")[1]
    gdp = float(i.split(",")[2])
    try:
        data_dict[year].append([country, gdp])
    except KeyError:
        data_dict[year] = []
        data_dict[year].append([country, gdp])
    finally:
        if year != s:
            s = year
# print(data_dict)
data_dict[s] = data_dict[s].sort(key=lambda e: e[1])
print(data_dict)
