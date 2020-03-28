#导包
import requests
import logging
# 定义封装登录API的类
class LoginApi():
    def __init__(self):
        # 定义ihrm登录接口url
        self.login_url = "http://182.92.81.159/api/sys/login"
    # 定义封装登录函数
    def login(self,jsonDdata,headers):
       response =  requests.post(self.login_url,json=jsonDdata,headers=headers)
       return response
# 防止导入模块时执行写在累外面的代码 调试用
if __name__ == "__main__":
    # 实例化对象
    login_api = LoginApi()
    jsonDdata = {"mobile":"13800000002","password":"123456"}
    headers = {"Content-Type":"application/json"}
    response = login_api.login(jsonDdata,headers)
    print(response)
    logging.info(f"{response.json()}")