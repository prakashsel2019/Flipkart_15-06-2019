import time
from pages.webgeneric import WebGeneric
from testdata.ExcelUtil import *
from selenium.webdriver.common.keys import Keys
from testdata import data as data

class Searching_page(WebGeneric):
    def __init__(self, driver):
        WebGeneric.__init__(self, driver)
        self.item = "//input[@placeholder='Search for products, brands and more']"
        self.collect_brand = "//*[@class='_3wU53n']"
        self.clk_add_cart = "//button[@class='_2AkmmA _2Npkh4 _2MWPVK']"
        self.clk_remove_cart = "//span[contains(text(),'Remove')]"
        self.clk_help_center = "//*[contains(text(),'Help Center')]"
        self.footer_links_path = "//*[@class='_2NHqR1 row']//a"
        global wb
        wb = WebGeneric(driver)

    def search_item(self):
        wb.enter('xpath', self.item, data.Item_Name)
        wb.key_down('xpath', self.item)

    def sort_order(self):
        wb.sort('xpath', data.Sorting_value)
        time.sleep(10)

    def store_parent_window(self):
        parent_window = self.driver.current_window_handle
        return parent_window

    def switch_parent(self, parent_window):
        wb.swtch_to_parent_window(parent_window)

    def select_brand(self):
        wb.collective_xpath('xpath', self.collect_brand)
        wb.brand_selection('xpath', data.Brand_value)

    def switch_child(self, parent_window):
        wb.switch_to_child_window(parent_window)
        time.sleep(5)

    def add_cart(self):
        wb.click('xpath', self.clk_add_cart)
        time.sleep(5)

    def remove_cart(self):
        wb.click('xpath', self.clk_remove_cart)

    def click_help_center(self):
        wb.click('xpath', self.clk_help_center)
        time.sleep(5)
        self.driver.back()

    def footer_link_one_by_one(self):
        wb.footer_links('xpath', self.footer_links_path)






