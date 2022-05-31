# 函数的定义:def 函数名(参数列表):函数体.参数列表可以有多个，且参数可以是多种形式
def add(x,y):
    z = x + y
    return z


# 函数的调用：函数名(对应的参数)。调用函数时，输入的具体参数必须与定义函数时对应。
print(add(6,8))


# return:返回的结果可以是计算的值，也可以是表达式,且可以返回多个结果.如果不写就会默认返回None
def add1(x,y):
    return x + y
print(add1(6,8))


# 函数:位置参数:调用函数时，输入的具体参数必须与定义函数时一一对应.多或少都会报错
def add2(x,y):
    return x + y
print(add2(6,8))
print(add2("hello","world"))
# print(add2(1,3,5))  # 会报错
# print(add2(5)) # 会报错


# 函数:关键字参数:调用函数时，输入的具体参数顺序不用与定义函数时对应，以key=value调用。也可以
# 与位置参数连用，但必须先使用位置参数,否则会报错。
def student_lesson(grade,subject):
    z = "{}年级上{}课".format(grade,subject)
    return z
print(student_lesson(grade=2,subject="语文"))
print(student_lesson(subject="语文",grade=2))


# 函数:默认参数:其中某个参数会有默认值，不写就会执行默认值，带有默认值的参数必须放在最后面.
def study_language(name,language='python'):
    info = ("{}要学习{}语言".format(name,language))
    return info
print(study_language("王五","java"))
print(study_language("李四","python"))
print(study_language("张三"))


# 函数:可变参数:其中某个参数会有变化，以*args来表示，可以有列表和字典的形式
def add(x,y,*args):
    print(args)
    z = x + y + sum(args)
    return z
print(add(3,4))
print(add(3,4,5))
print(add(3,4,5,6,7,8))   # 传递多个参数

# 以列表的方式传递多个参数，但列表前必须要加上*号表示可变
print(add(3,4,*[5,6,7,8]))

# 以字典的方式传递多个参数，必须以key=value的形式。
def show_info(**kwargs):
    print(kwargs)

print(show_info(a = "张三",b = "李四",c = 123))
# 可以传入字典，但在前面都需要加上两个*
dt_date = {"x":1,"y":2,"z":3}
print(show_info(**dt_date))


# 面向对象
# 实例: 创建学生类，要求有属性：姓名和年级 ; 方法有：学习的方法，打印学生的上课情况
class Students():  # 定义一个类(是一个大的类，如汽车，电梯等)
    # 定义了类里面的属性(可以理解为参数或者变量)
    name = ""
    grade = ""

    # 定义了类里面的方法(可以理解为函数)
    def study(self):
        print("{}年级的学生{}正在学习".format(self.name,self.grade))

s1 = Students()
s1.name = "张三"
s1.grade = 5
print(s1.study())
s1.study()

s2 = Students()
s2.name = "李四"
s2.grade = 4
s2.study()









