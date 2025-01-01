from fastapi import FastAPI
from middleware.response import response_middleware
from utils.response import success_response, error_response

# 创建 FastAPI 应用实例
app = FastAPI()

# 注册全局中间件，用于统一处理响应格式
app.middleware("http")(response_middleware)


@app.get('/')  # 路由装饰器，处理 GET 请求
def read_books():
    """
    获取书籍列表接口
    返回: 
    {
        "code": 200,
        "msg": "成功",
        "data": {
            "books": []
        }
    }
    """
    return success_response({'books': []})


@app.get('/error')
def test_error():
    """
    测试错误响应接口
    返回:
    {
        "code": 999,
        "msg": "自定义错误消息",
        "data": null
    }
    """
    return error_response("自定义错误消息")


@app.get('/exception')
def test_exception():
    """
    测试异常处理接口
    抛出异常后会被中间件捕获并格式化为统一响应:
    {
        "code": 999,
        "msg": "这是一个异常",
        "data": null
    }
    """
    raise ValueError("这是一个异常")
