from typing import Any


def success_response(data: Any = None) -> dict:
    return {
        "code": 200,
        "msg": "成功",
        "data": data
    }


def error_response(msg: str = "失败") -> dict:
    return {
        "code": 999,
        "msg": msg,
        "data": None
    }
