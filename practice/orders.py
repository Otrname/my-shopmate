import json
with open("data/orders.json", encoding="utf-8") as f:
    orders = json.load(f)

for order_id, order in orders.items():
    print(order_id, "| 客户", order["customer_id"], "|", order["status"], "|", order["total"], order["currency"], "|", order["items"][0]["qty"], "件商品")

print(f"总共{len(orders)}个订单")
