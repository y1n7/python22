import time
import pytest
from selenium import webdriver
from PageObjects.login_page import LoginPage
from PageObjects.home_page import HomePage
from PageObjects.first_lesson_page import FirstLessonPage
from PageObjects.cart_page import CartPage
from TestDatas import common_datas as cd
from TestDatas import login_datas as ld
from common.base_page import BasePage


@pytest.fixture
def init_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(cd.login_url)
    # 关闭首页弹窗
    # HomePage(driver).close()
    # 点击登录按钮弹出登录页面
    HomePage(driver).login()
    # 调用登录页面的登录行为
    LoginPage(driver).login(ld.success_data["user"], ld.success_data["passwd"])
    yield {"driver": driver}
    driver.quit()


@pytest.mark.usefixtures("init_driver")
class TestAddCart:

    def test_add_cart_success(self, init_driver):
        # 选择进站必学第一个课程进行点击
        HomePage(init_driver["driver"]).click_go_lesson()
        bp = BasePage(init_driver["driver"])
        bp.switch_to_new_window()
        time.sleep(3)
        FirstLessonPage(init_driver["driver"]).click_add_cart_button()
        time.sleep(3)
        FirstLessonPage(init_driver["driver"]).click_cart_button()
        bp.switch_to_new_window()
        time.sleep(5)
        CartPage(init_driver["driver"]).click_cart_go_lesson_delete()
        time.sleep(2)


if __name__ == '__main__':
    pytest.main()
