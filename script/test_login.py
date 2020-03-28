# 导包
import unittest
from api.login import LoginApi
import logging
from utils import assert_utils
import app
# 定义测试类
class TestLogin(unittest.TestCase):

    # 初始化
    def setUp(self):
        # 实例化登录的Api类
       self.login_api = LoginApi()

    def tearDown(self):
        pass

    # 编写测试用例
    # 登录成功
    def test01_login_succeed(self):

        # 定义登录成功需要的请求体
        jsonData = {"mobile":"13800000002","password":"123456"}
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
        assert_utils(self,response,200,True,10000,"操作成功")
    # 密码错误
    def test02_pwd_error(self):
        # 定义登录请求体数据
        jsonData = {"mobile":"13800000002","password":"12345678"}
        # 定义请求头
        # Headers = {"Content-Type":"application/json"}
        # 利用封装的登录接口，发送请求体。测试ihrm系统
        response = self.login_api.login(jsonData,app.Headers)
        # 利用日志打印登录响应的结果 必须导入 import logging
        logging.info(f"登录响应的结果:{response.json()}")
        # 断言 响应码 success、code、message
        assert_utils(self,response,200,False,20001,"用户名或密码错误")

    # 账号不存在
    def test03_mobile_is_not_exists(self):
        # 定义登录请求体数据
        jsonData = {"mobile": "13900000002", "password": "123456"}
        # 定义请求头
        # Headers = {"Content-Type": "application/json"}
        # 利用封装的登录接口，发送请求体。测试ihrm系统
        response = self.login_api.login(jsonData, app.Headers)
        # 利用日志打印登录响应的结果 必须导入 import logging
        logging.info(f"登录响应的结果:{response.json()}")
        # 断言 响应码 success、code、message
        assert_utils(self, response, 200, False, 20001, "用户名或密码错误")

    #  # 输入的手机号码有英文字符
    def test04_mobile_english_str(self):
        # 定义登录请求体数据
        jsonData = {"mobile": "138000000AS", "password": "123456"}
        # 定义请求头
        # Headers = {"Content-Type": "application/json"}
        # 利用封装的登录接口，发送请求体。测试ihrm系统
        response = self.login_api.login(jsonData, app.Headers)
        # 利用日志打印登录响应的结果 必须导入 import logging
        logging.info(f"登录响应的结果:{response.json()}")
        # 断言 响应码 success、code、message
        assert_utils(self, response, 200, False, 20001, "用户名或密码错误")
    # 手机号码有特殊字符
    def test05_mobile_specific_symbol(self):
        # 定义登录请求体数据
        jsonData = {"mobile": "1380000#&00", "password": "123456"}
        # 定义请求头
        # Headers = {"Content-Type": "application/json"}
        # 利用封装的登录接口，发送请求体。测试ihrm系统
        response = self.login_api.login(jsonData, app.Headers)
        # 利用日志打印登录响应的结果 必须导入 import logging
        logging.info(f"登录响应的结果:{response.json()}")
        # 断言 响应码 success、code、message
        assert_utils(self, response, 200, False, 20001, "用户名或密码错误")

    # 手机号码为空(bug)
    def test06_mobile_null(self):
        # 定义登录请求体数据
        jsonData = {"mobile": "", "password": "123456"}
        # 定义请求头
        Headers = {"Content-Type": "application/json"}
        # 利用封装的登录接口，发送请求体。测试ihrm系统
        response = self.login_api.login(jsonData, app.Headers)
        # 利用日志打印登录响应的结果 必须导入 import logging
        logging.info(f"登录响应的结果:{response.json()}")
        # 断言 响应码 success、code、message
        assert_utils(response, 200, False, 20001, "用户名或密码错误")

    # 密码为空
    def test07_pwd_null(self):
        # 定义登录需要的请求体
        jsonData = {"mobile": "13800000002", "password": ""}
        # 定义请求头
        # Headers = {"Content-Type": "application/json"}
        # 利用封装的登录接口，发送请求体。测试ihrm系统
        response = self.login_api.login(jsonData, app.Headers)
        # 利用日志打印登录响应的结果 必须导入 import logging
        logging.info(f"登录响应的结果:{response.json()}")
        # 断言 响应码 success、code、message
        assert_utils(self, response, 200,False, 20001, "用户名或密码错误")

    # 多参-多出1个参数
    def test08_more_parameter(self):
        # 定义登录需要的请求体
        jsonData = {"mobile": "13800000002", "password": "123456","sign":"123"}
        # 定义请求头
        # Headers = {"Content-Type": "application/json"}
        # 利用封装的登录接口，发送请求体。测试ihrm系统
        response = self.login_api.login(jsonData, app.Headers)
        # 利用日志打印登录响应的结果 必须导入 import logging
        logging.info(f"登录响应的结果:{response.json()}")
        # 断言 响应码 success、code、message
        assert_utils(self, response, 200, True, 10000, "操作成功")

    # 少参 - 缺少mobile
    def test09_lack_mobile(self):
        # 定义登录需要的请求体
        jsonData = {"password": "123456"}
        # 定义请求头
        # Headers = {"Content-Type": "application/json"}
        # 利用封装的登录接口，发送请求体。测试ihrm系统
        response = self.login_api.login(jsonData, app.Headers)
        # 利用日志打印登录响应的结果 必须导入 import logging
        logging.info(f"登录响应的结果:{response.json()}")
        # 断言 响应码 success、code、message
        assert_utils(self, response, 200, False, 20001, "用户名或密码错误")

    # 少参 - 缺少password
    def test10_lack_pwd(self):
        # 定义登录需要的请求体
        jsonData = {"password": "123456"}
        # 定义请求头
        # Headers = {"Content-Type": "application/json"}
        # 利用封装的登录接口，发送请求体。测试ihrm系统
        response = self.login_api.login(jsonData, app.Headers)
        # 利用日志打印登录响应的结果 必须导入 import logging
        logging.info(f"登录响应的结果:{response.json()}")
        # 断言 响应码 success、code、message
        assert_utils(self, response, 200, False, 20001, "用户名或密码错误")

    # 无参数
    def test11_not_parameter(self):
        # 定义登录需要的请求体
        jsonData = None
        # 定义请求头
        # Headers = {"Content-Type": "application/json"}
        # 利用封装的登录接口，发送请求体。测试ihrm系统
        response = self.login_api.login(jsonData, app.Headers)
        # 利用日志打印登录响应的结果 必须导入 import logging
        logging.info(f"登录响应的结果:{response.json()}")
        # 断言 响应码 success、code、message
        assert_utils(self, response, 200, False, 99999, "抱歉，系统繁忙，请稍后重试")

    # 错误的参数
    def test12_error_parameter(self):
        # 定义登录成功需要的请求体
        jsonData = {"mb": "13800000002", "password": "123456"}
        # 定义请求头
        # Headers = {"Content-Type": "application/json"}
        # 利用封装的登录接口，发送请求体。测试ihrm系统
        response = self.login_api.login(jsonData, app.Headers)
        # 利用日志打印登录响应的结果 必须导入 import logging
        logging.info(f"登录响应的结果:{response.json()}")
        # 断言 响应码 success、code、message
        assert_utils(self, response, 200, False, 20001, "用户名或密码错误")