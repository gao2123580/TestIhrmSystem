# 导包
import unittest
import app
import logging
import pymysql
import requests
from api.emp import EmpApi
from api.login import LoginApi
from utils import assert_utils, emp_data
from parameterized import parameterized
# 定义测试类
class TestEmp(unittest.TestCase):

    # 初始化
    def setUp(self):
        #实例化登录接口对象
        self.login_api = LoginApi()
        # 提取查询接口的url
        self.emp_url = "http://182.92.81.159" + "/api/sys/user"
        #实例化员工模块类
        self.emp_id = EmpApi()
    def tearDown(self):
        pass

    # 编写测试员工增删改查案例
    def test01_emp_login_succeed(self):
        # 1. 登录成功接口请求
        response = self.login_api.login({"mobile":"13800000002","password":"123456"},headers=app.Headers)
        # 获取返回的json 数据
        result = response.json()
        # 利用日志打印登录接口返回的响应的数据  用日志打印必须使用格式化输出
        logging.info(f"员工模块登录的响应结果为：{result}")
        # 提取令牌
        token = result.get("data")
        # 设置请求头部数据
        app.Headers = {"Content-Type":"application/json","Authorization":"Bearer " +token}
        # 打印请求头 用日志打印必须使用格式化输出
        logging.info(f"请求头部数据为:{app.Headers}")
        # 断言
        assert_utils(self, response, 200, True, 10000, "操作成功")

    # 员工模块数据路径
    filename = app.FILENAME + "/data/emp.json"
    # 参数化
    @parameterized.expand(emp_data(filename, "add_emp"))
    # 2.添加员工接口请求
    def test02_add_emp(self,username,mobile,http_code,success,code,message):
        response = self.emp_id.add_emp(username,mobile,app.Headers)
        # 打印添加员工的结果
        logging.info(f"添加员工的结果为：{response.json()}")
        # 获取添加员工返回的json数据
        add_result = response.json()
        logging.info(f"添加员工返回的json数据:{add_result}")
        # 提取员工的id
        app.EMP_ID = add_result.get("data").get("id")
        # 打印获取员工的id
        logging.info(f"获取员工的id为：{app.EMP_ID}")
        # 断言
        assert_utils(self, response,http_code,success,code,message)


    # 参数化
    @parameterized.expand(emp_data(filename,"qury_emp"))
    # 3.拼接查询员工接口
    def test03_quer_emp(self,http_code,success,code,message):
        # 发送查询接口请求 调用查询员工id
        response = self.emp_id.quer_emp(app.EMP_ID,headers=app.Headers)
        # 查询员工的结果
        logging.info(f"查询员工的结果为：{response.json()}")
        # 断言
        assert_utils(self, response,http_code,success,code,message)

    # 参数化
    @parameterized.expand(emp_data(filename, "modify_emp"))
    def test04_modify_emp(self,username,http_code,success,code,message):
        # 发送修改员工接口的请求
        response = self.emp_id.modify_emp(app.EMP_ID,username,headers=app.Headers)
        # 打印修改员工返回的结果
        logging.info(f"修改员工返回的结果：{response.json()}")
        # 建立数据库连接
        conn = pymysql.connect(host="182.92.81.159", user="readuser", password="iHRM_user_2019", database="ihrm")
        # 获取游标
        cursor = conn.cursor()
        # 执行查询的sql语句
        sql = f"select username from bs_user where id={app.EMP_ID}"
        # 输出sql语句
        logging.info(f"打印sql语句{sql}")
        cursor.execute(sql)
        # 调试执行到位sql结果
        result = cursor.fetchone()
        logging.info(f"执行sql语句查询的结果为{result}")
        # 关闭游标
        cursor.close()
        # 关闭连接
        conn.close()
        # 断言数据库查询结果
        self.assertEqual(username,result[0])
        # 断言
        assert_utils(self, response,http_code,success,code,message)
    # 参数化
    @parameterized.expand(emp_data(filename, "delete_emp"))
    def test05_delete_emp(self,http_code,success,code,message):
        # 发送删除员工id请求
        response = self.emp_id.delete_emp(app.EMP_ID,headers=app.Headers)
        # 打印删除响应结果
        logging.info(f"删除响应结果:{response.json()}")
        # 断言
        assert_utils(self, response,http_code, success, code,message)