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
