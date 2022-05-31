#1. 输入a,b,c,d4个整数，计算a+b-c*d的结果
a = 1
b = 6
c = 10
d = 3
print(a + b - c*d)

# 2. 打印1~100内被3整除的所有数的和 。
sum = 0
for x in range(0,101,1):
    if x%3 !=0:
        continue
    sum += x
print(sum)

# 3. 使用range()输出1~10内的所有奇数 。
for x in range(1,11,2):
    print(x)

# 4. 打印1~100所有偶数的和 减去 所有奇数的和 的值
a = 0
sum1 = 0
b = 1
sum2 = 0
while a <= 100 and b<= 100:
    sum1 += a
    a += 2
    sum2 += b
    b += 2
print(sum1-sum2)

# 5. 求1+2+3+...+100的和
a = 1
sum = 0
while a <= 100:
    sum += a
    a += 1
print(sum)

# 6. 判断一个数n能同时被3和5整除
a = 15
print(a % 3 == 0 and a % 5 == 0)

# 7. 定义一个整数变量，判断该变量值是否是1-100内的某个数，如果是打印出来
a = 15
if 1 <= a <= 100:
    print(a)

# 8. 输入三个整数x,y,z，请把这三个数由小到大输出。备注：输入方法：input()
x,y,z = map(int,input("输入三个整数:").split(","))
lst1 = [x,y,z]
lst1.sort()
print(lst1)

# 9. 利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。备注：需要使用input()方法
a = int(input("你的成绩是:"))
if 60 <= a <= 89:
    print("B")
elif  a >= 90:
    print("A")
else:
    print("C")

# 10. 将一个列表的数据复制到另一个列表中。
lst1 = [1,2,3,6]
lst2 = [4,7,8,9]
lst3 = lst1.copy()
print(lst1)
print(lst2)
print(lst3)

# 11. 输出 9*9 乘法口诀表。




# 12. 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。




# 13. 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。





# 14. 题目：打印出如下图案（菱形）:
