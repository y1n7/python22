from selenium.webdriver.common.by import By


class HomePageLoc:
    # 元素定位
    # 登录按钮
    button_loc = (By.ID, 'js-signin-btn')
    # 首页弹窗关闭按钮
    close_loc = (By.XPATH, '//span[@class="close imv2-add_circle_o js-close-activity"]')
    # 我的课程按钮
    my_lesson_loc = (By.XPATH, '//span[text()="我的课程"]')
    # 进站必学推荐的第一个课程
    go_lesson_loc = (By.XPATH, '//div[@data-group="进站必学"]//div[@data-type="推荐"]//a[1]')
