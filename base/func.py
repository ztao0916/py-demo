# 函数的定义与使用-包括高级特性和函数式编程
# 列表推导式-使用[],在其中包含一个表达式和一个for子句,然后有0个或多个for或if子句
# 练习:L = ['Hello', 'World', 18, 'Apple', None],由于非字符串类型无法调用str.lower()方法,需要过滤非字符串类型
import math
from collections.abc import Iterable
import time
L = ['Hello', 'World', 18, 'Apple', None]
L_lower = [s.lower() for s in L if isinstance(s, str)]
print(f'L_lower:{L_lower}')  # ['hello', 'world', 'apple']
# squares = [n**2 for n in range(2, 8)]
# print(f'squares: {squares}')
# 创建一个3-15之间偶数的平方列表
# even_squares = [n**2 for n in range(3, 16) if n % 2 == 0]
# print(f"even_squares: {even_squares}")

# 函数的定义-使用def关键字
# 定义一个求和函数


def add(x, y):
    return x+y


# print(f'add(3,5):{add(3, 5)}')  # 8

# 空函数,pass语句什么都不做,只是一个占位符,等价于js中的空函数
# function empty_func() {}


def empty_func():
    pass  # 占位符

# 创建一个求绝对值的函数


# def abs_func(x):
#     if x >= 0:
#         return x
#     else:
#         return -x


# print(f'abs_func(-5):{abs_func(-5)}')  # 5

# print(f'abs_func("aaa"):{abs_func("aaa")}')# 报错:TypeError: '>=' not supported between instances of 'str' and 'int'
# 参数类型检查


def abs_func(x):
    # isinstance()函数可以判断一个变量是不是字符串,接收两个参数,第一个是变量,第二个是类型,类型是一个包含多个类型的元组,如果变量是其中的一个类型就返回True
    if not isinstance(x, (int)):
        raise TypeError('错误的参数类型')
    if x >= 0:
        return x
    else:
        return -x


try:
    print(abs_func('A'))
except TypeError as e:
    print(e)

# 返回多个值,可以通过多个变量接收,也可以通过一个变量接收,这个变量是一个元组


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print(f'x:{x},y:{y}')  # x:151.96152422706632,y:130.0
# r = move(100, 100, 60, math.pi / 6)
# print(f'r:{r}')  # r:(151.96152422706632, 130.0)

# 定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程ax^2 + bx + c = 0的两个解


def quadratic(a, b, c):
    # 计算b^2-4ac
    delta = b**2 - 4*a*c
    # 判断delta的正负(负数没有实数解,开根号会报错)
    if delta < 0:
        return '无实数解'
    elif delta == 0:
        return -b/(2*a)
    else:
        x1 = (-b + math.sqrt(delta))/2*a
        x2 = (-b - math.sqrt(delta))/2*a
        return x1, x2


# 测试,通过输入执行
# a, b, c = map(int, input('请输入a,b,c:').split(','))

# print(f'quadratic({a},{b},{c}):{quadratic(a, b, c)}')

# 创建一个简单的通讯录,需要输入姓名和电话号码,然后可以打印姓名和电话
# 通讯录是一个字典,姓名是key,电话是value
contacts = {}

# 添加联系人到通讯录


def add_contact(name, phone):
    contacts[name] = phone

# 获取通讯录中的联系人电话


def get_contact(name):
    return contacts[name]


# name = input('请输入姓名:')
# phone = input('请输入电话:')
# add_contact(name, phone)
# print(f'通讯录:{contacts}')
# name = input('请输入需要查询的姓名:')
# print(f'{name}的电话是:{get_contact(name)}')

# 函数的参数,包括位置参数,默认参数,可变参数,关键字参数,命名关键字参数

# 位置参数,调用函数时,传入的参数按照位置顺序依次赋值给参数


def power2(x):
    return x*x

# 默认参数,调用函数时,如果没有传入参数,使用默认参数;n=2,表示n的默认值是2


def power(x, n=2):
    return x**n


# print(f'默认参数,power(5):{power(5)},n不传默认2')  # 25

# 默认参数的坑:默认参数必须指向不变对象,如果指向可变对象,默认参数会变化
# 默认参数如果是一个list,每次调用都会改变默认参数的值


def add_end(L=[]):
    L.append('END')
    return L


# print(f'默认参数,第一次调用add_end():{add_end()}')  # ['END']
# print(f'默认参数,第二次调用add_end():{add_end()}')  # ['END', 'END']
# print(f'默认参数,第三次调用add_end():{add_end()}')  # ['END', 'END', 'END']
# 默认参数是一个可变对象,每次调用都会改变默认参数的值

# 可变参数,传入的参数个数是可变的,可以是0个,1个,2个等,在参数前面加一个*号,表示可变参数,在调用的时候,传入的参数会被包装成一个tuple


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum += n
    return sum


