
import time
from pages.webgeneric import WebGeneric
from testdata.ExcelUtil import *
from testdata import data as data

class Logout_page(WebGeneric):
    def __init__(self, driver):
        WebGeneric.__init__(self, driver)
        self.text = 'Logout'
        global wb
        wb = WebGeneric(driver)

    def click_logut(self):
        ms = wb.xpath_combo('xpath', data.Logout_S_xpath)
        wb.mouse_hover_without_locator(ms)
        wb.click('link_text', self.text)


# def logout(uname):
#     driver.switch_to.window(parent_window)
#     f_xpath= "//div[contains(text(),"
#     s_xpath = uname
#     xpath = f_xpath + s_xpath
#     element = driver.find_element_by_xpath(xpath)
#     webdriver.ActionChains(driver).move_to_element(element).perform()
#     driver.find_element_by_link_text("Logout").click()
#
# logout("'Prakash')]")