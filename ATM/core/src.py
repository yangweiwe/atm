
session_dict = {
    "name": None,
    "is_login":False
}

def login():
    pass

def register():
    if session_dict["is_login"]:
        print("is login")
        return

    while True:
        name = input("please input your name>>:").strip()
        # 判断用户是否纯在


def check_balance():
    pass

def transfer():
    pass

def repay():
    pass

def withdraw():
    pass

def check_records():
    pass

def shopping():
    pass

def check_shopping_cart():
    pass



func_dic={
    '1':login,
    '2':register,
    '3':check_balance,
    '4':transfer,
    '5':repay,
    '6':withdraw,
    '7':check_records,
    '8':shopping,
    '9':check_shopping_cart
}
def run():
    while True:
        print(
            '''
                    1、登录
                    2、注册
                    3、查看余额
                    4、转账
                    5、还款
                    6、取款
                    7、查看流水
                    8、购物
                    9、查看购买商品

            '''
        )

        choice=input('please choice>>:').strip()
        if choice not in func_dic:continue
        func_dic[choice]()
