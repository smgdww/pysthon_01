# 条件语句
"""
单条件判断
"""
a = 9
b = 10
if a > b:
    print("yes")
else:
    print("no")

"""
多条件判断
"""
score = 65
if score > 90:
    print("优秀")
elif score > 80:
    print("良")
elif score > 60:
    print("及格")
else:
    print("不及格")

if 60 < score < 80:
    print("价格")


if None:
    print("yes")


# for循环
for x in "abcdefg":
    print(x)



# while循环
a = 1
while a <= 5:
    print(a)
    a += 1

a = 1
sum = 0
while a <= 100:
    sum += a
    a += 1
print(sum)

# range
for x in range(1,10,2):
    print(x)


for x in range(1,11,1):
    if x == 7:
        continue
    print(x)

# 列表
alst = []
blst = [56,5.6,"yes",True]
print(alst)
print(blst)

for x in blst:
    print(x)



dlst = [12,13,56,78,78]
elst = [66,89]

dlst.append(99)
print(dlst)

print(dlst.count(78))

dlst.extend(elst)
print(dlst)

print(dlst.index(78))

dlst.insert(1,99)
print(dlst)

dlst.reverse()
print(dlst)

dlst.sort()
print(dlst)

dlst.pop()
print(dlst)

for x in range(1,11,1):
    print(x)

for x in range(2,11,2):
    print(x)

for x in range(2,11,2):
    if x%2!=0:
        continue
    print(x)





flst = (12,True,12.3,"yes")
print(flst)



