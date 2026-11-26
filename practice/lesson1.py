# 1.列表
# items = ["耳机", "充电宝", "手表"]
#
# print(items[10])
# print(items[-1])
# print(len(items))
#
# items.append("数据线")
# print(items)
#
# for item in items:
#     print("商品: ", item)

# 2.字典
# order = {
#     "order_id": "S020261101",
#     "status": "已签收",
#     "total": 89.0,
#
# }
#
# print(order["status"])
# print(order["total"])
#
# order["status"] = "退款中"
# print(order)
#
# print(order["refund"])
# print(order.get("refund"))
# print(order.get("refund", "没有退款记录"))
#
# for key, value in order.items():
#     print(key, "=>", value)

#3.嵌套
# orders["S020261101"]["items"][0]["name"]

import json
with open("data/orders.json", encoding="utf-8") as f:
    orders = json.load(f)

print(type(orders))
print(len(orders))

first = orders["SO20261101"]
print(first["status"])
print(first["items"][0]["name"])

text = json.dumps(first, ensure_ascii=False)
print(type(text))
print(text)