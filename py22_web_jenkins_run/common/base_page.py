from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from common.logger_handler import LoggerHandler
from selenium.webdriver.remote.webdriver import WebDriver
from common.dir_paths import DirPaths
from datetime import datetime
import os
import time


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.logger = LoggerHandler("WEB自动化日志")
        # time_now = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        # logs_path = os.path.join(DirPaths.logs_dir, "{}.log".format(time_now))
        # self.logger = LoggerHandler("WEB自动化日志", 0, logs_path, 0)

    # 等待元素可见
    def wait_ele_visible(self, locator, img_doc, timeout=30, poll_fre=0.5):
        """
        :param locator: 元组类型（元素定位策略，元素定位表达式）
        :param img_doc: 截图文件的命名部分。${页面名称_行为名称}_当前的时间.png
        :param timeout: 最长等待时间
        :param poll_fre: 轮询时间
        :return:
        """
        self.logger.info("{}：等待 {} 元素可见".format(img_doc, locator))
        try:
            start = datetime.now()
            WebDriverWait(self.driver, timeout, poll_fre).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            self.logger.exception("{}：等待 {} 元素可见异常".format(img_doc, locator))
            self.save_page_screenshot(img_doc)
            raise
        else:
            end = datetime.now()
            duration = (end - start)
            self.logger.info("等待结束，开始时间为：{}，结束时间为：{}，一共等待耗时为：{}".format(start, end, duration))

    def wait_page_contains_element(self, locator, img_doc, timeout=30, poll_fre=0.5):
        self.logger.info("{}：等待 {} 元素存在".format(img_doc, locator))
        try:
            start = datetime.now()
            WebDriverWait(self.driver, timeout, poll_fre).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            self.logger.exception("{}：等待 {} 元素存在异常".format(img_doc, locator))
            self.save_page_screenshot(img_doc)
            raise
        else:
            end = datetime.now()
            duration = (end - start)
            self.logger.info("等待结束，开始时间为：{}，结束时间为：{}，一共等待耗时为：{}".format(start, end, duration))

    def get_element_text(self, locator, img_doc, timeout=30, poll_fre=0.5):
        self.wait_page_contains_element(locator, img_doc, timeout, poll_fre)
        ele = self.get_element(locator, img_doc)
        self.logger.info("{}：获取 {} 元素的文本内容.".format(img_doc, locator))
        try:
            text = ele.text
        except:
            self.logger.exception("{}：获取 {} 元素的文本内容异常.".format(img_doc, locator))
            self.save_page_screenshot(img_doc)
            raise
        else:
            self.logger.info("获取的文本值为 {}".format(text))
            return text

    def get_element_attribute(self, locator, attr, img_doc, timeout=30, poll_fre=0.5):
        self.wait_page_contains_element(locator, img_doc, timeout, poll_fre)
        ele = self.get_element(locator, img_doc)
        self.logger.info("{}：获取 {} 元素的属性 {}.".format(img_doc, locator, attr))
        try:
            value = ele.get_attribute(attr)
        except:
            self.logger.exception("{}：获取 {} 元素的属性 {} 出现异常.".format(img_doc, locator, attr))
            self.save_page_screenshot(img_doc)
            raise
        else:
            self.logger.info("获取的属性值为 {}".format(value))
            return value

    def check_element_exists(self, locator, img_doc, timeout=30, poll_fre=0.5):
        try:
            WebDriverWait(self.driver, timeout, poll_fre).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            self.logger.exception("{}：{} 元素不存在".format(img_doc, locator))
            self.save_page_screenshot(img_doc)
            return False
        else:
            self.logger.info("{}：{} 元素存在".format(img_doc, locator))
            return True

    def switch_to_new_window(self):
        time.sleep(2)
        wins = self.driver.window_handles
        try:
            self.driver.switch_to.window(wins[-1])
        except:
            self.logger.exception("切换新窗口失败")
        else:
            self.logger.info("切换新窗口成功")

    def get_current_url(self):
        try:
            current_url = self.driver.current_url
        except:
            self.logger.exception("获取当前url失败")
        else:
            self.logger.info("获取的当前url是： {}".format(current_url))
            return current_url

    def get_element(self, locator, img_doc):
        self.logger.info("{}：查找 {} 元素".format(img_doc, locator))
        try:
            ele = self.driver.find_element(*locator)
        except:
            self.logger.exception("{}：查找 {} 元素异常".format(img_doc, locator))
            self.save_page_screenshot(img_doc)
            raise
        else:
            return ele

    def input_text(self, locator, value, img_doc, timeout=30, poll_fre=0.5):
        # 1）等待元素可见 2）查找元素 3）输入动作
        self.wait_ele_visible(locator, img_doc, timeout, poll_fre)
        ele = self.get_element(locator, img_doc)
        self.logger.info("{}：对 {} 元素输入文本 {}".format(img_doc, locator, value))
        try:
            ele.send_keys(value)
        except:
            self.logger.exception("{}：对 {} 元素输入文本 {} 异常".format(img_doc, locator, value))
            # 截图 命名。 页面名称_行为名称_当前的时间.png
            self.save_page_screenshot(img_doc)
            raise

    def click_element(self, locator, img_doc, timeout=30, poll_fre=0.5):
        # 1）等待元素可见 2）查找元素 3）点击
        self.wait_ele_visible(locator, img_doc, timeout, poll_fre)
        ele = self.get_element(locator, img_doc)
        self.logger.info("{}：点击 {} 元素".format(img_doc, locator))
        try:
            ele.click()
        except:
            self.logger.exception("{}：点击 {} 元素异常".format(img_doc, locator))
            # 截图 命名。 页面名称_行为名称_当前的时间.png
            self.save_page_screenshot(img_doc)
            raise

    def save_page_screenshot(self, img_doc):
        time_now = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        screenshot_path = os.path.join(DirPaths.screenshots_dir, "{}_{}.png".format(img_doc, time_now))
        try:
            self.driver.save_screenshot(screenshot_path)
        except:
            self.logger.exception("当前网页截图失败")
        else:
            self.logger.info("截取当前网页成功并存储在：{}".format(screenshot_path))


