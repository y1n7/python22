from PageLocators.login_page_loc import LoginPageLoc as loc
from common.base_page import BasePage


class LoginPage(BasePage):
    # 登录操作
    def login(self, username, passwd):
        self.input_text(loc.user_loc, username, "登录页面_用户名输入")
        self.input_text(loc.passwd_loc, passwd, "登录页面_密码输入")
        self.click_element(loc.button_loc, "登录页面_点击登录按钮")

    def get_error_msg(self):
        return self.get_element_text(loc.form_error_loc, "登录页面_获取登录错误提示信息")



