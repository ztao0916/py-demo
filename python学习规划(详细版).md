# 第一周详细学习计划: 基础知识储备
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

```plain
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
+ 能够独立编写基础Python程序
+ 理解并运用Python的主要特性
+ 掌握面向对象编程基础
+ 能够创建和管理Python项目

# 第二周详细学习计划：Web框架基础
## 学习目标
掌握Flask框架基础，学习后端API开发核心概念，完成个人博客API系统的开发。

## 第1天：Flask入门与路由基础
### 上午学习内容（2小时）
#### Flask环境搭建
1. 安装Flask

```bash
pip install flask
pip install python-dotenv    # 用于环境变量管理
```

2. 创建第一个Flask应用

```python
# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Flask!'

if __name__ == '__main__':
    app.run(debug=True)
```

3. 基础路由设置

```python
# 不同HTTP方法的路由
@app.route('/users', methods=['GET'])
def get_users():
    return {'users': ['user1', 'user2']}

@app.route('/users', methods=['POST'])
def create_user():
    return {'message': 'User created'}, 201

# URL参数
@app.route('/users/<int:user_id>')
def get_user(user_id):
    return {'user_id': user_id}
```

### 下午项目实战（2小时）
创建基础博客API框架：

```python
# blog/
#   ├── app.py
#   ├── config.py
#   └── requirements.txt

# app.py
from flask import Flask, jsonify

app = Flask(__name__)

# 示例博客数据
posts = [
    {
        'id': 1,
        'title': '第一篇博客',
        'content': '这是内容',
        'author': '张三'
    }
]

@app.route('/api/posts', methods=['GET'])
def get_posts():
    return jsonify(posts)

