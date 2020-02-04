# TODO figure out why HtmlTestRunner doesn't want to be imported, or use another way of HTML reporting
# TODO throw everything into separate test cases
# TODO if time permits, implement POM
import os
from pyunitreport import HTMLTestRunner
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from datetime import date

current_directory = os.getcwd()


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
    def test_Automation(self):
        """All tests"""
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
        # Add 6 hours to the project for today
        # Find today's date first in format 2020-02-03
        today = date.today().strftime('%Y-%m-%d')

        # Determining xpath of input field where label stands in document.
        input_xpath = '(//input[@value="{}"])[1]/../input[@id="projectsum"]'.format(today)
        input_field = self.driver.find_element_by_xpath(str(input_xpath))

        # Entering 6 hrs
        self.assertFalse(input_field.get_attribute("readonly"), 'Input field is READ-ONLY. Login as admin and unlock sheet')  # Fail if element is read only
        input_field.clear()
        driver.implicitly_wait(2)
        input_field.send_keys("6")

        # Adding comment
        # Click comment icon
        self.driver.find_element_by_xpath(
            '(//input[@value="{}"])[1]/../input[@id="projectsum"]/../a'.format(today)).click()
        self.driver.implicitly_wait(2)

        # Enter comment
        comment_box = self.driver.find_element_by_id("prjcomments")
        comment_box.clear()
        comment_box.send_keys('Automation Test Comment')
        self.driver.find_element_by_id('comments_submit').click()
        # Wait for text updated and then click X button
        wait = WebDriverWait(driver, 5)
        wait.until(ec.visibility_of_element_located((By.ID, "checkfield")))
        self.driver.find_element_by_class_name('close')
        driver.implicitly_wait(2)

        # Submit Time status
        self.driver.find_element_by_name('submit_time').click()

        # Open Weekly Status Entry
        self.driver.find_element_by_link_text('Weekly Status Entry').click()

        # Assert value is 6
        populated_box_value = self.driver.find_element_by_xpath(input_xpath).get_attribute('value')
        self.assertEqual(populated_box_value, '6')

        # Assert comment
        # TODO: Find text entered in comment. I have no idea how to rip it. Value not present.
        # populated_comment = self.driver.find_element_by_id(comment_box).get_attribute('text')
        # self.assertEqual(populated_comment, 'Automation Test Comment')

    def tearDown(self):
        """Cleaning up"""
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output=current_directory))
