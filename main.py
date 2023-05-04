name = "传智播客"
stock_code = "003032"
print(f"公司：{name}\n股票代码：{stock_code}")
stock_price = float(input("输入当前的股价："))
stock_price_daily_growth_factor = 1.2
growth_days = 7
finally_stock_price = stock_price * stock_price_daily_growth_factor ** growth_days
print(f"公司：{name}，股票代码：{stock_code}，当前股价：{stock_price}")
print("每日增长系数：%.1f，经过%d天的增长后，股价达到：%.2f" % (
    stock_price_daily_growth_factor, growth_days, finally_stock_price))
# 基本语句的使用
