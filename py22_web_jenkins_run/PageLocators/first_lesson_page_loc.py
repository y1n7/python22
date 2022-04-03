from selenium.webdriver.common.by import By


class FirstLessonPageLoc:
    # 进站必学的第一个课程加入购物车按钮
    first_lesson_cart_loc = (By.XPATH, '//div[@class="btns js-btns "]//a[@class="js-addcart addcart"]')
    # 购物车按钮
    cart_button = (By.XPATH, '//span[@class="icon-shopping-cart js-endcart"]')
