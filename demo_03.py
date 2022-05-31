# 字符串格式化
my_str = "my name is %s" % ("张三")
print(my_str)

# 格式化整数
my_str1 = "张三 今年 %d 岁" % (99)
print(my_str1)

# 格式化浮点数(小数)
my_str2 = "一斤苹果 %f 元" % (25)
print(my_str2)

# 辅助指令 : m:代表总长度， n:代表保留的小数位数
my_str3 = "一斤苹果 %12.3f 元" % (6.895)
print(my_str3)

# 辅助指令 : - 左对齐
my_str4 = "一斤苹果 %-12.3f 元" % (6.895)
print(my_str4)

# 辅助指令 : + 显示正数
my_str4 = "一斤苹果 %+6.3f 元" % (6.895)
print(my_str4)

# 辅助指令 : 0 用0代替空格
my_str5 = "一斤苹果 %06.3f 元" % (6.895)
print(my_str5)

# 使用format取格式化
my_str6 = "张三 今年 {} 岁" .format(25)
print(my_str6)

# 使用format传多个参数:前面和后面是对应关系
my_str7 = "今天星期{}，张三买了{}斤苹果".format('一',9)
print(my_str7)

# 1.连接字符串
astr = "+"
bstr = astr.join("456")
print(bstr)

# 2.分割字符串
cstr = "123,555,999"
dstr = cstr.split(",")
print(dstr)

# 3.查找字符串，返回最小索引，没有返回-1，index没有会报错
estr = "helloworld"
print(estr.find("l"))
print(estr.find("x"))
print(estr.index("l"))

# 查找以xxx结尾的字符串,对的返回True，错的返回False
fstr = "123456789"
print(fstr.endswith("9"))

# 查找以xxx开头的字符串，对的返回True，错的返回False
fstr = "123456789"
print(fstr.startswith("1"))

# 替换字符串
gstr = "helloworld"
hstr = gstr.replace("hello","fuck")
print(hstr)

# 序列的索引,正向数从0开始，反向数从-1开始，列表，元组，字符串都能使用
a = [56,"wode",999]
print(a[1])
print(a[-2])

# 序列的切片,第一个代表起始索引的位置，默认为0（包括该位置），第二个代表结束的索引位置（不包括该位置），默认为序列中数据的总数，
# 第三个代表步长，默认为1，不为1则是跳着取数。列表，元组，字符串都能使用。切片可以省略任意两个，就走默认值

b = ['red','green','blue','black','gold','orange']
print(b[0:5:1])
print(b[1:6:2])
print(b[:5:])
print(b[2:])
print(b[2::])
print(b[::2])

# 序列的相加，相乘 +:表示将一个序列的所有值添加到另一个序列中（在末尾） *:表示将一个序列中的所有数据翻倍.
# 注意:只能列表加入列表，字符串加入字符串，元组加入元组.列表，元组，字符串都能使用
c = [1,2]
d = [3,4]
print(d+c)
print(c * 2)

# 序列的检查元素 in 判断元素是否在序列中，在返回True,不在返回False.列表，元组，字符串都能使用
e = ['red','green','blue','black','gold','orange']
print('red' in e)
print('ww' in e)









