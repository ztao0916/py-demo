# Python后端开发第三周详细学习计划：进阶Web开发

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
- RESTful API设计规范应用
- 文件上传处理能力
- 数据库关系模型设计
- 中间件开发能力
- 性能优化意识