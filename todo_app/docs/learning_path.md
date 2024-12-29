# TODO 应用学习路线

## 项目结构

```
todo_app/
    ├── docs/
    │   └── learning_path.md
    ├── models/
    │   ├── __init__.py
    │   └── todo.py          # Todo类定义
    ├── utils/
    │   ├── __init__.py
    │   └── file_handler.py  # 文件处理类
    ├── main.py             # 主程序
    └── todos.json          # 数据存储文件
```

## 第一阶段：Python 基础概念（1-2 天）

### 1. 类的基本概念

-  类的定义
- 构造函数
- 实例方法
- 类方法
- 魔术方法(`__str__`等)

示例代码:

```python
class SimpleTask:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"任务：{self.title}"
```

### 2. 文件操作

- 文件的读写模式
- 上下文管理器(with 语句)
- 异常处理

示例代码:

```python
# 文件写入
with open('test.txt', 'w') as f:
    f.write('Hello')

# 文件读取
with open('test.txt', 'r') as f:
    content = f.read()
```

### 3. JSON 数据处理

- json.dumps()
- json.loads()
- 文件持久化

示例代码:

```python
import json

data = {'name': 'Task 1'}
json_str = json.dumps(data)    # 转为JSON字符串
data = json.loads(json_str)    # 从JSON字符串转回Python对象
```

## 第二阶段：核心模块学习（2-3 天）

### 1. Todo 类（models/todo.py）

- 类属性设计
- 数据转换方法
- 字符串表示

学习重点:

- `__init__`方法参数设计
- to_dict()和 from_dict()方法
- `__str__`方法实现

### 2. 文件处理器（utils/file_handler.py）

- 文件持久化实现
- ID 生成机制
- JSON 文件操作

学习重点:

- 文件存在性检查
- 数据读写操作
- ID 自增实现

### 3. 主程序（main.py）

- TodoApp 类设计
- 命令行交互
- 业务逻辑

学习重点:

- 类的组合使用
- 用户交互实现
- 错误处理机制

## 第三阶段：动手实践（3-4 天）

### 1. 简单版本实现

```python
class SimpleTodo:
    def __init__(self, title):
        self.title = title
        self.completed = False

    def complete(self):
        self.completed = True
```

### 2. 添加文件持久化

```python
class SimpleFileHandler:
    def save_todo(self, todo):
        with open('todo.txt', 'a') as f:
            f.write(f"{todo.title}\n")
```

### 3. 实现基本功能

```python
class SimpleTodoApp:
    def __init__(self):
        self.todos = []

    def add_todo(self, title):
        self.todos.append(SimpleTodo(title))
```

## 第四阶段：功能扩展（4-5 天）

### 1. 新功能添加

- 任务优先级
- 任务截止日期
- 任务标签

### 2. 错误处理改进

```python
def complete_todo(self, todo_id):
    try:
        todo_id = int(todo_id)
        # 处理逻辑
    except ValueError:
        print("无效的ID格式")
    except Exception as e:
        print(f"发生错误: {e}")
```

### 3. 用户界面优化

- 彩色输出
- 任务显示格式优化
- 交互式菜单改进

## 第五阶段：项目提升（5-7 天）

### 1. 代码优化

- 添加类型提示
- 完善代码注释
- 优化代码结构

### 2. 单元测试

```python
import unittest

class TestTodo(unittest.TestCase):
    def test_create_todo(self):
        todo = Todo("测试任务")
        self.assertEqual(todo.title, "测试任务")
```

### 3. 高级功能

- 多用户支持
- 数据库集成
- 导入导出功能

## 学习建议

### 1. 学习顺序

1. 运行完整程序体验功能
2. 从 Todo 类开始理解
3. 理解整体架构

### 2. 实践方法

1. 照着代码实现一遍
2. 不看代码独立实现
3. 尝试添加新功能

### 3. 重点关注

- 类的设计方式
- 数据持久化实现
- 代码组织结构
- 错误处理机制

### 4. 扩展学习

- Python 装饰器
- 文件操作最佳实践
- JSON 数据处理
- 命令行界面设计

## 检验标准

- 理解并能解释代码实现
- 独立完成基础功能开发
- 能够添加新的功能特性
- 代码符合 Python 规范
