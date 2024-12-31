# 模块和包的使用
# 常用的内置模块
# 1. os模块,语法: import os
# os模块是python内置的模块,提供了丰富的方法用于处理文件和目录
import time
import sys
import os
# 获取当前工作目录
print(f'当前工作目录: {os.getcwd()}')
# 获取当前工作目录的文件列表
print(f'当前工作目录的文件列表: {os.listdir()}')
# 判断当前目录下是否有txt文件
print(f'当前目录下是否有txt文件: {os.path.exists("test.txt")}')

# 2. sys模块,语法: import sys
# sys模块是python内置的模块,提供了一系列有关python运行环境的变量和函数
# 获取python解释器的版本信息
print(f'python解释器的版本信息: {sys.version}')
# 获取python解释器的路径
print(f'python解释器的路径: {sys.executable}')

# 3. time模块,语法: import time
# time模块是python内置的模块,提供了一系列有关时间的函数
# 获取当前时间戳
print(f'当前时间戳: {time.time()}')
# 获取当前时间
print(f'当前时间: {time.localtime()}')
# 格式化时间
print(f'格式化时间: {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}')