# 测试
# print(f'可变参数,calc(1,2,3):{calc(1, 2, 3)}')  # 6
# 如果已经有一个list或者tuple,要调用一个可变参数,可以在list或者tuple前面加一个*号,把list或者tuple的元素变成可变参数传进去
nums = [1, 2, 3, 4]
# print(f'可变参数,calc(*nums):{calc(*nums)}')

# 关键字参数,传入的参数是一个dict,在参数前面加两个*号,表示关键字参数,在调用的时候,传入的参数会被包装成一个dict,用key=value的形式传入


def person(name, age, **kw):
    print(f'name:{name},age:{age},other:{kw}')


# person("Michael", 30)
# 新增关键字参数
# person("Bob", 35, city='Beijing')
# 如果是一个dict,可以在dict前面加两个*号,把dict的元素变成关键字参数传进去
extra = {'city': 'Beijing', 'job': 'Engineer'}
# person('Jack', 24, **extra)

# 命名关键字参数,如果要限制关键字参数的名字,可以使用命名关键字参数,在参数前面加一个*,表示命名关键字参数,调用的时候,必须传入参数名字,不能多传入参数或者少传入参数,否则会报错


def person2(name, age, *, city, job):
    print(f'name:{name},age:{age},city:{city},job:{job}')


# 测试
# person2('Jack', 24, city='Beijing', job='Engineer')
# person2('Jack', 24, city='Beijing', job='Engineer',address='Chaoyang')  # 报错,多传入了一个参数,TypeError: person2() got an unexpected keyword argument 'address'

# 参数组合,顺序固定,必须是: 位置参数,默认参数,可变参数,命名关键字参数,关键字参数


def greet(name, greeting="Hello", *args, **kwargs):
    print(f"{greeting}, {name}!")
    if args:
        print("Additional args:", args)
    if kwargs:
        print("Additional kwargs:", kwargs)


# 测试
# greet("Jane")  # 只传入位置参数,默认参数生效
# greet("Jane", "Good morning")  # 传入位置参数和默认参数,默认参数被覆盖
# greet("Jane", "Good morning", 1, 2, 3)  # 传入位置参数,默认参数,可变参数
greet("Jane", "Good morning", 1, 2, 3, x=1, y=2)  # 传入位置参数,默认参数,可变参数,关键字参数
# greet("Jane", "Good morning", x=1, y=2)  # 传入位置参数,默认参数,关键字参数

# 递归函数,包含递归体和终止条件,递归体是函数自己调用自己,终止条件是递归的出口,避免无限递归
# 示例,求阶乘


def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)


# print(f'递归函数,fact(5):{fact(5)}')  # 120

# 使用递归函数实现汉诺塔
# 有三根柱子A,B,C,在A柱子上从上到下按照从小到大的顺序放置n个盘子,现在要把A柱子上的盘子移动到C柱子上,移动的规则是一次只能移动一个盘子,并且大盘子不能放在小盘子上,求移动的步骤,需要记录移动的次数

# 为什么move_count=[0]是一个列表,而不是一个数字?
# 列表是一个可变的数据结构,而字符串是不可变的;这是一个默认参数陷阱


def hanoi(n, a, b, c, move_count=[0]):
    if n == 1:
        print(f'{a}-->{c}')
        move_count[0] += 1
    else:
        hanoi(n-1, a, c, b, move_count)
        print(f'{a}-->{c}')
        move_count[0] += 1
        hanoi(n-1, b, a, c, move_count)
    return move_count


# 测试
# move_count = hanoi(4, 'A', 'B', 'C')
# print(f'移动次数:{move_count}')

# 高级特性-切片
# 切片是对list和tuple的一种操作,可以对list和tuple进行切片操作,获取一部分元素,切片操作是一种取出某一段元素的操作,返回的是一个新的list或者tuple,等价于js中的slice方法,不会改变原有的list或者tuple,基本语法是[start:stop:step]
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# print(f'有索引0,L[0:3]:{L[0:3]}')  # ['Michael', 'Sarah', 'Tracy']
# print(f'省略索引0,L[:3]:{L[:3]}')  # ['Michael', 'Sarah', 'Tracy']
# print(f'不传第二个参数,默认切到最后L[-1:]:{L[-1:]}')  # []

# 实践-取出0,100的list中的前10个元素
L = list(range(101))
# print(f'取前10个数L[:10]:{L[:10]}')  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 前10个数,每2个取1个
# print(f'前10个数,每2个取1个L[:10:2]:{L[:10:2]}')  # [0, 2, 4, 6, 8]
# 元组实践
T = tuple(range(101))
print(f'取前10个数T[:10]:{T[:10]}')  # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# 字符串可以理解成特殊的list,每个元素就是一个字符

