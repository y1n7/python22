from PageLocators.home_page_loc import HomePageLoc as loc
from common.base_page import BasePage


class HomePage(BasePage):

    def login(self):
        self.click_element(loc.button_loc, "首页_点击登录按钮来弹出登录页面")

    def close(self):
        self.click_element(loc.close_loc, "首页_关闭首页弹窗")

    def click_go_lesson(self):
        self.click_element(loc.go_lesson_loc, "首页_点击进站必学推荐的第一个课程")

    def check_user_exist(self):
        return self.check_element_exists(loc.my_lesson_loc, "首页_我的课程按钮")
