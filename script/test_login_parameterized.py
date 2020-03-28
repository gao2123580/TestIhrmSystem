# 导包
import unittest
from api.login import LoginApi
import logging
from utils import assert_utils, read_login_data
import app
from parameterized import parameterized
# 定义测试类
class TestLogin(unittest.TestCase):

    # 初始化
    def setUp(self):
        # 实例化登录的Api类
       self.login_api = LoginApi()

    def tearDown(self):
        pass

    # 定义加载登录数据文件的路径 引入app定义的路径
    filename = app.FILENAME + "/data/login.json"
    # 参数化
    @parameterized.expand(read_login_data(filename))
    # 编写测试用例
    # 登录成功
    def test01_login(self,case_name,jsonData,http_code,succeed,code,messsge):

        # 定义登录成功需要的请求体
        # jsonData = {"mobile":"13800000002","password":"123456"}
        # 定义请求头
        # Headers = {"Content-Type":"application/json"}
        # 利用封装的登录接口，发送请求体。测试ihrm系统  调用app页面的全局变量app.Headers
        response = self.login_api.login(jsonData,app.Headers)
        # 利用日志打印登录响应的结果 必须导入 import logging
        logging.info(f"登录响应的结果:{response.json()}")
        # 断言 响应码 success、code、message
        # self.assertEqual(200,response.status_code)
        # self.assertEqual(True,response.json().get("success"))
        # self.assertEqual(10000,response.json().get("code"))
        # self.assertIn("操作成功",response.json().get("message"))
        assert_utils(self,response,http_code,succeed,code,messsge)
