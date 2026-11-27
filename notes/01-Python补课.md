# 阶段 1：Python 补课

## 第 1 课：列表、字典、JSON、读文件

### 1. 列表 list

**是什么**：按顺序排好的一串东西，用方括号 `[]`。

**解决什么问题**：要处理"多个"同类东西时（多件商品、多条消息），不用起一堆变量名。

**比喻**：排队的队伍，每人有个座位号，**座位号从 0 开始**。

**常用代码**
```python
items = ["耳机", "充电宝", "手表"]
items[0]          # "耳机"（第 1 个）
items[-1]         # "手表"（最后一个）
len(items)        # 3
items.append("数据线")   # 末尾加一个
for item in items:       # 挨个处理
    print(item)
```

**踩过的坑**：
- `items[10]` 报 `IndexError: list index out of range`。原因：列表只有 3 个元素，编号是 0–2，10 超出范围。解决：取之前先确认编号小于 `len(items)`。

**我的理解**：列表没有字段都对应一个索引值,索引从0开始,并且可以增删改查

---

### 2. 字典 dict

**是什么**：按"名字"找东西的容器，用花括号 `{}`，每一项是 `键: 值`。

**解决什么问题**：一条数据有很多属性（订单号、状态、金额），用名字取比用位置取清楚得多。

**比喻**：快递柜，报柜子编号（键）就能拿到里面的东西（值）。

**常用代码**
```python
order = {"status": "已签收", "total": 89.0}
order["status"]            # "已签收"
order.get("refund")        # 键不存在时返回 None，不报错
order.get("refund", "无")  # 键不存在时返回 "无"
order["refund"]            # 键不存在时报 KeyError
order["note"] = "加急"      # 新增或修改
for key, value in order.items():
    print(key, value)
```

**嵌套**：字典里可以放列表，列表里可以放字典，一层层取：`orders["SO20261101"]["items"][0]["name"]`

**踩过的坑**：
- `order["refund"]` 报 `KeyError: 'refund'`。原因：字典里没有这个键。解决：不确定键在不在时用 `order.get("refund")`。

**我的理解**：
字典就是一个键对应一个值,没有重复的键,可通过键找值,字典中也可以有列表等其他字段穿插

---

### 3. JSON

**是什么**：一种**纯文本**的数据格式，长得几乎和 Python 的字典、列表一样。

**解决什么问题**：程序之间、程序和文件之间交换数据要用统一格式。**调用大模型 API 时，发出去的请求和收回来的结果都是 JSON。**

**和 Python 的对应**：JSON 对象 `{}` ↔ 字典；JSON 数组 `[]` ↔ 列表；`true/false/null` ↔ `True/False/None`

**常用代码**
```python
import json
data = json.loads('{"a": 1}')                 # 文本 → 字典
text = json.dumps(data, ensure_ascii=False)   # 字典 → 文本（中文不转成 \uXXXX）
```

**踩过的坑**：

**我的理解**：
json合适就是一段文字,可以转化为别的数据类型,比如字典,就可以方便查值了

---

### 4. 读文件

**常用代码**
```python
import json

with open("data/orders.json", encoding="utf-8") as f:
    orders = json.load(f)    # 直接从文件读成字典
```
- `with`：用完自动关闭文件
- `encoding="utf-8"`：文件里有中文时必须写，否则可能乱码或报错
- 路径 `data/orders.json` 是**相对于运行命令时所在的文件夹**

**踩过的坑**：
- 在主目录运行 `uv run ~/Desktop/my-shopmate/practice/lesson1.py` 报 `FileNotFoundError: ... 'data/orders.json'`。原因：`open` 里写的是**相对路径**，Python 从**运行命令时所在的文件夹**（主目录）去找，主目录下没有 `data` 文件夹。解决：先 `cd` 进项目文件夹再运行。

**我的理解**：
打开文件后可以自动关闭,但是得注意打开文件路径

---

## 第 2 课：函数、if 判断、异常处理

### 1. 函数

**是什么**：把一段代码打包起来，取个名字，想用的时候喊它的名字就行。

