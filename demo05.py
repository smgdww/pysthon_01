# 类变量
class Students():
    name = "张三"
    grade = "5年纪"

    def study(self):
        print("{}年级的学生{}正在学习".format(self.name,self.grade))

# 调用的时候有两种方法:

# 1.使用类名去调用
print(Students.name)
print(Students.grade)

print("="*20)

# 2.使用实例化对象去调用
s1 = Students()
print(s1.name)
print(s1.grade)


# 实例变量:实例变量可以放在不同的方法中,以“self.变量名”的方式定义的变量，
# 但如果放在a方法中但是要通过b方法打印，就必须先执行a方法，
# 再使用b方法。但这样不方便，通常放在构造变量中(会被自动调用。 def __init__():)

# 局部变量:只能在对应的方法中调用。

# 封装:当类中的部分数据不愿意被外界使用时，就可以把类的部分方法和属性隐藏掉,可以使用一个或者两个下划线。
# 但可以设置方法和属性。
class Students1(object):
    __score = ""

    def set_score(self, score):
        self.__score = score

    def get_score(self):
        return self.__score
s = Students1()
s.set_score(76)
s.__score = 65 #不会设置生效
print(s.get_score())


print("="*20)

# 继承:1.必须具有父子关系，有父类和子类。2.在子类中可以使用父类中的方法(功能)或这属性(数据)
class People():
    age = 0

    def eat(self,peope_tpye):
        print(peope_tpye,"在吃饭")

class Students2(People):  # 把父类的类名写入到子类中
    pass  # 代表空实现，必须要有

class Teacher(People):    # 把父类的类名写入到子类中
    pass  # 代表空实现，必须要有

s = Students2()
s.eat("学生")
Students2.age = 15
print(Students2.age)

s = Teacher()
s.eat("老师")
Teacher.age = 45
print(Teacher.age)


# 多肽:1.必须是继承关系。2.子类中的方法覆盖了父类的方法。
# 继承和多肽的区别：
# 子类直接调用父类的方法:继承
# 子类覆盖父类的方法:多肽






