# 面向对象编程
# 可以理解成js中的类,
# 类是抽象的,而实例是具体的
# 语法: class 类名: 类名首字母大写,类名通常是驼峰命名法
# 类中定义的函数称为方法,方法的第一个参数是self,表示实例本身
# 实例化: 创建类的实例,语法: 实例名 = 类名()
# 访问实例属性: 实例名.属性名
# 访问实例方法: 实例名.方法名()
# __init__方法: 初始化方法,在创建实例时自动调用,等价于js的constructor

class Dog:  # 定义一个类
    def __init__(self, name):  # 初始化方法,在创建实例时自动调用
        self.name = name
        # 双下划线__表示私有属性,本质是python解释器改了名字,外部无法访问
        self.__age = 1

    def bark(self):  # 定义一个方法,第一个参数是self,表示实例本身
        print(self.name + '汪汪汪')

    def get_age(self):
        print(f'获取年龄, {self.__age}')
        return self.__age

    def set_age(self, age):
        if age < 0:
            print('年龄不能为负数')
        else:
            self.__age = age

# 子类-拉布拉多


class Labrador(Dog):
    def bark(self):
        print(self.name + '汪汪汪,我是拉布拉多')


# 实例化
dog = Dog('旺财')
labrador = Labrador('拉布拉多')
dog.bark()  # 旺财汪汪汪
dog.set_age(2)
dog.get_age()  # 获取年龄, 2
labrador.bark()  # 拉布拉多汪汪汪,我是拉布拉多
