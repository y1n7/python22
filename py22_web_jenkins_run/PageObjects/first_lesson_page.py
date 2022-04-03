from PageLocators.first_lesson_page_loc import FirstLessonPageLoc
from common.base_page import BasePage


class FirstLessonPage(BasePage):

    def click_add_cart_button(self):
        self.click_element(FirstLessonPageLoc.first_lesson_cart_loc, "进站必学推荐第一个课程详情页面_点击加入购物车按钮")

    def click_cart_button(self):
        self.click_element(FirstLessonPageLoc.cart_button, "进站必学推荐第一个课程详情页面_点击购物车按钮来进入购物车页面")
