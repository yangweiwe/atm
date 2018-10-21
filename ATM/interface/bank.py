from  lib import common
from db import  db_handler
# 定义日志
get_logger0=common.get_logger('转账')
get_logger1=common.get_logger('取钱')
get_logger2=common.get_logger('还钱')




# 拿到余额
def get_account(name):
    account=db_handler.select_file(name)
    return account['account']

# 还款
def repay_account(name,account):
    user_account=db_handler.select_file(name)
    user_account['account']+=account
    db_handler.update_file(user_account)
    get_logger2.info('%s还钱%s'%(name,account))

# 取款
def withdraw_account(name,account):
    user_account = db_handler.select_file(name)
    user_account['account'] -= account*1.05
    db_handler.update_file(user_account)
    get_logger1.info('%s取钱%s'%(name,account))

# 转账
def transfer_interface(form_name,to_name,account):
    from_account = db_handler.select_file(form_name)
    to_account=db_handler.select_file(to_name)
    from_account['account']-=account
    from_account['ls'].append('%s 向%s 转钱%s'%(form_name,to_name,account))
    to_account['account'] += account
    to_account['ls'].append('%s 收到%s 转钱%s' % (to_name,form_name,account))
    db_handler.update_file(from_account)
    db_handler.update_file(to_account)
    get_logger0.info('%s 向%s 转钱%s'%(form_name,to_name,account))
    get_logger0.info('%s 收到%s 转钱%s' % (to_name,form_name,account))

# 查看流水
def look_ls(name):
    user_bank = db_handler.select_file(name)
    return user_bank['ls']