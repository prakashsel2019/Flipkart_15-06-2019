from selenium import webdriver

from pages.locgeneric import LocGeneric
import allure
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

class WebGeneric(LocGeneric):
    def __init__(self, driver):
        LocGeneric.__init__(self, driver)
        global lc
        lc = LocGeneric(driver)

    def enter(self, locator_type, locator_val, input_val):
        e = self.locator(locator_type, locator_val)
        e.send_keys(input_val)

    def click(self, locator_type, locator_val):
        c = self.locator(locator_type, locator_val)
        c.click()

    def report_pass(self):
        pass

    def report_fail(self):
        pass

    def select_day(self, locator_type, locator_val, input_val):
        day = self.locator(locator_type, locator_val)
        select = Select(day)
        select.select_by_visible_text(input_val)

    def select_month(self, locator_type, locator_val, input_val):
        month = self.locator(locator_type, locator_val)
        select = Select(month)
        select.select_by_value(input_val)

    def select_year(self, locator_type, locator_val, input_val):
        year = self.locator(locator_type, locator_val)
        select = Select(year)
        select.select_by_index(input_val)

    def mouse_hr(self, locator_type, locator_val):
        ele= self.locator(locator_type, locator_val)
        webdriver.ActionChains(self.driver).move_to_element(ele).perform()

    def mouse_hover_without_locator(self, element):
        webdriver.ActionChains(self.driver).move_to_element(element).perform()

    def sort(self, locator_type, sorting_value):
        self.f_xpath = "//div[contains(text(),"
        self.s_xpath = sorting_value
        xpath = self.f_xpath + self.s_xpath
        se = self.locator(locator_type, xpath)
        se.click()

    def key_down(self, locator_type, locator_value):
        kd = self.locator(locator_type, locator_value)
        kd.send_keys(Keys.ENTER)

    def collective_xpath(self, locator_type, locator_value):
        global cx
        cx = self.locators(locator_type, locator_value)

    def brand_selection(self, locator_type, locator_value):
        for i in cx:
            if i.text == "Apple iPhone 6s (Rose Gold, 32 GB)":
                self.first_xpath = "//*[@class='_3wU53n' and contains(text(),"
                self.second_path = locator_value
                full_xpath = self.first_xpath + self.second_path
                final_xpath = self.locator(locator_type, full_xpath)
                final_xpath.click()

    def swtch_to_parent_window(self, parent_window):
        self.parent_window = parent_window
        all_window = self.driver.window_handles
        for id in all_window:
            if parent_window == id:
                self.driver.switch_to.window(parent_window)

    def switch_to_child_window(self, parent_window):
        self.parent_window = parent_window
        all_window = self.driver.window_handles
        for id in all_window:
            if parent_window != id:
                self.driver.switch_to.window(id)


    def xpath_combo(self, locator_type, add_xpath):
        self.f_xpath = "//div[contains(text(),"
        self.s_xpath = add_xpath
        xpath = self.f_xpath + self.s_xpath
        se = self.locator(locator_type, xpath)
        return se

    def footer_links(self, locator_type, locator_value):
        links = [link.get_attribute("href") for link in self.locators(locator_type, locator_value)]
        for link in links:
            self.driver.get(link)
