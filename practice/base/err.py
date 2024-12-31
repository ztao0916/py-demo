# 错误处理
# 语法: try except finally
# try:
#     print('try...')
#     r = 10 / 0
#     print('result:', r)
# except ZeroDivisionError as e:  # ZeroDivisionError 是 Exception 的子类,表示除以0的错误
#     print('except:', e)
# finally:
#     print('finally...')
# print('END')


# try:
#     print('try...')
#     r = 10 / int('a')
#     print('result:', r)
# except ValueError as e:  # ValueError 是 Exception 的子类,表示输入的值错误
#     print('ValueError:', e)
# except ZeroDivisionError as e:  # ZeroDivisionError 是 Exception 的子类,表示除以0的错误
#     print('ZeroDivisionError:', e)
# finally:  # 无论是否发生异常,finally 都会执行
#     print('finally...')
# print('END')

# import logging


# def foo(s):
#     return 10/int(s)


# def bar(s):
#     return foo(s)*2


# def main():
#     try:
#         bar('0')
#     except Exception as e:
#         logging.exception(e)


# main()
# print('END')  # 程序打印完错误信息后,会继续执行,不阻塞代码运行

# 抛出错误:语法 raise Errorclass(error_info)

# 实践:找出以下程序的错误,并优化
from functools import reduce  # 内置高阶函数,累加器,语法: reduce(function, iterable)


def str2num(s):  # 定义一个字符串转数字的函数
    return int(s)


def calc(exp):  # 定义一个计算表达式的函数
    ss = exp.split('+')  # 将表达式按+分割成字符串列表
    ns = map(str2num, ss)  # 将字符串列表转换为数字列表
    return reduce(lambda acc, x: acc + x, ns)  # 将数字列表累加


def main():
    try:
        r = calc('100 + 200 + 345')
        print('100 + 200 + 345 =', r)
        r = calc('99 + 88 + 7.6')  # 抛出异常的原因: 7.6是浮点型,使用int的时候会报错
        print('99 + 88 + 7.6 =', r)
    except Exception as e:
        print('Error:', e)


main()
