PATH = 'E:\drivers/chromedriver.exe'
# URL = 'https://www.flipkart.com/'
URL = 'https://www.flipkart.com/'
SearchText = 'Macbook'
Item_Name = 'iPhone'
Sorting_value = "'Price -- Low to High')]"
Brand_value = "'Apple iPhone 6s (Space Grey, 32 GB)')]"
Logout_F_xpath = "//div[contains(text(),"
Logout_S_xpath = "'Qspiderflipkart')]"


import inspect
def whoami():
    return inspect.stack()[1][3]