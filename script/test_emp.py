# 导包
import unittest
import app
import logging
import requests
from api.login import LoginApi
from utils import assert_utils
# 定义测试类
class TestEmp(unittest.TestCase):

    # 初始化
    def setUp(self):
        #实例化登录接口对象
        self.login_api = LoginApi()
        # 提取查询接口的url
        self.emp_url = "http://182.92.81.159" + "/api/sys/user"
        # 实例化
        # self.test_as = TestAs()


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
        headers = {"Content-Type":"application/json","Authorization":"Bearer " +token}
        # 打印请求头 用日志打印必须使用格式化输出
        logging.info(f"请求头部数据为:{headers}")


        # 2.添加员工接口请求
        response = requests.post(self.emp_url,json={
                "username": "我是你的超级abf",
                "mobile": "14587333330",
                "timeOfEntry": "2020-03-16",
                "formOfEmployment": 2,
                "departmentName": "snowsnow",
                "departmentId": "1226092852421177344",
                "correctionTime": "2020-03-15T16:00:00.000Z"
                }, headers=headers)
        # 打印添加员工的结果
        logging.info(f"添加员工的结果为：{response.json()}")
        # 获取添加员工返回的json数据
        add_result = response.json()
        logging.info(f"添加员工返回的json数据:{add_result}")
        # # 提取员工的id
        emp_id = add_result.get("data").get("id")
        # # 打印获取员工的id
        logging.info(f"获取员工的id为：{emp_id}")
        # 断言
        assert_utils(self,response, 200, True, 10000, "操作成功")

        # # 3.拼接查询员工接口
        quer_emp_url = self.emp_url + "/" +  emp_id
        # # 打印拼接员工接口url
        logging.info(f"拼接员工接口url:{quer_emp_url}")
        # # 发送查询接口请求
        response = requests.get(quer_emp_url,headers=headers)
        # # 查询员工的结果
        logging.info(f"查询员工的结果为：{response.json()}")
        # 断言
        assert_utils(self,response, 200, True, 10000, "操作成功")

        # # 4.把员工id拼接url组成修改所需要的url
        modify_emp_url = self.emp_url + "/" + emp_id
        # 打印拼接修改的url
        logging.info(f"拼接修改的url:{modify_emp_url}")
        # 发送修改员工接口的请求
        response = requests.put(modify_emp_url,json={"username":"tome"},headers=headers)
        # 打印修改员工返回的结果
        logging.info(f"修改员工返回的结果：{response.json()}")
        # 断言
        assert_utils(self,response, 200, True, 10000, "操作成功")

        # # 5.把员工id拼接url组成删除所需要的url
        delete_emp_url = self.emp_url + "/" + emp_id
        # 打印删除所需要的url
        logging.info(f"删除所需要的url:{delete_emp_url}")
        # 发送删除员工id请求
        response = requests.delete(delete_emp_url,headers=headers)
        # 打印删除响应结果
        logging.info(f"删除响应结果:{response.json()}")
        # 断言
        assert_utils(self,response, 200, True, 10000, "操作成功")