# TODO figure out why HtmlTestRunner doesn't want to be imported, or use another way of HTML reporting
# TODO figure out why windows are duplicated when
# TODO detect that element is read only and throw a message that admin needs to unlock table
# TODO throw everything into separate test cases
# TODO if time permits, implement POM
import HtmlTestRunner
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from datetime import date


class OnlineTimesheet(unittest.TestCase):
    # declare variable to store the URL to be visited
    homepage_url = "http://qualitypointtech.net/timesheetdemo/"
    # parse user data from logindata.txt
    with open('logindata.txt', 'r') as file:
        for details in file:
            username, password = details.split(':')

    # Set up test case
    def setUp(self):
        """Initialize Firefox web driver"""
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    # Load home page
    def test_Challenge(self):
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

        # Determining xpath of input field where Microsoft label stands in document.
        input_xpath = '//label[text()="Microsoft"]/../../td/input[@value="{}"]/../input[@id="projectsum"]'.format(today)
        input_field = self.driver.find_element_by_xpath(str(input_xpath))

        # Entering 6 hrs
        input_field.clear()
        time.sleep(10)
        input_field.send_keys("6")

        # Adding comment
        # Click comment icon
        self.driver.find_element_by_xpath(
            '//label[text()="Microsoft"]/../../td/input[@value="' + today + '"]/../a').click()

        driver.implicitly_wait(2)

        # Enter comment
        comment_box = self.driver.find_element_by_xpath(
            '//label[text()="Microsoft"]/../../td/input[@value="' + today + '"]/../div/form/p/textarea')
        comment_box.clear()
        comment_box.send_keys('Automation Test Comment')
        self.driver.find_element_by_id('comments_submit').click()
        # Wait for text updated and then click X button
        wait = WebDriverWait(driver, 10)
        wait.until(ec.visibility_of_element_located((By.ID, "checkfield")))
        self.driver.find_element_by_class_name('close')
        driver.implicitly_wait(2)

        # Submit Time status
        self.driver.find_element_by_name('submit_time').click()

        # Open Weekly Status Entry
        self.driver.find_element_by_link_text('Weekly Status Entry').click()

        # Assert value is 6
        populated_box_xpath = '//label[text()="Microsoft"]/../../td/input[@value="{}"]/../input[@type="text"]'.format(
            today)
        populated_box_value = self.driver.find_element_by_xpath(populated_box_xpath).get_attribute('value')
        self.assertEqual(populated_box_value, '6')

    def tearDown(self):
        """Cleaning up"""
        self.driver.quit()


if __name__ == '__main__':
    print('hello!!!!!')
    testRunner = HtmlTestRunner.HTMLTestRunner(output='C:\\Reports')
    unittest.main(testRunner)
