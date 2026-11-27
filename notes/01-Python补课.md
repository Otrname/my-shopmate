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

## 面试可能问
1. 字典用 `d["key"]` 和 `d.get("key")` 取值有什么区别？
2. JSON 和 Python 字典是一回事吗？
3. 函数里 `print` 和 `return` 有什么区别？
4. 查询订单时，"订单不存在"和"不是你的订单"为什么要给用户一样的提示？
5. `try` 块里为什么不要放太多代码？`else` 有什么用？