# 实践: 利用切片操作,实现一个trim()函数,去除字符串首尾的空格,注意不要调用str的strip()方法


def trim(s):
    if not isinstance(s, str):
        raise TypeError('参数类型错误')
    if s == '':
        return s
    if s[0] == ' ':
        return trim(s[1:])
    if s[-1] == ' ':
        return trim(s[:-1])
    return s


# 测试
# print(f'trim(" hello "):{trim("     hello    ")}')  # hello


# 高级特性-迭代
# 迭代是访问集合元素的一种方式,迭代是一个重复的过程,每一次迭代的过程中,都会取出一个元素,直到没有元素可以取出为止,迭代是通过for...in来完成的,可以迭代list,tuple,dict,set,str等,迭代的过程中,不需要知道集合的内部结构,只需要知道如何取出每一个元素
# 迭代dict,默认情况下,dict迭代的是key,如果要迭代value,可以使用dict.values()方法,如果要同时迭代key和value,可以使用dict.items()方法

# 判断一个对象是否可以迭代,可以使用collections模块的Iterable类型判断

abc = isinstance('abc', Iterable)

# 实战:使用迭代查找list中的最大值和最小值,并返回一个tuple


def find_max_min(L):
    if not isinstance(L, list):
        raise TypeError('请传入一个list')
    if len(L) == 0:
        return (None, None)
    max = L[0]  # 假设第一个元素是最大值
    min = L[0]  # 假设第一个元素是最小值
    for x in L:
        if x > max:
            max = x  # 更新最大值
        if x < min:
            min = x  # 更新最小值
    return (max, min)


# 测试
# max_min = find_max_min(list(range(101)))
# print(f'最大值和最小值:{max_min}')


# 生成器-在循环的过程中不断推算出后续的元素,这样就不必创建完整的list,从而节省大量的空间,生成器是一种特殊的迭代器,可以通过生成器推导式和yield关键字来创建生成器

# 实践-斐波那契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:  # 循环条件
        yield b
        a, b = b, a+b
        n += 1
    return 'done'  # 生成器结束的标志


fib_gen = fib(6)
# print(f'斐波那契数列:{list(fib_gen)}')  # [1, 1, 2, 3, 5, 8]

# 普通函数和生成器函数的区别: 普通函数是顺序执行,遇到return语句或者最后一行函数语句就返回,生成器函数是在每次调用next()方法的时候执行,遇到yield语句返回,再次执行时从上次返回的yield语句处继续执行


def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield (3)
    print('step 3')
    yield (5)


# next(odd()) #始终返回step 1,因为每次调用都是一个新的生成器
o = odd()
next(o)
next(o)
next(o)

# 高阶函数: 函数可以作为参数传入另一个函数,这种函数称为高阶函数,高阶函数可以接收函数作为参数,也可以把函数作为结果返回
# sorted语法: sorted(iterable,key=None,reverse=False),key是一个函数,用来指定排序的key,reverse是一个bool值,用来指定排序的顺序,默认是升序
# map函数: map(function,iterable),将function作用于iterable的每一个元素,返回一个新的list
# reduce函数: reduce(function,iterable),对iterable中的元素进行累积操作,返回一个值
# filter函数: filter(function,iterable),过滤iterable中的元素,返回一个新的list

# 实践: 按名称排序,忽略大小写
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
sorted_result = sorted(L, key=lambda x: x[0].lower())
print(f'按名称排序:{sorted_result}')
# 按成绩排序,由高到底
score_sorted_result = sorted(L, key=lambda x: x[1], reverse=True)
print(f'按成绩排序:{score_sorted_result}')

# 装饰器
# 装饰器是一个返回函数的高阶函数,装饰器的作用是在不改变原函数的情况下,为函数添加新的功能,语法糖@可以简化装饰器的调用

# 定义一个装饰器


# def log(func):
#     def wrapper(*args, **kwargs):
#         func_name = getattr(func, '__name__', 'unknown')
#         print(f'调用函数{func_name}')
#         return func(*args, **kwargs)
#     return wrapper
# 使用@符号调用装饰器


# @log
# def now(*args, **kwargs):
#     print('2021-07-11', args, kwargs)  # 定义函数的时候,才需要加*号,表示可变参数,关键字参数,命名关键字参数


# now(1, 2, 3, x=4, y=5)

# 装饰器实践: 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间

def log_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = round((end_time - start_time)*1000, 4)
        print(f'{func.__name__}执行时间:{execution_time}秒')
        return result
    return wrapper


@log_time
def test1():
    print('test')


test1()


# 偏函数: functools模块提供了一个partial函数,用来创建一个新的函数,这个函数可以固定住原函数的部分参数,从而简化函数的调用
