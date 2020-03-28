# 导包
import unittest
import app
import time

from script.test_emp02 import TestEmp
from script.test_login_parameterized import TestLogin
from HTMLTestRunner_PY3 import HTMLTestRunner
# 创建测试套件
suite = unittest.TestSuite()
# 把测试用添加到测试套件中
suite.addTest(unittest.makeSuite(TestLogin))
suite.addTest(unittest.makeSuite(TestEmp))
# 获取时间戳
# time = time.strftime("%Y%m%d_%H%M%S")
# 设置测试报告路径，调用app里工的FILENAME
report = app.FILENAME + "/report/ihrm_{}.html".format(time.strftime("%Y%m%d_%H%M%S"))

# 使用 HTMLTestRunner_PY3 生成测试报告
with open(report,"wb")as f:
    # 实例化测试报告
    runner = HTMLTestRunner(f,verbosity=1,
                            title="ihrm人力资源管理系统",
                            description="使用HTMLTestRunner_PY3生成测试报告")

    # 使用实例化的htmltestrunner运行测试套件
    runner.run(suite)