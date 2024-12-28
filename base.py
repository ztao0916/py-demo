# 变量声明---赋值即声明
x = 1
y = 2
z = 3

# 全局作用域
if x == 1:
    w = 4  # w在if语句块中声明，但是在if语句块外也可以使用


print(f'w={w}')  # 可以访问

# 函数作用域


def func():
    a = 5
    print(f'a={a}')  # 可以访问,只能在函数内访问


# print(f'a={a}')  # 报错，a未定义 = name 'a' is not defined

# python整数没有大小限制
# float和int是不同的类型
print(type(1))  # <class 'int'>
print(type(1.0))  # <class 'float'>

# python对比JavaScript,特有的数据类型
# 1. 元组 tuple 一旦创建就不能修改 用()表示 有序 不可变 有重复元素
# 2. 集合 set 无序 不重复 用{}表示 无索引

# 算数运算符 + - * / // % ** 分别表示 加减乘除 取整 取余 幂运算
# 比较运算符 == != > < >= <= 分别表示 等于 不等于 大于 小于 大于等于 小于等于

print(5/2)  # 2.5 返回浮点数
print(5//2)  # 2 返回整数
print(5 % 2)  # 1 返回余数
print(5**2)  # 25 返回幂运算
print('hello' * 3)  # hellohellohello 字符串可以和数字相乘,js中不可以

# 类型转换 list等价于arry.from()方法,可迭代对象都可以使用list()方法转换为数组
print(f'list({(1, 2, 3)})={list((1, 2, 3))}')  # list((1,2,3))=[1, 2, 3]

# 相等运算符 == 和 is, ==比较值是否相等，is比较对象是否相等
# a = [1, 2, 3]
# b = [1, 2, 3]
# c=a

# print(f'a==b:{a==b}')  # a==b:True
# print(f'a is b:{a is b}')  # a is b:False
# print(f'a is c:{a is c}')  # a is c:True

# 逻辑运算符 and or not
# and 两个条件都为真时返回真 or 两个条件有一个为真时返回真 not 取反
# 逻辑运算符的优先级 not > and > or
# 举例
# a =1
# b=2
# print(a==b and a==1) #False
# print(a==b or a==1) #True
# print(not a==b) #True
# print(not a==b and a==1) #True

# match-case 语句 类似于switch-case语句
# a = 4
# match a:
#     case 1:
#         print(f'a={a}')  # a=1
#     case 2:
#         print(f'a!={a}')  # a!=a
#     case _:
#         print('default')  # default

# match-case 复杂匹配 用|分隔 用_表示默认匹配
a = 4
match a:
    case x if x < 10:  # 定义一个变量x,x和a的值相等
        print(f'x=a={a}')  # a=4
    case _:
        print('default')  # default

# match-case 匹配列表
a = [1, 2]
# 匹配列表的长度
match a:
    case [1]:
        print(f'a={a}')  # a=[1]
    case [1, 2]:
        print(f'a={a}')  # a=[1, 2]
    case [1, 2, 3]:
        print(f'a={a}')  # a=[1, 2, 3]
    case _:
        print('其他情况')  # 其他情况

# 循环语句 for in
# for in 遍历列表 -符合迭代器协议的对象都可以使用for in
num = [1, 2, 3, 4, 5]
for i in num:
    print(f'i={i}')  # i=1 i=2 i=3 i=4 i=5
# list列表操作
# 给num新增数据,append()方法,等价于js数组push()方法
num.append(6)  # [1, 2, 3, 4, 5, 6]
# 删除数据,remove()方法,等价于js数组splice()方法
num.remove(5)  # [1, 2, 3, 4, 6]
# 插入数据,insert()方法,等价于js数组splice()方法
num.insert(0, 0)  # [0, 1, 2, 3, 4, 6]
# 修改数据,等价于js数组splice()方法
num[0] = 1  # [1, 1, 2, 3, 4, 6]
# 查找数据--获取下标,等价于js数组indexOf()方法
print(num.index(6))  # 5
# 拓展列表,extend()方法,等价于js数组concat()方法
num.extend([7, 8])  # [1, 1, 2, 3, 4, 6, 7, 8]
# 切片操作,等价于js数组slice()方法, 返回新列表,不会改变原列表
print(num[0:2])  # [1, 1]
# 字典操作,等价于js对象obj操作
# 创建字典
dict = {'name': 'zhangsan', 'age': 18}
# 获取值
print(dict['name'])  # zhangsan
# 修改值
dict['name'] = 'lisi'
print(dict['name'])  # lisi
# 删除值,有两种方法,del和pop
# del dict['name']  # 删除name键值对,原字典变为{'age':18}
# dict.pop('name')  # 删除name键值对,原字典变为{'age':18}
# 添加值
dict['sex'] = '男'  # 添加新的键值对
print(f'dict={dict}')

# set集合操作,不支持索引,不支持重复元素
# 创建集合
set = {1, 2, 3}
# 添加元素
set.add(4)  # {1, 2, 3, 4}
print(f'添加元素后,set={set}')  # {1, 2, 3, 4}
# 删除元素
set.remove(4)  # {1, 2, 3}
print(f'删除元素后,set={set}')  # {1, 2, 3}
# set结合list进行操作
set1 = {1, 2, 3}
list1 = [4, 5, 6]
# 将list1中的元素添加到set1中
set1.update(list1)  # {1, 2, 3, 4, 5, 6}
print(f'将list1中的元素添加到set1中,set1={set1}')  # {1, 2, 3, 4, 5, 6}
