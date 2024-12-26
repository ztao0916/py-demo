# 转义字符串
print('I\'m ok')

# 多行字符串
# print('''line1
# line2
# line3''')

# print(r'''hello,
# world''')

# 布尔值 and,or,not
# print(True or False) #True
print(True and False)  # False
# print(not True) #False
# print(not False) #True
# print(not 1 > 2) #True
# print(f'空值: {None}')
# print(None)

# if语句
# age = int(input('请输入你的年龄:'))
# if age >= 18:
#     print('adult')
# elif age > 12:
#     print('teenager')
# else:
#     print('kid')


# 变量赋值问题
# a = 'ABC'
# b = a
# a = 'XYZ'
# print(b)

# 全部大写的变量名表示常量

# 练习题
# n=123
# f=456.789
# s1= 'hello,world'
# s2='hello,\'adam\''
# s3= r'hello,"bart"' #r表示原生字符串，不转义
# s4 = r'''hello,
# Lisa!'''
# print(f's2, {s2}')
# print(f's3, {s3}')
# print(f's4, {s4}')

# tuple-元祖(指向不可变) list-列表(指向可变)
# L = [
#     ['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', 'Ruby', 'PHP'],
#     ['Adam', 'Bart', 'Bob']
# ]
# 打印Apple
# print(L[0][0])
# 打印Python
# print(L[1][1])
# 打印Bob
# print(L[2][2])

# height = float(input('请输入��高:'))
# weight = float(input('请输入体重:'))
# # BMI计算公式
# bmi = weight / (height * height)
# if bmi < 18.5:
#     print('过轻')
# elif bmi < 25:
#     print('正常')
# elif bmi < 28:
#     print('过重')
# else:
#     print('肥胖')


# match-case可以理解成switch-case,代替if-elif-else
# score = input('请输入分数:')
# match score:
#     case 'A':
#         print('优秀')
#     case 'B':
#         print('良好')
#     case 'C':
#         print('及格')
#     case 'D':
#         print('不及格')
#     case _: #_表示默认值
#         print(f'输入值: {score}')

# 复杂匹配,可以理解成数学表达式
# score = int(input('请输入分数:'))  # 将输入转换为整数
# match score:
#     case x if x > 90:
#         print('优秀')
#     case x if x > 60:
#         print('及格')
#     case _:
#         print('不及格')

# args = ['gcc', 'hello.c', 'world.c']
# args = ['clean']
# args = ['gccdd']

# match args:
#     # 如果仅出现gcc，报错:
#     case ['gcc']:
#         print('gcc: missing source file(s).')
#     # 出现gcc，且至少指定了一个文件:
#     case ['gcc', file1, *files]:
#         print('gcc compile: ' + file1 + ', ' + ', '.join(files))
#     # 仅出现clean:
#     case ['clean']:
#         print('clean')
#     case _:
#         print('invalid command.')

# for循环-求和
# sum = 0
# numList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for num in numList:
#     sum += num
# print(f'1到10的和: {sum}')
# for循环求和-1到1000,range(1,1000)表示1到999
# sum = 0
# for i in range(1, 1001):
#     sum += i
# print(f'for循环求和1到1000的和: {sum}')

# while循环求和1到1000
# sum = 0
# i = 1000
# while i >= 1:
#     sum += i
#     i -= 1
# print(f'while循环求和1到1000的和: {sum}')

# 循环打印 hello,xxx
L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print(f'hello, {name}')


# dict-字典--理解成js的map
# set-集合(数学集合)--理解成js的set
a = 'abc'
print(a.replace('a', 'A'))
print(a)
