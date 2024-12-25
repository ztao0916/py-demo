import json
import random
from datetime import datetime

def randomize_zeros(data):
    if isinstance(data, dict):
        return {k: randomize_zeros(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [randomize_zeros(x) for x in data]
    elif isinstance(data, (int, float)) and data == 0:
        return random.randint(1, 1000)
    elif isinstance(data, str) and data.strip() in ['0', '00', '0.0']:
        return str(random.randint(1, 1000))
    return data

# 读取原始JSON
with open('demo.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 随机化处理
randomized_data = randomize_zeros(data)

# 生成带时间戳的文件名
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
output_filename = f'demo_random_{timestamp}.json'

# 保存到新文件
with open(output_filename, 'w', encoding='utf-8') as f:
    json.dump(randomized_data, f, indent=2, ensure_ascii=False)

print(f'已生成随机数据并保存到文件: {output_filename}')