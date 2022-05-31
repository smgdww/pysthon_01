
## 需求-迭代1：登录功能
# 1. 定义两条用户数据 ，要求用户数据的属性包括用户角色，用户账号，密码，部门
# 2. 要求返回的格式是字典形式 ，包含两个字段，code和message ,code为0代表成功，为1代表失败 ；message给出相应的提示 ，格式如 ：{'code':0,'message':'登录成功'}
# 3. 用户通过控制台输入用户名和密码，判断用户名和密码是否和定义数据中的用户名密码相匹配，若匹配返回成功登录消息体，并把用户列表也追加到返回结果中,{'code':0,'message':'登录成功',user_list:[]}
# 4. 若用户名输入为空或密码输入为空，都给出对应的提示，如用户名不能为空
# 5. 若用户名或密码不匹配，都给出登录失败，请检查您的用户名或密码是否填写正确。提示

user_list = [{'role':'admin','account':'admin','password':'123456','dept':'tester'},{'role':'user','account':'dev','password':'1234567','dept':'dev'}]
a = input("请输入用户名:")
b = input("请输入密码:")
def login():
    for x in user_list:
        if a == x.get('account') and b == x.get('password'):
            return {'code': 0, 'message': '登录成功'}, x

        elif a == x.get('account') and len(b) == 0:
            return {'code': 1, 'message': '登录失败'},"密码不能为空"

        elif b == x.get('password') and len(a) == 0:
            return {'code': 1, 'message': '登录失败'}, "用户名不能为空"

        elif a == x.get('account') and b != x.get('password'):
            return {'code': 1, 'message': '登录失败'},"请检查您的用户名或密码是否填写正确"

        elif a != x.get('account') and b == x.get('password'):
            return {'code': 1, 'message': '登录失败'},"请检查您的用户名或密码是否填写正确"

        #elif a != x.get('account') and b != x.get('password'):
         #   return {'code': 1, 'message': '登录失败'}, "请检查您的用户名或密码是否填写正确"    (为什么加上这条if语句输入dev用户名和它对应的密码后结果不正确，但输入admin用户名和它对应的密码后结果又是正确)

        elif len(a) == 0 and len(b) != 0:
            return {'code': 1, 'message': '登录失败'}, "用户名不能为空"

        elif len(a) != 0 and len(b) == 0:
            return {'code': 1, 'message': '登录失败'}, "密码不能为空"


print(login())


input("请输入查寻的账号:")