**解决什么问题**：同一段逻辑（比如"查订单"）要在很多地方用，不用每次都重写一遍；以后大模型 Agent 调用的"工具"，本质上就是一个个函数。

**比喻**：榨汁机。放进去的东西叫**参数**（苹果），出来的东西叫**返回值**（苹果汁）。

**常用代码**
```python
def add(a, b):        # def 定义函数，a、b 是参数
    return a + b      # return 把结果交出去

result = add(3, 5)    # result 是 8
```
- `print` 只是显示到屏幕上；`return` 才是把结果交给调用的人。
- 没写 `return` 的函数，返回的是 `None`。

**踩过的坑**：
- 跟练 `bad_add` 里只写了 `print(a + b)`，`x = bad_add(3, 5)` 之后 `print(x)` 显示 `None`。原因：函数只打印、没 `return`，什么都没交出来。解决：要把结果给别人用，就必须 `return`。

**我的理解**：把代码打包,在里面有一些操作,当用到的时候可以调用,相当于一个工具

---

### 2. if 判断

**是什么**：根据条件决定程序走哪条路。

**解决什么问题**：程序要"看情况办事"，比如订单是不是这个客户的、状态是不是"已签收"。

**比喻**：门卫，看一眼你的证件，决定放不放你进去。

**常用代码**
```python
if status == "已签收":
    ...
elif status == "运输中":
    ...
else:
    ...

if order_id not in orders:          # in / not in：键在不在字典里
    ...
if order["customer_id"] != customer_id:   # != 不相等
    ...
```
- `==` 是比较，`=` 是赋值，别搞混。
- 条件后面加冒号 `:`，下一行缩进 4 个空格。

**踩过的坑**：
- （暂无，遇到了再补）

**我的理解**：根据条件不同，走不同的路

---

### 3. 异常处理

**是什么**：程序出错时不直接崩溃，而是由你决定怎么处理。

**解决什么问题**：用户会输错订单号、文件可能不存在。不处理的话程序直接报红退出；处理了就能给用户一句友好的提示。

**比喻**：走钢丝下面的安全网。网只铺在钢丝下面，不要铺满整个马戏场。

**常用代码**
```python
# 主动报错：自己判断"这不行"
raise KeyError("订单不存在")
raise PermissionError("无权查询他人订单")

# 接住错误
try:
    order = get_order(order_id, customer_id)   # 只放可能出错的那一行
except (KeyError, PermissionError):            # 一次接多种异常，用括号
    print("抱歉，没有找到这个订单")
else:
    print(order["status"])                     # 没出错才执行，且不在安全网里
```
| 异常 | 什么时候出现 |
|---|---|
| `KeyError` | 字典里没有这个键 |
| `FileNotFoundError` | 文件路径不对 |
| `ValueError` | 值不对，比如 `int("abc")` |
| `PermissionError` | 没有权限 |

**踩过的坑**：
- 作业第一版把 4 行 `print` 也放进了 `try`。问题：打印时如果手滑写错键名（`order['stauts']`），也会抛 `KeyError`，被当成"订单不存在"，真 bug 被藏起来了。解决：`try` 里只放 `get_order` 那一行，打印挪到 `else` 里。
- `.strip()` 在主程序和 `get_order` 里各写了一次，重复了。改成只在 `get_order` 里写，因为以后调用它的可能是大模型 Agent，函数自己要能处理脏数据。

**我的理解**：遇到错误的时候代码不直接报错,保证接下来也能执行,获取报错信息,raise 是自己主动报错；try 里只放可能出错的那一行。

---

## 第 3 课：类与对象

### 1. 类和对象

**是什么**：类是一个模具，规定"这种东西有什么数据、能做什么"；对象是用模具造出来的一个个具体的东西。

**解决什么问题**：把"数据"和"操作数据的函数"装进同一个盒子，不用让一堆函数共用散落在外面的变量。比如 `OrderStore` 把订单数据和查订单、列订单的方法放在一起。

**比喻**：月饼模具和月饼。一个模具能压出很多月饼，每个月饼的馅可以不一样。

