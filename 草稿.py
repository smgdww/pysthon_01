

# 2.定义从文件中读取数据，并返回的是列表的形式
def form_file_get_data(file_name):
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

if __name__ == '__main__':
    result = form_file_get_data("test.txt")