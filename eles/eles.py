from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
import operations
import testdata
import os


'''整个脚本运行下的元素定位方法'''

class Eles:
    def __init__(self,driver):
        self.driver = driver

    #定义：查找元素方法函数
    def eles_find_element(self, loc,timeout=10,poll_frequency = 0.5 ):
        return WebDriverWait(self.driver, timeout = timeout, poll_frequency = poll_frequency).until(lambda x:x.find_element(*loc))


    #定义：点击方法函数
    def eles_click(self, loc):
        self.eles_find_element(loc).click()
        time.sleep(1)

    #定义：enter确认模拟点击的方法函数
    def eles_click_enter(self,loc):
        ele = self.eles_find_element(loc)
        ele.send_keys(Keys.ENTER)
        time.sleep(1)

    # 使用向下键确认模拟点击方法
    def eles_click_down(self, loc):
        el = self.eles_find_element(loc)
        el.send_keys(Keys.DOWN)
        time.sleep(1)


    #定义：输入方法函数
    def eles_input(self,loc,value):
        ele = self.eles_find_element(loc)
        ele.click()
        ele.clear()
        time.sleep(2)
        ele.send_keys(value)
        time.sleep(2)

    # 获取文本方法
    def eles_get_text(self, loc):
        return self.eles_find_element(loc).text


    #定义：页面返回/回退函数
    def eles_back(self):
        self.driver.back()
        time.sleep(1)


    # 获取value的属性方法
    def eles_get_value(self, loc):
        # 使用get_attribute获取指定的元素值
        self.eles_find_element(loc).get_attribute("textContent")

    #定义：判断元素是否存在，存在返回true，不存在返回false
    def eles_element_isExist(self,loc):
        try:
            self.eles_find_element(loc,timeout=2)
            return True
        except:
            return False


    #定义：登录用户名
    def system_input_username(self,username):
        self.eles_input(operations.public_username_input,username)
        time.sleep(1)

    #定义：登录密码
    def system_input_password(self,password):
        self.eles_input(operations.public_password_input,password)
        time.sleep(1)

    #定义：登录操作
    def system_login_button(self):
        self.eles_click(operations.login_button)
        time.sleep(1)


    #组装登录操作方法
    def system_login(self):
        self.system_input_username("dym6")
        self.system_input_password("123456")
        self.system_login_button()
        time.sleep(1)

