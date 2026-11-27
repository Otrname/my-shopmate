# 1.类和对象: 模具和月饼
# region
# class Customer:
#     def __init__(self, customer_id, name):
#         self.customer_id = customer_id
#         self.name = name
#
#     def greet(self):
#         return f"您好, {self.name}! 您的客户编号是 {self.customer_id}"
#
#
# a = Customer("C1001", "小明")
# b = Customer("C1002", "Alice")
# print(a.greet())
# print(b.greet())
# print(a.name)
# endregion

# 2.方法
# region
# class Order:
#     def __init__(self, order_id, status):
#         self.order_id = order_id
#         self.status = status
#
#     def ship(self):
#         self.status = "运输中"
#
#
# o = Order("SO1", "已付款")
# print(o.status)
# o.ship()
# print(o.status)
# endregion

# 3.属性
#region
# class Cart:
#     def __init__(self):
#         self.items = []
#
#     def add(self, name, price):
#         self.items.append({"name": name, "price": price})
#
#     def total(self):
#         result = 0
#         for item in self.items:
#             result += item["price"]
#         return result
#
#
# cart = Cart()
# cart.add("耳机", 89.0)
# cart.add("充电宝", 35.5)
# print(cart.items)
# print(len(cart.items))
# print(cart.total())

#endregion

# 4.坑
# region
# class Bad:
#     def hello(name):
#         return name
#
# Bad().hello("x")

# endregion

# 例题
class ProductStore:
    def __init__(self, products):
        self.products = products

    def get_product(self, product_id, seller_id):
        product_id = product_id.strip()
        if product_id not in self.products:
            raise KeyError("商品不存在")

        product = self.products[product_id]
        if product["seller_id"] != seller_id:
            raise PermissionError("无权查看其他商家的商品")

        return product

    def list_products(self, seller_id):
        result = []
        for product_id, product in self.products.items():
            if product["seller_id"] == seller_id:
                result.append(product_id)
        return result

    def total_stock(self, seller_id):
        total = 0
        for product_id, product in self.products.items():
            if product["seller_id"] == seller_id:
                total += product["stock"]
        return total


if __name__ == "__main__":
    products = {
        "P001": {"seller_id": "S1", "name": "耳机", "stock": 10},
        "P002": {"seller_id": "S1", "name": "充电宝", "stock": 5},
        "P003": {"seller_id": "S2", "name": "手表", "stock": 3},
    }
    store = ProductStore(products)

    result = store.list_products("S1")
    print(f"S1 的商品：{result}")
    result = store.list_products("S9")
    print(f"S9 的商品：{result}")
    print("---")

    print("S1 查 P002：")
    try:
        product = store.get_product("P002", "S1")
    except (KeyError, PermissionError):
        print("抱歉，没有找到这个商品。")
    else:
        print(f"名称：{product['name']}")
        print(f"库存：{product['stock']}")
    print("---")

    print("S1 查 P003：")
    try:
        product = store.get_product("P003", "S1")
    except (KeyError, PermissionError):
        print("抱歉，没有找到这个商品。")
    else:
        print(f"名称：{product['name']}")
        print(f"库存：{product['stock']}")
    print("---")

    total = store.total_stock("S1")
    print(f"S1 总库存：{total}")




