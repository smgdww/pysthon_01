## 需求-迭代2：用户查询功能:
1. 用户查询功能必须是在登录以后才能调用 ，否则给出权限不足提示
2. 若输入的用户名正确，返回登录用户的信息，password字段不显示。
3. 若输入的用户名不正确 ，给出无查询结果的提示
4. 查询支持模糊查询。



## 需求-迭代3：用户新增功能:
1. 将默认用户数据放在文件中保存，以上迭代功能查询数据都要从文件查询 。
2. 需要对文件的读写进行异常捕获
3. 用户可以输入关键字add进行新增用户 ，新增的用户信息可以保存到文件中 。
4. 同时进行查询时，也能查询出该用户 。
