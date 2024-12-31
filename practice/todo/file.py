# 文件读写
# 文件写入: 语法: with open(文件名, 模式, 编码)
# 模式: w 写入, a 追加, r 读取, rb 读取二进制文件
# 编码: utf-8 等
# with 语句: 自动管理文件的关闭和打开, 语法: with open(文件名, 模式, 编码) as 文件对象:
# 写入一个test.txt文件
with open('test.txt', 'w', encoding='utf-8') as f:
    f.write('hello, world!')  # write方法写入
    print('写入成功')

# 文件读取,read方法
with open('test.txt', 'r', encoding='utf-8') as f:
    content = f.read()  # read方法读取
    print(content)

# 给test.txt文件追加内容
with open('test.txt', 'a', encoding='utf-8') as file:
    file.write('\nhello, python!')  # 追加内容,并换行
    print('追加成功')


# json处理
import json

data = {'name': '张三', 'age': 18}

# 将python数据转换为json字符串
json_str = json.dumps(data, ensure_ascii=False)
print(json_str, type(json_str))

# 将json字符串转换为python数据
data = json.loads(json_str)
print(data, type(data))

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False)
    print('写入json文件成功')

# 读取json文件
with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)  # load方法读取json文件
    print(data, type(data))
