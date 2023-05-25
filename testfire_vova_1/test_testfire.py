from Testfire_element import LandingHelper
from Testfire_element import LandingHelper
from Testfire_element import UserHelper

def test_login (browser):
    landing_page = LandingHelper(browser)
    landing_page.go_to_site()
    login_page = LandingHelper(browser)
    login_page.sent_keys("jsmith")
    login_page.sent_keys("demo1234")
    user_page = UserHelper(browser)
    element = user_page.find_element()
    assert element
    
    
    


