from fastapi import Request
from fastapi.responses import JSONResponse
from typing import Callable
import traceback


async def response_middleware(request: Request, call_next: Callable):
    try:
        # 执行请求
        response = await call_next(request)

        # 如果是 JSONResponse，修改其结构
        if isinstance(response, JSONResponse):
            content = response.body.decode()
            # 已经是标准格式的不处理
            if isinstance(content, dict) and "code" in content:
                return response

            return JSONResponse(
                content={
                    "code": 200,
                    "msg": "成功",
                    "data": response.body
                },
                status_code=response.status_code
            )

        return response
    except Exception as e:
        # 捕获所有异常并返回统一错误格式
        error_msg = str(e)
        print(f'error_msg: {error_msg}')
        traceback.print_exc()
        return JSONResponse(
            content={
                "code": 999,
                "msg": error_msg,
                "data": None  # python的None/False/True-> json的null/false/true
                # "data": {}  # 想保持一致, 可以返回空对象
            },
            status_code=500
        )
