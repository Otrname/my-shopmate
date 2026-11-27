# ============================================================
# 阶段 1 第 3 课作业：订单仓库 OrderStore（把数据和操作装进一个类）
# 运行方式：uv run practice/order_store.py
# ============================================================
#
# 【场景】
# 第 2 课你写了一个 get_order 函数，它用的 orders 字典放在函数外面。
# 现在 ShopMate 要加更多功能（查订单、列出订单、算消费总额……），
# 如果每个功能都是一个散落的函数，再加一个到处共用的 orders，很快就乱了。
# 这节课把"订单数据"和"操作订单的方法"装进同一个类：OrderStore（订单仓库）。
# 以后 Agent 的"查订单"工具，背后就是调用这个仓库。
#
# ------------------------------------------------------------
# 【数据从哪来】
# 还是 data/orders.json，和第 2 课一样，4 个订单：
#
#   订单号        客户    状态     商品                              金额
#   SO20261101   C1001   已签收   降噪蓝牙耳机 Pro 2                  89.0 USD
#   SO20261115   C1001   运输中   20000mAh 快充移动电源 ×2            71.0 USD
#   SO20261120   C1002   已付款   智能手表 S3                        129.0 EUR
#   SO20261003   C1003   已签收   65W 氮化镓充电器、Type-C 数据线    5960.0 JPY
#
# 区别：这次不在文件最上面读数据，而是在类的 __init__ 里读。
#
# ------------------------------------------------------------
# 【分步任务】
#
# 第 1 步：定义类 OrderStore，写 __init__(self, path)
#   - path 是订单文件的路径，比如 "data/orders.json"
#   - 用第 1 课的 with open + json.load 读文件
#   - 把读到的字典存到 self.orders 里（这样其他方法都能用到它）
#
# 第 2 步：写方法 get_order(self, order_id, customer_id)
#   - 规则和第 2 课一模一样（不存在 → raise；不是这个客户的 → raise；否则 return 订单字典）
#   - 区别：数据要从 self.orders 里拿，而不是外面的 orders
#
# 第 3 步：写方法 list_orders(self, customer_id)
#   - 返回一个列表，里面是这个客户的所有订单号
#   - 思路：先准备一个空列表，遍历 self.orders，客户对得上就 append 进去，最后 return
#   - 用到：第 1 课的 for 遍历字典 .items()、列表 append；第 2 课的 if
#
# 第 4 步：写主程序（放在 if __name__ == "__main__": 下面）
#   - 创建一个仓库对象：store = OrderStore("data/orders.json")
#   - 按下面"预期输出"依次调用方法、打印结果
#   - 查订单那部分用第 2 课的 try / except / else
#
# ------------------------------------------------------------
# 【预期输出】（运行一次，屏幕上应该完整显示下面这些）
#
#   C1001 的订单：['SO20261101', 'SO20261115']
#   C1003 的订单：['SO20261003']
#   C9999 的订单：[]
#   ---
#   C1001 查 SO20261115：
#   状态：运输中
#   金额：71.0 USD
#   ---
#   C1001 查 SO20261120：
#   抱歉，没有找到这个订单，请检查订单号是否正确。
#
# 说明：
#   - C9999 是一个没有任何订单的客户，应该得到空列表 []，程序不能报错。
#   - 中间的 --- 用 print("---") 打出来就行。
#
# ------------------------------------------------------------
# 【加分项】（做完基础部分再做）
#   写方法 total_amount(self, customer_id)：返回这个客户所有订单金额的总和。
#   预期：
#     C1001 消费总额：160.0
#   提示：跟练例子 3 里购物车 total() 的写法（先设 0，循环里 +=）。
#   （先不管币种不同的问题，C1001 的两个订单都是 USD。）
#
# ------------------------------------------------------------
# 【思考题】写完代码后回答：
#   和第 2 课"一个 orders 变量 + 一个 get_order 函数"比，
#   把它们装进 OrderStore 类里，有什么好处？至少说出一点。
#   提示：想想如果测试时想换一份假数据文件，两种写法各要改哪里。
#   我的回答：
#   1. 换数据更方便：测试时想换一份假数据，只需要 `OrderStore("data/test_orders.json")` 传不同路径
#      就能创建新仓库对象，不用去改文件最上面写死的全局变量。
#   2. 数据和逻辑打包在一起：所有操作订单的方法都通过 `self.orders` 读写同一份数据，
#      不会出现全局变量到处被改、代码越写越乱的问题，也能同时存在多个互不干扰的仓库实例。
#
# ------------------------------------------------------------
# 【自查清单】交给导师 review 前，自己先打勾：
#   [x] 运行结果和预期输出完全一致
#   [x] 类里的方法第一个参数都是 self
#   [x] 方法里用的是 self.orders，没有用类外面的变量
#   [x] get_order / list_orders 里没有 print，只 return / raise
#   [x] 思考题写了回答
#
# ============================================================

# 从这里开始写你的代码 ↓
import json


class OrderStore:
    # 第 1 步：定义类 OrderStore，写 __init__(self, path)
    def __init__(self, path):
        self.path = path
        with open(path, "r", encoding="utf-8") as f:
            self.orders = json.load(f)

    # 第 2 步：写方法 get_order(self, order_id, customer_id)
    def get_order(self, order_id, customer_id):
        order_id = order_id.strip()
        if order_id not in self.orders:
            raise KeyError("订单不存在")

        order = self.orders[order_id]
        if order["customer_id"] != customer_id:
            raise PermissionError("无权查询他人订单")

        return order

    # 第 3 步：写方法 list_orders(self, customer_id)
    def list_orders(self, customer_id):
        result = []
        for order_id, order in self.orders.items():
            if order["customer_id"] == customer_id:
                result.append(order_id)
        return result

    # 加分项：计算某个客户所有订单金额总和
    def total_amount(self, customer_id):
        total = 0
        for order_id, order in self.orders.items():
            if order["customer_id"] == customer_id:
                total += order["total"]
        return total


# 第 4 步：写主程序（放在 if __name__ == "__main__": 下面）
if __name__ == "__main__":
    store = OrderStore("data/orders.json")

    print(f"C1001 的订单：{store.list_orders('C1001')}")
    print(f"C1003 的订单：{store.list_orders('C1003')}")
    print(f"C9999 的订单：{store.list_orders('C9999')}")

    print("---")
    print("C1001 查 SO20261115：")
    try:
        order = store.get_order("SO20261115", "C1001")
    except (KeyError, PermissionError):
        print("抱歉，没有找到这个订单，请检查订单号是否正确。")
    else:
        print(f"状态：{order['status']}")
        print(f"金额：{order['total']} {order['currency']}")

    print("---")
    print("C1001 查 SO20261120：")
    try:
        order = store.get_order("SO20261120", "C1001")
    except (KeyError, PermissionError):
        print("抱歉，没有找到这个订单，请检查订单号是否正确。")
    else:
        print(f"状态：{order['status']}")
        print(f"金额：{order['total']} {order['currency']}")

    print("---")
    print(f"C1001 消费总额：{store.total_amount('C1001')}")

