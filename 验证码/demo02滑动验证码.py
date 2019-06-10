# coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
email ="654735670@qq.com"
password = '123456'
url = "https://account.geetest.com/login"

class CrackGeetest():
    def __init__(self):
        self.url = url
        self.brower = webdriver.Chrome()
        self.wait = WebDriverWait(self.brower,20)
        self.email = email
        self.password = password
    def get_geetest_button(self):
        """
        获取button对象
        :return: 按钮对象
        """
        button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,".geetest_radar_tip")))
        return button
    def __main__(self):
        button =self.get_geetest_button()
        button.click()

