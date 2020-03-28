# 导包
import logging
import os
from logging import handlers

# 定义 登录数据的路径
FILENAME = os.path.dirname(os.path.abspath(__file__))
# 定义公共的请求头全局变量
Headers = {"Content-Type":"application/json"}
# 定义全局变量 查询id
EMP_ID = ""

# 编写初始化日志配置函数
def init_logging():
    # 创建日志器
    logger = logging.getLogger()
    # 设置日志等级
    logger.setLevel(logging.INFO)
    # 创建控制台处理器
    sh = logging.StreamHandler()
    # 创建文件处理器
    filename = os.path.dirname(os.path.abspath(__file__)) + f"/log/ihrm.log"
    fh = logging.handlers.TimedRotatingFileHandler(filename,
                                                   when = "m",
                                                   interval=1,
                                                   backupCount=3,
                                                   encoding="utf-8")
    # 创建格式化器
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt)
    # 将格式化器添加到处理器当中
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    # 将处理器添加到日志器当中
    logger.addHandler(sh)
    logger.addHandler(fh)

if __name__ == '__main__':
    # 调用初始化日志函数
    init_logging()
    # 初始化日志之后，利用logging来打印日志
    logging.info("test ----------测试日志打印--------")