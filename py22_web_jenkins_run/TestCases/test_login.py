import pytest
from PageObjects.login_page import LoginPage
from PageObjects.home_page import HomePage
from TestDatas import login_datas as ld


@pytest.fixture
def init_driver(init):
    print("=============================测试方法级别：用例开始==================================")
    yield init
    print("=============================测试方法级别：用例结束==================================")


@pytest.fixture(scope="class")
def demo():
    print("=============================测试类级别：用例开始==================================")
    yield
    print("=============================测试类级别：用例结束==================================")


@pytest.mark.usefixtures("init_driver")
class TestLogin:
    @pytest.mark.login
    def test_login_success(self, init_driver):
        pass
        # 关闭首页弹窗
        # HomePage(init_driver["driver"]).close()
        # 点击登录按钮弹出登录页面
        HomePage(init_driver["driver"]).login()
        # 调用登录页面的登录行为
        LoginPage(init_driver["driver"]).login(ld.success_data["user"], ld.success_data["passwd"])
        # 断言
        assert HomePage(init_driver["driver"]).check_user_exist()

    @pytest.mark.usefixtures("demo")
    @pytest.mark.parametrize("case", ld.wrong_data)
    def test_failed_wrong_data(self, init_driver, case):
        # 关闭首页弹窗
        # HomePage(init_driver["driver"]).close()
        # 点击登录按钮弹出登录页面
        HomePage(init_driver["driver"]).login()
        # 调用登录页面的登录行为
        LoginPage(init_driver["driver"]).login(case["user"], case["passwd"])
        # 断言
        assert case["check"] == LoginPage(init_driver["driver"]).get_error_msg()


# @pytest.mark.usefixtures("login_web")
# def test_demo(init):
#     print(init)


if __name__ == '__main__':
    pytest.main(["-v", "-s", "-m", "login"])
