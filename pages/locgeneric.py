class LocGeneric:
    def __init__(self, driver):
        self.driver = driver

    def locator(self, loc_type, locator_val):
        try:
            if loc_type == "name":
                ele = self.driver.find_element_by_name(locator_val)
            elif loc_type == "id":
                ele = self.driver.find_element_by_id(locator_val)
            elif loc_type == "xpath":
                ele = self.driver.find_element_by_xpath(locator_val)
            elif loc_type == "link_text":
                ele = self.driver.find_element_by_link_text(locator_val)
            return ele
        except AssertionError as e:
            self.report_fail
        except:
            self.report_fail()

    def locators(self, loc_type, locator_val):
        try:
            if loc_type == "name":
                ele = self.driver.find_elements_by_name(locator_val)
            elif loc_type == "id":
                ele = self.driver.find_elements_by_id(locator_val)
            elif loc_type == "xpath":
                ele = self.driver.find_elements_by_xpath(locator_val)
            return ele
        except AssertionError as e:
            self.report_fail
        except:
            self.report_fail()


