from fastapi import FastAPI, HTTPException
from typing import Dict, Any
import json
import random
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 配置CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有来源
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有方法
    allow_headers=["*"],  # 允许所有头
)

def randomize_zeros(data: Any) -> Any:
    """将数据中的0值替换为随机数"""
    if isinstance(data, dict):
        return {k: randomize_zeros(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [randomize_zeros(x) for x in data]
    elif isinstance(data, (int, float)) and data == 0:
        return random.randint(1, 1000)
    elif isinstance(data, str) and data.strip() in ['0', '00', '0.0']:
        return str(random.randint(1, 1000))
    return data

@app.get("/api/demo")
async def get_random_demo() -> Dict:
    """
    获取随机化后的demo数据
    返回: JSON格式的随机化demo数据
    """
    try:
        # 读取原始JSON文件
        with open('demo.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # 随机化处理
        randomized_data = randomize_zeros(data)
        
        return randomized_data
        
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Demo file not found")
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Invalid JSON format in demo file")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 健康检查接口
@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8200)