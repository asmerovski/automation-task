import unittest
# import HtmlTestRunner
# import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import date


class OnlineTimesheet(unittest.TestCase):
    # declare variable to store the URL to be visited
    with open('logindata.txt', 'r') as file:
        for details in file:
            username, password = details.split(':')
    homepage_url = "http://qualitypointtech.net/timesheetdemo/"

    # Set up test case
    def setUp(self):
        """Initialize Firefox web driver"""
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    # Load home page
    def test_home_page_login(self):
        """Checking if title is ok, elements are present and login is successful."""
        driver = self.driver
        driver.get(self.homepage_url)
        # Check if title is OK, and login controls present
        self.assertIn("Online Timesheet • Qualitypointtech.com", driver.title)
        self.assertTrue(driver.find_element_by_name('username'))
        self.assertTrue(driver.find_element_by_name('password'))
        self.assertTrue(driver.find_element_by_name('login'))
        driver.find_element_by_name('username').send_keys(self.username)
        driver.find_element_by_name('password').send_keys(self.password)
        driver.find_element_by_name('login').click()

        """Entering and checking data"""
        # Add 6 hours to the Microsoft project for today

        # Find today's date first in format 2020-02-03
        today = date.today().strftime('%Y-%m-%d')

        # Determining xpath of input field where Microsoft label stands in doc.
        # input_xpath = str('//label[text()="Microsoft"]/../../td/input[@value="{}"]/../input[@id="projectsum"]'.format(today))
        input_field = self.driver.find_element_by_xpath(
            '//label[text()="Microsoft"]/../../td/input[@value="2020-02-03"]/../input[@id="projectsum"]')

        # Entering 6 hrs
        input_field.clear()
        input_field.send_keys("6")


#    def test_enter_data(self):
#        """Entering and checking data"""
#        # Add 6 hours to the Microsoft project for today
#
#        # Find today's date first in format 2020-02-03
#        today = date.today().strftime('%Y-%m-%d')
#
#        # Determining xpath of input field where Microsoft label stands in doc.
#        # input_xpath = str('//label[text()="Microsoft"]/../../td/input[@value="{}"]/../input[@id="projectsum"]'.format(today))
#        input_field = self.driver.find_element_by_xpath('//label[text()="Microsoft"]/../../td/input[@value="2020-02-03"]/../input[@id="projectsum"]')
#
#        # Entering 6 hrs
#        input_field.clear()
#        input_field.send_keys("6")
#
#        # Adding text to comment window


#        self.assertIn(self.search_term, self.driver.title)
#        # to verify if the search results page contains any results or no results were found.
#        self.assertNotIn("No results found.", self.driver.page_source)

#   def test_add_item_to_cart(self):
#       # to load a given URL in browser window
#       self.driver.get(self.homepage_url)
#       # to enter search term, we need to locate the search textbox
#       searchTextBox = self.driver.find_element_by_id("twotabsearchtextbox")
#       # to clear any text in the search textbox
#       searchTextBox.clear()
#       # to enter the search term in the search textbox via send_keys() function
#       searchTextBox.send_keys(self.search_term)
#       # to search for the entered search term
#       searchTextBox.send_keys(Keys.RETURN)
#       # to click on the first search result's link
#       self.driver.find_element_by_xpath(
#           "(//div[@class='sg-col-inner']//img[contains(@data-image-latency,'s-product-image')])[2]").click()
#       # since the clicked product opens in a new tab, we need to switch to that tab.
#       # to do so we will use window_handles()
#       self.driver.switch_to.window(self.driver.window_handles[1])
#       # to add the product to cart by clicking the add to cart button
#       self.driver.find_element_by_id("add-to-cart-button").click()
#       # to verify that sub cart page has loaded
#       self.assertTrue(self.driver.find_element_by_id("hlb-subcart").is_enabled())
#       # to verify that the product was added to the cart successfully
#       self.assertTrue(self.driver.find_element_by_id("hlb-ptc-btn-native").is_displayed())
#

#   def tearDown(self):
#       """Cleaning up"""
#       self.driver.quit()


if __name__ == '__main__':
    print('hello!!!!!')
    # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/'))
