# Python后端开发第一周详细学习计划

## 学习目标
通过本周的学习，掌握Python基础语法和核心概念，为后续后端开发打下坚实基础。

## 第1-2天：Python基础与数据结构

### 上午学习内容（2小时）

#### Python基础语法
1. Python环境搭建
   - Python解释器安装
   - IDE选择和配置（PyCharm或VS Code）
   - 虚拟环境创建：
```python
python -m venv myenv
source myenv/bin/activate  # Linux/Mac
myenv\Scripts\activate     # Windows
```

2. 基本语法规则
   - 缩进规范（与JavaScript的显著区别）
   - 注释使用（单行#和多行'''）
   - 变量命名规范
   - Python代码风格（PEP 8）

3. 基本数据类型
```python
# 数值类型
age = 25                  # 整数
price = 19.99            # 浮点数
is_active = True         # 布尔值
name = "Python"          # 字符串

# 字符串操作
full_name = "John Doe"
print(len(full_name))    # 长度
print(full_name.upper()) # 大写转换
print(full_name.split()) # 分割

# f-string使用（类比JavaScript模板字符串）
print(f"Hello, {name}!")
```

### 下午学习内容（2小时）

#### 复合数据结构
1. 列表（List）
```python
# 列表操作
fruits = ['apple', 'banana', 'orange']
fruits.append('grape')           # 添加元素
fruits.insert(1, 'watermelon')  # 插入元素
fruits.remove('banana')         # 删除元素
print(fruits[0:2])             # 切片操作

# 列表方法
print(len(fruits))             # 长度
print(fruits.index('apple'))   # 查找索引
fruits.sort()                  # 排序
```

2. 元组（Tuple）
```python
# 元组示例（不可变列表）
coordinates = (10, 20)
date = ('2024', '12', '28')
```

3. 字典（Dict）
```python
# 字典操作（类比JavaScript对象）
user = {
    'name': 'John',
    'age': 30,
    'skills': ['Python', 'JavaScript']
}

# 字典方法
print(user.get('name'))        # 获取值
user['location'] = 'Beijing'   # 添加键值对
print(user.keys())            # 所有键,等价于Object.keys(user)
print(user.values())          # 所有值
```

4. 集合（Set）
```python
# 集合操作
tags = {'python', 'coding', 'web'}
tags.add('backend')           # 添加元素
tags.remove('coding')         # 删除元素
```

### 练习任务
1. 创建一个简单的通讯录程序：
```python
contacts = {}

def add_contact():
    name = input("输入姓名: ")
    phone = input("输入电话: ")
    contacts[name] = phone
    print("联系人添加成功！")

def show_contacts():
    for name, phone in contacts.items():
        print(f"{name}: {phone}")
```

## 第3天：控制流与函数

### 上午学习内容（2小时）

#### 控制流
1. 条件语句
```python
# if/elif/else语句
age = 20
if age < 18:
    print("未成年")
elif age < 35:
    print("青年")
else:
    print("成年")

# 三元运算符
status = "成年" if age >= 18 else "未成年"
```

2. 循环
```python
# for循环
for i in range(5):
    print(i)

# while循环
count = 0
while count < 5:
    print(count)
    count += 1

# 列表推导式（特别注意！这是Python特有的）
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
evens = [x for x in numbers if x % 2 == 0]
```

### 下午学习内容（2小时）

#### 函数
1. 函数定义与调用
```python
# 基本函数
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# 可变参数
def sum_numbers(*args):
    return sum(args)

# 关键字参数
def user_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
```

2. Lambda函数
```python
# Lambda函数（类比JavaScript箭头函数）
square = lambda x: x**2
double = lambda x: x * 2
```

3. 装饰器
```python
# 简单装饰器
def timer(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"函数执行时间：{end - start}秒")
        return result
    return wrapper

@timer
def slow_function():
    import time
    time.sleep(1)
```

## 第4天：面向对象编程

### 上午学习内容（2小时）

#### 类和对象
```python
class User:
    def __init__(self, name, age):
        self.name = name
        self._age = age  # 约定私有属性
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("年龄不能为负数")
        self._age = value
    
    def greet(self):
        return f"你好，我是{self.name}"
```

### 下午学习内容（2小时）

#### 继承和多态
```python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "汪汪!"

class Cat(Animal):
    def speak(self):
        return "喵喵!"
```

## 第5天：模块和包管理

### 上午学习内容（2小时）

#### 模块系统
```python
# 模块导入
import os
from datetime import datetime
from random import randint

# 自定义模块
# utils.py
def validate_email(email):
    return '@' in email

# main.py
from utils import validate_email
```

### 下午学习内容（2小时）

#### 项目实战：TODO应用
1. 项目结构
```
todo_app/
    ├── __init__.py
    ├── models/
    │   ├── __init__.py
    │   └── todo.py
    ├── utils/
    │   ├── __init__.py
    │   └── file_handler.py
    └── main.py
```

## 每日练习建议
1. 早上学习新概念
2. 下午动手练习
3. 晚上复习和完成小项目
4. 记录学习笔记和遇到的问题

## 学习资源
1. Python官方文档
2. Real Python网站
3. GitHub上的Python入门项目

## 注意事项
1. 多写代码，少看视频
2. 遇到问题先尝试自己解决
3. 善用Python的交互式环境（REPL）
4. 做好笔记，特别是与Node.js的区别部分

## 周末项目任务
完成一个完整的命令行TODO应用，包含：
1. 任务的增删改查
2. 数据持久化
3. 命令行交互界面
4. 基本的错误处理

## 检验标准
- 能够独立编写基础Python程序
- 理解并运用Python的主要特性
- 掌握面向对象编程基础
- 能够创建和管理Python项目