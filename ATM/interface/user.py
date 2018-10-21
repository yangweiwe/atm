from db import db_handler

# 查询用户接口
def get_userinfo_interface(name):
    return db_handler.select_file(name)

# 注册用接口
def register_interface(name, pwd,account):
    user_dict = {'name':name,'pwd':pwd,'account':account,'credit':account,'locked':False,'ls':[]}
    db_handler.update_file(user_dict)

# 锁定用户
def locked_interface(name):
    user_dict = db_handler.select_file(name)
    user_dict["locked"] = True
    db_handler.update_file(user_dict)