import os,sys
from core import src
# 拿到启动文件的绝对路径
path = os.path.dirname(os.path.dirname(__file__))
# 项目根目录加入到环境变量中
sys.path.append(path)

if __name__ == '__main__':
    src.run()