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

## 面试可能问
1. 字典用 `d["key"]` 和 `d.get("key")` 取值有什么区别？
2. JSON 和 Python 字典是一回事吗？
