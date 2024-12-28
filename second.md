# Python后端开发第二周详细学习计划：Web框架基础

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
```
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
- 理解RESTful API设计原则
- 掌握Flask框架基础用法
- 能够实现基本的用户认证
- 理解数据库ORM操作