import json,os
from conf import setting

# 定义查看数据函数
def select_file(name):
    """
    :param name:文件名字 默认为用户名
    :return: 返回json数据 用户信息
    """
    # 拼接需要查找文件的路径
    db_path = os.path.join(setting.BASE_DB,f"{name}.json")
    # 如果存在
    if os.path.exists(db_path):
        with open(db_path,"r",encoding="utf8") as f:
            return json.load(f)
    return False

# 定义用来更新数据的函数
def update_file(user_dict):
    """
    :param user_dict: 调用函数之前查到的用户信息
    :return:
    """
    db_path = os.path.join(setting.BASE_DB, f"{user_dict['name']}.json")
    with open(db_path, 'w', encoding='utf-8')as f:
        json.dump(user_dict, f)
        f.flush()