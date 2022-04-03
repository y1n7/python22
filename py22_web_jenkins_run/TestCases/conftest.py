import pytest
from selenium import webdriver
from TestDatas import common_datas as cd
from TestDatas import login_datas as ld
from PageObjects.login_page import LoginPage
from PageObjects.home_page import HomePage


@pytest.fixture()
def init():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(cd.login_url)
    yield {"driver": driver}
    driver.quit()


@pytest.fixture()
def login_web(init):
    # 调用了init，并用init作为参数
    # 关闭首页弹窗
    # HomePage(init["driver"]).close()
    # 点击登录按钮弹出登录页面
    HomePage(init["driver"]).login()
    # 调用登录页面的登录行为
    LoginPage(init["driver"]).login(ld.success_data["user"], ld.success_data["passwd"])
    print("前置操作")
    yield init
    # 如果用例调用login_web，此时会有两个yield，通过调用init可以得到driver，也可以通过调用login_web得到driver
    print("后置操作")


@pytest.fixture(scope="session", autouse=True)
def session_gl():
    print("=========================测试会话开始=============================")
    yield True
    print("=========================测试会话结束=============================")

"""
用例当中调用login_web的执行顺序
init的前置
login_web的前置
执行用例
login_web的后置
init的后置
fixture继承可以继承高级别，但是不能继承低级别，function可以继承class，但是class不能继承function
"""



