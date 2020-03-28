# 导包
import requests
# 创建测试类
class EmpApi():
    # 初始化
    def __init__(self):
        self.emp_url = "http://182.92.81.159" + "/api/sys/user"

    # 添加员工封装
    def add_emp(self,username,mobile,headers):
        jsonData = { "username":username,
                "mobile": mobile,
                "timeOfEntry": "2020-03-16",
                "formOfEmployment": 2,
                "departmentName": "snowsnow",
                "departmentId": "1226092852421177344",
                "correctionTime": "2020-03-15T16:00:00.000Z"}
        return requests.post(self.emp_url,json=jsonData,headers=headers)

    # 查询封装
    def quer_emp(self,emp_id,headers):
        quer_emp_url = self.emp_url + "/" +emp_id
        return requests.get(quer_emp_url,headers=headers)

    # 修改封装
    def modify_emp(self,emp_id,username,headers):
        # 4.把员工id拼接url组成修改所需要的url
        modify_emp_url = self.emp_url + "/" + emp_id
        # 设置修改数据
        jsonDdata = {"username":username}
        return requests.put(modify_emp_url,json=jsonDdata,headers=headers)

    # 删除封装
    def delete_emp(self,emp_id,headers):
        # 5.把员工id拼接url组成删除所需要的url
        delete_emp_url = self.emp_url + "/" + emp_id
        return requests.delete(delete_emp_url,headers=headers)
