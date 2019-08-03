from pages.Loginpage import Login_page
# from pages.homepage import HomePage
import pytest

from pages.mousehover import mouse_hover_page
from pages.Logoutpage import Logout_page

from pages.Search_page import Searching_page
@pytest.mark.usefixtures("test_setup")
class TestMouseHover:
    def test_login(self):
        driver = self.driver
        lg = Login_page(driver)
        lg.enter_username('7899091518')
        lg.enter_password('Qspiderflipkart@123')
        lg.click_login()

    def test_search(self):
        driver = self.driver
        global sr
        sr = Searching_page(driver)
        sr.search_item()

    def test_sort_order(self):
        sr.sort_order()
        global pw
        pw = sr.store_parent_window()
        sr.select_brand()
        sr.switch_child(pw)

    def test_add_to_cart(self):
        sr.add_cart()

#     def test_remove_from_cart(self):
#         sr.remove_cart()
#         sr.switch_parent(pw)

#     def test_click_help_center(self):
#         sr.click_help_center()

#     def test_logout(self):
#         driver = self.driver
#         lg = Logout_page(driver)
#         # lg.switch_to_parent_window(pw)
#         lg.click_logut()

#     def test_mouse_hr(self):
#         driver = self.driver
#         mhr = mouse_hover_page(driver)
#         mhr.cancel_popup()
#         # mhr.mse_hr()
#         # mhr.clk_on_items()

#     def test_footer(self):
#         sr.footer_link_one_by_one()
