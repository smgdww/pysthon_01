"""
需求-迭代1：登录功能
1. 定义两条用户数据 ，要求用户数据的属性包括用户角色，用户账号，密码，部门
2. 要求返回的格式是字典形式 ，包含两个字段，code和message ,code为0代表成功，为1代表失败 ；message给出相应的提示 ，格式如 ：{'code':0,'message':'登录成功'}
3. 用户通过控制台输入用户名和密码，判断用户名和密码是否和定义数据中的用户名密码相匹配，若匹配返回成功登录消息体，并把用户列表也追加到返回结果中,{'code':0,'message':'登录成功',user_list:[]}
4. 若用户名输入为空或密码输入为空，都给出对应的提示，如用户名不能为空
5. 若用户名或密码不匹配，都给出登录失败，请检查您的用户名或密码是否填写正确。提示
"""
# 定义从文件中读取数据，并返回的是列表的形式
def from_file_get_data(file_name):
    f = None   # 这一步是为了如果文件没有内容，就不用关闭了
    try:
        f = open(file_name,"r")
        line = f.readline()
        user_data = eval(line)
        return user_data
    except Exception as e:
        print(e)
    finally:
        if not f:
            f.close()

# 定义一个向文件中写入内容，用户添加的信息是在原来的基础上添加的函数
f = None
def save_date(file_name,file_content):
    try:
        f = open(file_name,"w")
        f.write(str(file_content))
    except Exception as e:
        print(e)
    finally:
        if not f:
            f.close()


# 定义默认的用户数据
# user_list = [{'role':'admin','account':'admin','password':'123456','dept':'tester'},{'role':'user','account':'dev','password':'1234567','dept':'dev'}]

"""
值 if 表达式1 else 表达式2
"""

user_list = []
user_list = user_list if user_list else from_file_get_data(r"C:\python36\pysthon_01\作业答案\test.txt")

# 定义默认的返回结果
result = {"code":0,"message":""}

# 定义一个登录功能
def login(username,password):
    # 1.当输入密码或者账号为空的时候
    if username == None or username == "":
        result.update({"code":1,"message":"用户名不能为空!"})
        return result

    if password == None or password == "":
        result.update({"code":1,"message":"密码不能为空!"})
        return result

    # 2.当登录成功的时候
    for user_info in user_list:
        if username == user_info.get("account") and password == user_info.get("password"):
            result.update({"message": "登录成功!","user_list":user_list})
            return result

    # 3.当登录不成功的时候(用户名和密码不匹配)
    result.update({"code":1,"message":"请检查您的用户名或密码是否填写正确!"})
    return result

"""
## 需求-迭代2：用户查询功能:
1. 用户查询功能必须是在登录以后才能调用 ，否则给出权限不足提示
2. 若输入的用户名正确，返回登录用户的信息，password字段不显示。
3. 若输入的用户名不正确 ，给出无查询结果的提示
4. 查询支持模糊查询。
"""


"""
## 需求-迭代3：用户新增功能:
1. 将默认用户数据放在文件中保存，以上迭代功能查询数据都要从文件查询 。
2. 需要对文件的读写进行异常捕获
3. 用户可以输入关键字add进行新增用户 ，新增的用户信息可以保存到文件中 。
4. 同时进行查询时，也能查询出该用户 。
"""



# 4.定义一个用户进行操作的类
class User():


    # 定义用户查询的功能
    def get_user(self,username):

        # 判断用户是否登录，若登录成功可以进行查询。若没有登录成功，返回权限不足
        if result.get("code") != 0:
            result.update({"code":11,"message":"用户未登录，无法查询结果!"})
            return result

        # 输入正确用户名进行查询，返回结果(支持模糊查询)
        result.update({"user_list": []})
        lst = []   # 这个列表代表存放的查询出的结果的数据
        for x in user_list:
            account = x.get("account")
            if username in account:   # in 代表支持模糊查询
                x.pop("password")
                lst.append(x)

        # 判断新列表里的数据，如果不为空，查询成功，返回对应的结果
        if list:
            result.update({"message": "查询用户成功!","user_list":lst})
            return result

        # 输入正确用户名不正确，返回无查询结果提示

        result.update({"code":12,"message":"未查询到用户，请重新输入!"})
        return result

    # 定义用户添加的功能
    def user_add(self,username,password="123456",**kwargs):
        user_dict = {}
        user_dict["account"] = username
        user_dict["password"] = password
        user_dict.update(**kwargs)
        # 将组装的用户数据添加到用户列表中
        user_list.append(user_dict)
        save_date("test.txt",user_list)
        result.update({"message": "添加用户成功"})




if __name__ == '__main__':
    flge = True

# 进行循环以便用户做各种操作

    while flge:
        # 提供用户的各种操作
        vls = input("操作请输入对应编号:\n"
                  "1:)进行登录:\n"
                  "2:)进行查询，请输入用户名:\n"
                  "3:)添加用户，请添加信息:\n"
                  "q:)退出操作:\n"
                  "其他字符：未知操作，请重新输入:")

        # 当输入未知字符后，跳过这次循环，进行再次输入
        if not vls in ("1","2","q","quit","3"):
            print("="*30)
            continue

        # 进行登录操作
        if vls == "1":
            username = input("请输入用户名:")
            password = input("请输入密码:")
            login_result = login(username,password)
            print(login_result)
            print("="*30)
            continue

        # 进行查询操作
        if vls == "2":
            name = input("请输入用户名:")
            user = User()
            get_result = user.get_user(name)
            print(get_result)
            print("="*30)
            continue

        # 进行用户添加操作
        if vls == "3":
            name = input("请输入用户名:")
            user = User()
            get_result = user.get_user(name) # 这步是先判断用户名是否存在
            if 12 == get_result.get("code"):
                password = input("请输入用户密码")
                role = input("请输入用户角色")
                dept = input("请输入用户部门")
                user.user_add(name,password,role=role,dept=dept)
            if 0 == get_result.get("code"):
                result.update({"code":13,"message":"用户已存在，无法添加!"})
                print(result)
            print(get_result)
            print("="*30)


            username = input("请输入用户名:")
            password = input("请输入密码:")
            add_result = user_add()
            print(add_result)
            continue

        # 进行退出操作
        if vls in ("q","quit"):
            flge = False
            print("退出成功!")







