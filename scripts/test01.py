# @allure.step("内容"),只能修饰函数
# allure.attach("描述","内容")  只能修饰函数体内容,失败截图
# @pytest.allure.sever
import allure
import pytest


class Test():
    @pytest.allure.severity(pytest.allure.severity_level.minor)
    @allure.step("test正在运行")
    def test01(self):
        allure.attach("test1","")
        print("test01被执行")

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step("test2正在运行")
    def test02(self):
        allure.attach("test1", "测试成功")
        print("test02被执行")