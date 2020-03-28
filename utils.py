# 封装断言

# 导入json模块
import json
import os
import unittest
# class TestAs(unittest.TestCase): #断言是重unittest.TestCase里继承的
def assert_utils(self,response,sta_code,success,code,message):
    """
     response,sta_code,success,code,message
     传入形参 在script目录下的test_login里面
     调用这个assert_utils函数传入实参

    """
    # 状态响应码
    self.assertEqual(sta_code,response.status_code)
    self.assertEqual(success,response.json().get("success"))
    self.assertEqual(code,response.json().get("code"))
    self.assertIn(message,response.json().get("message"))

# 封装读取登录数据的函数
def read_login_data(filename):
    # filename 是指登录数据的路径和名称
    with open(filename,"r",encoding="utf-8") as f:
        # 加载json数据
        jsonData = json.load(f)
        # 定义 一个存放登录数据的空列表
        result_list = []
        # 遍历这个jsonData 取出每一条登录测试点的数据
        for login_data in jsonData:
            # 将所有的登录数据以元组的形式存在空列表result_list中
            result_list.append(tuple(login_data.values()))
        # 把提取的数据返回到列表
        return result_list

# 封装读取员工模块增删改查数据的函数
# 先定义员工模块数据路径

def emp_data(filename,interface_name):
    # 读取数据文件
    with open(filename,"r",encoding="utf-8")as f:
        #把数据文件加载json格式数据
        jsonData = json.load(f)
        # 定义一个空列表
        result_list =[]
        # 存放员工的某个接口传过来的数据到空列表
        result_list.append(tuple(jsonData.get(interface_name).values()))
        return result_list



# 调试代码
if __name__== "__main__":
    # 调试读取登录数据的代码
    # filename = os.path.dirname(os.path.abspath(__file__))+"/data/login.json"
    # # 打印路径
    # print(f"路径:{filename}")
    # # 实例化 封装登陆读取函数 并传入读取数据的路径
    # result = read_login_data(filename)
    # print(result)
    filename = os.path.dirname(os.path.abspath(__file__)) + "/data/emp.json"