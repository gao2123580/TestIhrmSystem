# 导包
import requests
import unittest
import logging
from app import init_logging

# 定义测试类
class TestLogin(unittest.TestCase):
    # 初始化
    def setUp(self):
        # 定义登录url
        self.login_url = "http://182.92.81.159/api/sys/login"
        # 定义添加员工url
        self.emp_url = "http://182.92.81.159" + "/api/sys/user"

        # 调用 app.py 日志配置函数并初始化
        init_logging()

    def tearDown(self):
        pass

    def test_login_emp(self):
        # 1.定义请求头
        Headers = {"Content-Type": "application/json"}
        # 定义请求数据
        json = {"mobile": "13800000002","password": "123456"}
        # 发送登录请求
        response = requests.post(self.login_url,json=json,headers=Headers)
        # 获取返回的json数据
        result = response.json()
        # print("登录的结果为：",result)
        logging.info(f"登录返回的结果：{result}")
        # 提取令牌
        token = result.get("data")
        # 打印返回的令牌
        logging.info(f"返回的令牌:{token}")

        # 2.定义请求头并拼接
        Headers = {"Content-Type":"application/json","Authorization":"Bearer " + token}
        # 打印请求头信息
        logging.info(f"请求头信息:{Headers}")
        # 提取数据
        jsonData ={
                "username":"爱因斯奥托曼打怪兽",
                "mobile":"14585555555",
                "timeOfEntry":"2020-03-16",
                "formOfEmployment":2,
                "departmentName":"snowsnow",
                "departmentId":"1226092852421177344",
                "correctionTime":"2020-03-15T16:00:00.000Z"
        }
        # 发送添加员工请求数据
        response = requests.post(self.emp_url,json=jsonData,headers=Headers)
        # 获取返回的json数据
        result = response.json()
        logging.info(f"打印添加员工响应数据：{result}")
        # 获取员工的id
        emp_id = result.get("data").get("id")
        # 打印获取员工的id
        logging.info(f"获取员工的id:{emp_id}")

        # 3.拼接查询的员工的url
        query_emp = self.emp_url + "/" + emp_id
        # 打印查询员工的路径
        logging.info(f"查询员工的url:{query_emp}")
        # 发送查询请求
        response = requests.get(query_emp,headers=Headers)
        # 获取返回的json数据
        query_result = response.json()
        # 打印查询返回的响应体
        logging.info(f"查询返回的响应体：{query_result}")

        # 4.拼接修改员工的url
        modify_emp = self.emp_url + "/" + emp_id
        # 打印修改员工的路径
        logging.info(f"打印修改员工:{modify_emp}")
        # 发送修改请求
        response = requests.put(modify_emp,json={"usernsme":"我是你的超级英雄呀"},headers=Headers)
        # 获取返回的json数据
        modify_result = response.json()
        # 打印返回修改请求响应体
        logging.info(f"修改请求响应体：{modify_result}")

        # 5.拼接删除员工的url
        delete_emp = self.emp_url + "/" + emp_id
        # 打印删除员工的路径
        logging.info(f"删除员工的路径{delete_emp}")
        # 发送删除请求
        response = requests.delete(delete_emp,headers=Headers)
        # 获取返回的数据
        delete_result = response.json()
        # 打印删除的结果
        logging.info(f"删除的结果:{delete_result}")









