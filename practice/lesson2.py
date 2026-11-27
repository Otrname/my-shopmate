# 1.函数
# def add(a, b):
#     return a + b
#
#
# result = add(3, 5)
# print(result)


# def bad_add(a, b):
#     print(a + b)
#
# x = bad_add(3, 5)
# print(x)

# 2.if判断
# def check_status(status):
#     if status == "已签收":
#         return "可以申请退货"
#     elif status == "运输中":
#         return "请等待收货"
#     else:
#         return "订单处理中"
#
# print(check_status("运输中"))
# print(check_status("已付款"))

# 3.异常处理
# orders = {"SO1": "耳机"}
# print(orders["SO999"])

# 加上安全网：
orders = {"SO1": "耳机"}
try:
    print(orders["SO999"])
except KeyError:
    print("订单不存在")