import time
from pages.webgeneric import WebGeneric
from testdata.ExcelUtil import *

class Login_page(WebGeneric):
    def __init__(self, driver):
        WebGeneric.__init__(self, driver)
        self.uname = "//input[@class='_2zrpKA _1dBPDZ']"
        self.paswrd = "//input[@class='_2zrpKA _3v41xv _1dBPDZ']"
        self.clk_login = "//button[@class='_2AkmmA _1LctnI _7UHT_c']"
        global wb
        wb = WebGeneric(driver)

    def enter_username(self, username):
        wb.enter('xpath', self.uname, username)

    def enter_password(self, password):
        wb.enter('xpath', self.paswrd, password)

    def click_login(self):
        wb.click('xpath', self.clk_login)
        time.sleep(5)
