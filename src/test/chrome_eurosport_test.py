import unittest
from src.main.common import appium_driver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

# This test runs with appium v1.14.1. Just start appium with this command:
# appium --chromedriver-executable /home/luis/Documents/chromedriver
#
# Make sure you're using uiautomator2 because it's tha latest and supported version.


class GoogleMapsTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = appium_driver.AppiumDriver(appPackage='', browserName='Chrome', automationName='UiAutomator2',
                                                platformVersion='6').driver

    def setUp(self):
        self.driver.get('https://www.eurosport.co.uk/')
        try:
            self.driver.implicitly_wait(5)
            self.driver.find_element_by_css_selector('button[class=\'qc-cmp-button\']').click()
            self.driver.find_element_by_css_selector('path[class =\'close-x\']').click()
            self.driver.find_element_by_css_selector('a[class=\'sb-close\']').click()

        except NoSuchElementException:
            print('No popup. No need to accept.')
        finally:
            self.driver.implicitly_wait(30)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

#    @unittest.skip('')
    def test_eurosport_formula1(self):
        self.driver.find_element_by_css_selector('div[data-modal-id="navallsport"]').click()
        self.driver.find_element_by_css_selector('li[class=\'modalnav__rightcol-item\'] > a[href=\'/allmotorsports/\']').click()
        self.driver.find_element_by_css_selector('div[class="modalnav__rightcol-subnav modalnav__rightcol-subnav--open"] > div[class="modalnav__rightcol-subnav-title"]')
        self.driver.find_element_by_css_selector('li[class="modalnav__rightcol-subnav-list-item"] > a[href="/formula-1/"]').click()
        self.driver.find_element_by_css_selector('li[class=\'breadcrumb-item fade-in two\']  a[href=\'/formula-1/\']')
        print('Finished test eurosport formula1')

#    @unittest.skip('')
    def test_eurosport_motorcycling(self):
        self.driver.find_element_by_css_selector('div[data-modal-id="navallsport"]').click()
        self.driver.find_element_by_css_selector('li[class=\'modalnav__rightcol-item\'] > a[href=\'/allmotorsports/\']').click()
        self.driver.find_element_by_css_selector('div[class="modalnav__rightcol-subnav modalnav__rightcol-subnav--open"] > div[class="modalnav__rightcol-subnav-title"]')
        self.driver.find_element_by_css_selector('a[href="/moto/"]').click()
        self.driver.find_element_by_css_selector('li[class=\'breadcrumb-item fade-in two\']  a[href=\'/moto/\']')

        self.driver.find_element_by_css_selector('a[class="has-relation col-left"] > span[class="navtab-label"]').click()
        self.driver.find_element_by_css_selector('ul[class="categorylist hidetablet"] a[href="/moto/world-championship/standing.shtml"]').click()

        self.driver.find_element_by_css_selector('span[class="nav-tab__dropdown-arrow"]').click()
        categories = self.driver.find_elements_by_css_selector('ul[class="nav-tab__dropdown-content"] > li')
        for cat in categories:
            if cat.text == 'MotoGP':
                cat.click()
                break
        else:
            assert False

        miguel = self.driver.find_element_by_css_selector('a[href^="/moto/miguel-oliveira"] > span[class="player"]')
        actions = ActionChains(self.driver)
        actions.move_to_element(miguel).perform()
        miguel.click()
        self.driver.find_element_by_css_selector('h1[class="person-head__person-name"]')
        print('Finished test eurosport Miguel Oliveira')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(GoogleMapsTests)
    unittest.TextTestRunner(verbosity=1).run(suite)