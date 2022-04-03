from selenium.webdriver.common.by import By


class LoginPageLoc:

    # 元素定位
    # 用户名输入框
    user_loc = (By.NAME, "email")
    # 密码输入框
    passwd_loc = (By.NAME, "password")
    # 登录按钮
    button_loc = (By.XPATH, '//input[@value="登录"]')
    # 错误提示框
    form_error_loc = (By.XPATH, '//ul[@class="autoul"]//following-sibling::p[@class="rlf-tip-wrap errorHint color-red"]')