**常用代码**
```python
class OrderStore:                       # 类名首字母大写
    def __init__(self, path):           # 创建对象时自动执行，"出厂设置"
        with open(path, encoding="utf-8") as f:
            self.orders = json.load(f)  # 属性：对象长期记住的数据

    def list_orders(self, customer_id): # 方法：第一个参数永远是 self
        ...

store = OrderStore("data/orders.json")  # 造一个对象，self 不用自己传
store.list_orders("C1001")              # 用 . 调用方法
store.orders                            # 用 . 取属性
```
- `self` 指"这个对象自己"。
- **什么该挂在 `self` 上**：对象要长期记住的东西（比如仓库里的 `self.orders`）。只在某一次调用里临时用的（比如这次查询的订单号），用普通变量就行。

**踩过的坑**：
- 类里的方法忘了写 `self`，报 `TypeError: Bad.hello() takes 1 positional argument but 2 were given`。原因：调用时 Python 会自动把对象本身传进去当第一个参数。解决：每个方法第一个参数都写 `self`。
- 作业里写了 `self.order_id = order_id.strip()`，下一行用的却是 `order_id`，`strip` 白做了。而且订单号只是这次查询用的，不该挂在 `self` 上。解决：改成普通变量 `order_id = order_id.strip()`。

**我的理解**：类是模具，对象是用这个模具做出来的具体成品（实例），就像月饼模具和压出来的每个月饼。类的作用是把“数据（属性）”和“操作这些数据的函数（方法）”装在一起，比如 OrderStore 里既装了订单数据 self.orders，也装了查订单、列订单、算总额这些方法。只有需要对象长期保存、多个方法共用的数据才写成 self.xxx，只在当前方法里临时用一下的变量直接用普通变量就行。

---

### 2. 遍历字典与 `+=` 累加

**是什么**：`for` 直接遍历字典只拿到键；用 `.items()` 每次拿到一对（键, 值），`for` 后面写两个变量把它拆开。`+=` 是"在原来基础上加"。

**解决什么问题**：要从字典里按条件筛出一部分（某个客户的所有订单号），或者把它们的金额加起来。

**比喻**：一排储物柜。直接 `for` 只看到柜号；`.items()` 是管理员每次递给你一个托盘，左边放柜号，右边放柜里的东西。`+=` 像往存钱罐里一笔一笔投钱。

**常用代码**
```python
for order_id in orders:                     # 只拿到键（柜号）
    ...
for order_id, order in orders.items():      # 键和值一起拿
    if order["customer_id"] == customer_id: # 判断用右手（值）
        result.append(order_id)             # 收集左手（键）

total = 0                                   # 先拿个空罐子
for order_id, order in orders.items():
    total += order["total"]                 # 等于 total = total + order["total"]
```

**踩过的坑**：
- 作业里写 `for order in self.orders:` 然后用 `order["customer_id"]`，报 `TypeError: string indices must be integers, not 'str'`。原因：直接遍历字典拿到的是键（字符串 `"SO20261101"`），不是订单字典。解决：改成 `for order_id, order in self.orders.items():`。
- 变量名用了 `list`，把 Python 自带的 `list` 盖掉了。解决：换成 `result`、`order_ids` 这种名字。

**我的理解**：直接 for x in orders: 遍历字典时，x 拿到的只是键（key，比如订单号字符串），相当于只拿到储物柜编号、没拿到里面的东西，所以直接取值会报 TypeError；加上 .items() 后，for a, b in orders.items(): 每次能同时拿到键和值，a 是键（订单号），b 是对应的值（订单详情字典）。total += 5 等价于 total = total + 5，就是把原来的值加上 5 再存回 total。

---

## 面试可能问
1. 字典用 `d["key"]` 和 `d.get("key")` 取值有什么区别？
2. JSON 和 Python 字典是一回事吗？
3. 函数里 `print` 和 `return` 有什么区别？
4. 查询订单时，"订单不存在"和"不是你的订单"为什么要给用户一样的提示？
5. `try` 块里为什么不要放太多代码？`else` 有什么用？
6. 类和对象是什么关系？`self` 是什么？
7. 什么数据应该存成 `self.xxx`，什么用普通变量就行？
8. 把数据和函数装进一个类（比如 `OrderStore`），比全局变量加函数好在哪？
