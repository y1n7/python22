from PageLocators.cart_page_loc import CartPageLoc
from common.base_page import BasePage


class CartPage(BasePage):

    def click_cart_go_lesson_delete(self):
        self.click_element(CartPageLoc.cart_go_lesson_delete_loc, "购物车页面_删除第一个课程")