@app.route('/api/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = next((post for post in posts if post['id'] == post_id), None)
    if post is None:
        return {'error': 'Post not found'}, 404
    return jsonify(post)
```

## 第2天：请求处理与响应
### 上午学习内容（2小时）
#### 请求处理
```python
from flask import request

@app.route('/api/posts', methods=['POST'])
def create_post():
    if not request.is_json:
        return {'error': 'Content-Type must be application/json'}, 415
    
    data = request.get_json()
    
    # 数据验证
    if not all(key in data for key in ['title', 'content', 'author']):
        return {'error': 'Missing required fields'}, 400
    
    new_post = {
        'id': len(posts) + 1,
        'title': data['title'],
        'content': data['content'],
        'author': data['author']
    }
    posts.append(new_post)
    return jsonify(new_post), 201
```

#### 响应处理
```python
from flask import make_response, jsonify

@app.route('/api/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    global posts
    posts = [post for post in posts if post['id'] != post_id]
    return '', 204

# 自定义响应头
@app.route('/api/status')
def get_status():
    response = make_response(jsonify({'status': 'ok'}))
    response.headers['X-Custom-Header'] = 'Custom Value'
    return response
```

### 下午项目实战（2小时）
扩展博客API的CRUD操作：

```python
# 更新博客文章
@app.route('/api/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    if not request.is_json:
        return {'error': 'Content-Type must be application/json'}, 415
    
    data = request.get_json()
    post = next((post for post in posts if post['id'] == post_id), None)
    
    if post is None:
        return {'error': 'Post not found'}, 404
    
    post.update({
        'title': data.get('title', post['title']),
        'content': data.get('content', post['content']),
        'author': data.get('author', post['author'])
    })
    
    return jsonify(post)
```

## 第3-4天：数据库集成（SQLAlchemy）
### 第3天上午：数据库配置（2小时）
#### SQLAlchemy设置
```python
# 安装依赖
# pip install flask-sqlalchemy

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# 定义模型
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'author': self.author,
            'created_at': self.created_at.isoformat()
        }
```

### 第3天下午：数据库操作（2小时）
#### CRUD操作实现
```python
# 创建文章
@app.route('/api/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    
    new_post = Post(
        title=data['title'],
        content=data['content'],
        author=data['author']
    )
    
    db.session.add(new_post)
    db.session.commit()
    
    return jsonify(new_post.to_dict()), 201

# 获取文章列表
@app.route('/api/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    return jsonify([post.to_dict() for post in posts])
```

### 第4天：高级数据库操作（4小时）
#### 查询和过滤
```python
# 分页
@app.route('/api/posts')
def get_posts():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    
    pagination = Post.query.order_by(Post.created_at.desc()).paginate(
        page=page, per_page=per_page, error_out=False)
    
    return jsonify({
        'posts': [post.to_dict() for post in pagination.items],
        'total': pagination.total,
        'pages': pagination.pages,
        'current_page': pagination.page
    })

# 搜索
@app.route('/api/posts/search')
def search_posts():
    query = request.args.get('q', '')
    posts = Post.query.filter(
        Post.title.ilike(f'%{query}%') | 
        Post.content.ilike(f'%{query}%')
    ).all()
    return jsonify([post.to_dict() for post in posts])
```

## 第5-6天：用户认证
### 第5天：基础认证（4小时）
#### 用户模型和密码加密
```python
# pip install flask-login werkzeug

from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
```

#### 注册和登录API
```python
@app.route('/api/auth/register', methods=['POST'])
def register():
    data = request.get_json()
    
    if User.query.filter_by(username=data['username']).first():
        return {'error': 'Username already exists'}, 400
    
    user = User(username=data['username'], email=data['email'])
    user.set_password(data['password'])
    
    db.session.add(user)
    db.session.commit()
    
    return {'message': 'User registered successfully'}, 201

@app.route('/api/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    
    if user and user.check_password(data['password']):
        return {'access_token': 'dummy_token'}, 200
    
    return {'error': 'Invalid credentials'}, 401
```

### 第6天：JWT认证（4小时）
#### JWT实现
```python
# pip install flask-jwt-extended

from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)

app.config['JWT_SECRET_KEY'] = 'your-secret-key'
jwt = JWTManager(app)

@app.route('/api/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    
    if user and user.check_password(data['password']):
        access_token = create_access_token(identity=user.id)
        return {'access_token': access_token}, 200
    
    return {'error': 'Invalid credentials'}, 401

@app.route('/api/posts', methods=['POST'])
@jwt_required()
def create_post():
    current_user_id = get_jwt_identity()
    # ... 创建文章逻辑
```

## 第7天：项目整合与API文档
### 上午：项目结构优化（2小时）
#### 项目结构
```plain
blog/
├── app/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── post.py
│   │   └── user.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   └── posts.py
│   └── utils/
│       └── __init__.py
├── config.py
├── requirements.txt
└── run.py
```

### 下午：API文档编写（2小时）
#### API文档示例
```python
"""
Blog API Documentation

Base URL: /api

Authentication:
POST /auth/register
    Request: {
        "username": "string",
        "email": "string",
        "password": "string"
    }
    Response: {
        "message": "User registered successfully"
    }

POST /auth/login
    Request: {
        "username": "string",
        "password": "string"
    }
    Response: {
        "access_token": "string"
    }

Blog Posts:
GET /posts
    Query Parameters:
        - page: int
        - per_page: int
    Response: {
        "posts": [...],
        "total": int,
        "pages": int,
        "current_page": int
    }

POST /posts
    Headers:
        Authorization: Bearer <token>
    Request: {
        "title": "string",
        "content": "string"
    }
    Response: {
        "id": int,
        "title": "string",
        "content": "string",
        "author": "string",
        "created_at": "string"
    }
"""
```

## 本周项目成果
完整的博客API系统，包含：

1. 用户认证（注册、登录）
2. 文章CRUD操作
3. 数据库集成
4. API文档

## 学习建议
1. 多参考Flask官方文档
2. 使用Postman测试API
3. 注重代码组织结构
4. 重视错误处理和参数验证

## 扩展学习
1. Flask-RESTful扩展
2. Flask-Migrate数据库迁移
3. Flask-CORS处理跨域
4. 单元测试编写

## 检验标准
+ 理解RESTful API设计原则
+ 掌握Flask框架基础用法
+ 能够实现基本的用户认证
+ 理解数据库ORM操作

# 第三周详细学习计划：进阶Web开发
## 学习目标
掌握进阶Web开发技术，包括RESTful API设计、文件处理、数据库进阶操作，并完成图片分享平台的开发。

## 第1-2天：RESTful API设计与规范
### 第1天上午：API设计理论（2小时）
#### RESTful API设计原则
1. 资源命名规范

```python
# 好的实践
@app.route('/api/users', methods=['GET'])         # 获取用户列表
@app.route('/api/users/<int:user_id>', methods=['GET'])  # 获取单个用户
@app.route('/api/users/<int:user_id>/posts', methods=['GET'])  # 获取用户的文章

# 避免的实践
@app.route('/api/getUsers', methods=['GET'])      # 避免动词
@app.route('/api/user_posts/<int:user_id>', methods=['GET'])  # 避免下划线
```

2. HTTP方法使用规范

```python
# CRUD操作映射
@app.route('/api/posts', methods=['POST'])        # 创建资源
@app.route('/api/posts/<int:id>', methods=['GET'])     # 读取资源
@app.route('/api/posts/<int:id>', methods=['PUT'])     # 更新资源
@app.route('/api/posts/<int:id>', methods=['DELETE'])  # 删除资源
```

### 第1天下午：状态码和错误处理（2小时）
#### 统一错误处理
```python
from flask import jsonify

class APIError(Exception):
    def __init__(self, message, status_code=400, payload=None):
        super().__init__()
        self.message = message
        self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        rv['status'] = 'error'
        return rv

@app.errorhandler(APIError)
def handle_api_error(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

# 使用示例
@app.route('/api/posts/<int:id>')
def get_post(id):
    post = Post.query.get(id)
    if not post:
        raise APIError('Post not found', status_code=404)
    return jsonify(post.to_dict())
```

### 第2天：API版本控制与文档（4小时）
#### API版本控制
```python
from functools import wraps

def api_version(version):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            return f(*args, **kwargs)
        return wrapper
    return decorator

@app.route('/api/v1/users')
@api_version('v1')
def get_users_v1():
    # V1版本的实现
    pass

@app.route('/api/v2/users')
@api_version('v2')
def get_users_v2():
    # V2版本的实现
    pass
```

## 第3-4天：文件上传与处理
### 第3天：基础文件处理（4小时）
#### 文件上传配置
```python
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/api/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        raise APIError('No file part')
    
    file = request.files['file']
    if file.filename == '':
        raise APIError('No selected file')
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        return jsonify({
            'message': 'File uploaded successfully',
            'filename': filename
        })
```

### 第4天：图片处理（4小时）
#### 图片处理功能
```python
# pip install Pillow
from PIL import Image

def create_thumbnail(image_path, size=(200, 200)):
    with Image.open(image_path) as img:
        img.thumbnail(size)
        thumb_path = f"thumbnails/{os.path.basename(image_path)}"
        img.save(thumb_path)
        return thumb_path

@app.route('/api/images', methods=['POST'])
def upload_image():
    file = request.files['image']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        # 创建缩略图
        thumb_path = create_thumbnail(file_path)
        
        return jsonify({
            'original': filename,
            'thumbnail': os.path.basename(thumb_path)
        })
```

## 第5天：数据库高级操作
### 上午：关系模型设计（2小时）
#### 模型关系定义
```python
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    liked_posts = db.relationship(
        'Post',
        secondary='likes',
        backref=db.backref('liked_by', lazy='dynamic')
    )

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(200), nullable=False)
    caption = db.Column(db.String(500))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    comments = db.relationship('Comment', backref='post', lazy='dynamic')

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
```

### 下午：高级查询操作（2小时）
#### 复杂查询示例
```python
# 获取用户的所有帖子和评论数
@app.route('/api/users/<int:user_id>/posts')
def get_user_posts(user_id):
    posts = Post.query\
        .filter_by(user_id=user_id)\
        .outerjoin(Comment)\
        .add_columns(func.count(Comment.id).label('comment_count'))\
        .group_by(Post.id)\
        .all()
    
    return jsonify([{
        'post': post.Post.to_dict(),
        'comment_count': post.comment_count
    } for post in posts])

# 获取热门帖子
@app.route('/api/posts/trending')
def get_trending_posts():
    return Post.query\
        .join(Comment)\
        .group_by(Post.id)\
        .order_by(func.count(Comment.id).desc())\
        .limit(10)\
        .all()
```

## 第6天：中间件开发
### 上午：自定义中间件（2小时）
#### 请求计时中间件
```python
import time
from functools import wraps

def timing_middleware():
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            response = f(*args, **kwargs)
            duration = time.time() - start_time
            
            # 添加响应头
            if isinstance(response, tuple):
                response[0].headers['X-Response-Time'] = str(duration)
            else:
                response.headers['X-Response-Time'] = str(duration)
            
            return response
        return wrapper
    return decorator
```

#### 用户认证中间件
```python
def auth_required():
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            auth_header = request.headers.get('Authorization')
            if not auth_header:
                raise APIError('No authorization header', status_code=401)
            
            try:
                token = auth_header.split(' ')[1]
                # 验证token
                user = verify_token(token)
                if not user:
                    raise APIError('Invalid token', status_code=401)
                
                # 将用户信息添加到g对象
                g.user = user
                return f(*args, **kwargs)
            except Exception as e:
                raise APIError('Authentication failed', status_code=401)
        
        return wrapper
    return decorator
```

### 下午：安全中间件（2小时）
#### CORS和安全头设置
```python
from flask_cors import CORS
from flask_talisman import Talisman

# CORS配置
CORS(app, resources={
    r"/api/*": {
        "origins": ["http://localhost:3000"],
        "methods": ["GET", "POST", "PUT", "DELETE"],
        "allow_headers": ["Content-Type", "Authorization"]
    }
})

# 安全头设置
Talisman(app,
    force_https=True,
    content_security_policy={
        'default-src': "'self'",
        'img-src': ['*', 'data:'],
        'script-src': ["'self'"],
    }
)
```

## 第7天：项目整合
### 上午：图片分享平台核心功能实现（2小时）
#### 完整的帖子创建流程
```python
@app.route('/api/posts', methods=['POST'])
@auth_required()
def create_post():
    # 文件上传处理
    if 'image' not in request.files:
        raise APIError('No image file')
    
    image = request.files['image']
    if not allowed_file(image.filename):
        raise APIError('Invalid file type')
    
    # 保存图片
    filename = secure_filename(image.filename)
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    image.save(image_path)
    
    # 创建缩略图
    thumb_path = create_thumbnail(image_path)
    
    # 创建帖子
    data = request.form
    post = Post(
        image_url=filename,
        thumbnail_url=os.path.basename(thumb_path),
        caption=data.get('caption', ''),
        user_id=g.user.id
    )
    
    db.session.add(post)
    db.session.commit()
    
    return jsonify(post.to_dict()), 201
```

### 下午：项目优化和文档（2小时）
#### 性能优化
```python
# 缓存装饰器
from functools import wraps
from flask_caching import Cache

cache = Cache(app, config={'CACHE_TYPE': 'simple'})

def cached(timeout=5 * 60, key_prefix='view/%s'):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            cache_key = key_prefix % request.path
            rv = cache.get(cache_key)
            if rv is not None:
                return rv
            rv = f(*args, **kwargs)
            cache.set(cache_key, rv, timeout=timeout)
            return rv
        return decorated_function
    return decorator

# 使用缓存
@app.route('/api/posts/trending')
@cached(timeout=300)
def get_trending_posts():
    # ... 获取热门帖子的逻辑
```

## 本周项目成果
完整的图片分享平台，包含：

1. 图片上传和处理
2. 用户关注系统
3. 点赞和评论功能
4. 性能优化
5. API文档

## 学习建议
1. 重视代码复用和模块化
2. 注意性能优化
3. 做好错误处理
4. 编写完整的API文档

## 扩展学习
1. 图片CDN集成
2. 消息队列处理
3. WebSocket实时通知
4. 搜索功能实现

## 检验标准
+ RESTful API设计规范应用
+ 文件上传处理能力
+ 数据库关系模型设计
+ 中间件开发能力
+ 性能优化意识

# 第四周详细学习计划：生产环境和优化
## 学习目标
通过本周学习，掌握FastAPI框架、异步编程、性能优化和生产环境部署，实现一个具备实时通信功能的聊天系统。

## 第1-2天：FastAPI基础与实践
### 上午学习内容（2小时）
#### FastAPI核心概念
1. FastAPI特性
    - 基于Python 3.6+类型注解
    - 异步支持
    - 自动API文档
    - 依赖注入系统
2. 基础功能
    - 路由系统
    - 请求和响应模型
    - 路径参数和查询参数
    - 请求体验证
    - 响应模型
3. Pydantic模型
    - 数据验证
    - 模型嵌套
    - 字段类型
    - 自定义验证器

### 下午学习内容（2小时）
#### FastAPI进阶特性
1. 依赖注入
    - 依赖函数
    - 类作为依赖项
    - 子依赖
    - 全局依赖
2. WebSocket支持
    - WebSocket端点
    - 连接管理
    - 消息处理
    - 错误处理

### 实践项目
使用FastAPI重构基础的WebSocket聊天服务器。

## 第3-4天：异步编程与Redis集成
### 上午学习内容（2小时）
#### asyncio异步编程
1. 异步编程基础
    - async/await语法
    - 事件循环
    - Tasks和Futures
    - 异步上下文管理器
2. FastAPI中的异步操作
    - 异步路由处理
    - 异步依赖
    - 后台任务
    - 长轮询实现

### 下午学习内容（2小时）
#### Redis应用
1. Redis基础操作
    - 数据类型和操作
    - 事务处理
    - 发布/订阅模式
    - 过期策略
2. FastAPI与Redis集成
    - aioredis使用
    - 缓存实现
    - 会话管理
    - 消息队列

### 实践项目
实现聊天系统的消息缓存和实时通知功能。

## 第5天：日志和监控
### 上午学习内容（2小时）
#### 日志系统
1. FastAPI日志配置
    - 日志级别
    - 日志格式化
    - 日志处理器
    - 中间件日志
2. 日志最佳实践
    - 结构化日志
    - 日志轮转
    - 错误追踪
    - 日志聚合

### 下午学习内容（2小时）
#### 系统监控
1. FastAPI应用监控
    - 性能指标
    - 请求追踪
    - 资源使用监控
    - 健康检查接口
2. 监控工具
    - FastAPI内置监控
    - Prometheus集成
    - Grafana面板
    - 告警配置

### 实践项目
为聊天系统添加完整的日志和监控功能。

## 第6-7天：Docker容器化与部署
### 上午学习内容（2小时）
#### Docker基础
1. 容器基础
    - 镜像和容器
    - Dockerfile编写
    - 容器生命周期
    - 数据卷管理
2. Docker Compose
    - 服务编排
    - 网络配置
    - 环境变量
    - 多容器管理

### 下午学习内容（2小时）
#### 部署实践
1. FastAPI应用部署
    - Uvicorn配置
    - Nginx反向代理
    - SSL证书配置
    - 负载均衡
2. 生产环境优化
    - 性能调优
    - 安全配置
    - 错误处理
    - 日志管理

### 实践项目
完成聊天系统的容器化和生产环境部署。

## 周末项目：FastAPI实时聊天系统
### 核心功能
1. 用户系统
    - JWT认证
    - 用户管理
    - 权限控制
    - 会话管理
2. 实时通信
    - WebSocket消息处理
    - 群聊功能
    - 私聊功能
    - 在线状态管理
3. 数据处理
    - 消息持久化
    - Redis缓存
    - 离线消息
    - 消息历史
4. 系统功能
    - 文件上传
    - 消息通知
    - 用户搜索
    - 表情支持

### 技术架构
1. 后端服务
    - FastAPI应用服务器
    - Redis缓存层
    - PostgreSQL数据库
    - Nginx反向代理
2. 部署架构
    - Docker容器
    - Docker Compose
    - 监控系统
    - 日志管理

### 项目检验标准
1. 功能完整性
    - API完整性
    - WebSocket稳定性
    - 数据一致性
    - 错误处理
2. 性能指标
    - 响应时间<100ms
    - WebSocket延迟<50ms
    - 支持1000+并发连接
    - 内存使用优化
3. 部署要求
    - Docker容器化
    - 环境配置
    - 日志收集
    - 监控告警

## 额外学习资源
1. 官方文档
    - FastAPI文档
    - asyncio文档
    - Redis文档
    - Docker文档
2. 工具和框架
    - Pydantic
    - aioredis
    - SQLAlchemy async
    - Uvicorn
3. 示例项目
    - FastAPI官方示例
    - 实时聊天应用
    - Docker部署示例
    - Redis最佳实践

## 注意事项
1. 关注FastAPI的异步特性
2. 重视WebSocket性能优化
3. 保证数据一致性
4. 注意安全性配置
5. 做好错误处理
6. 重视代码可维护性

