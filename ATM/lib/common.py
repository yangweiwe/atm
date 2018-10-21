from core import src
import logging.config
from conf import setting

# 验证是否登录装饰器
def login_auth(func):
    def inter(*args, **kwargs):
        if not src.session_dict["is_login"]:
            print("please login")
            src.login()
        return func(*args, **kwargs)
    return inter

# 日志函数
def get_logger(name):
    logging.config.dictConfig(setting.LOGGING_DIC)
    logger = logging.getLogger(name)
    return logger