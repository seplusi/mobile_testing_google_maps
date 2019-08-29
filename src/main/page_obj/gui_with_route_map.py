from selenium.common.exceptions import NoSuchElementException


class SelectedPlaceRouteGui(object):
    def __init__(self, driver, place):
        self.driver = driver
        self.header_element = self.driver.find_element_by_id('com.google.android.apps.maps:id/header_container')
        self.validate_header(place)
        self.validate_map_items()
        self.start_button = self.driver.find_element_by_id('com.google.android.apps.maps:id/start_button')
        self.steps_and_more_button = self.driver.find_element_by_id('com.google.android.apps.maps:id/persistent_footer_secondary_button')

    def validate_header(self, place):
        self.header_element.find_element_by_xpath('//android.widget.FrameLayout[contains(@content-desc,\'Navigate up\')]')
        self.header_element.find_element_by_xpath('//android.widget.TextView[@text=\'Your location\']')
        self.header_element.find_element_by_xpath('//android.widget.TextView[@text=\'%s\']' % place)
        self.header_element.find_element_by_xpath('//android.widget.ImageView[contains(@content-desc, \'Overflow menu\')]')
        self.header_element.find_element_by_xpath('//android.widget.ImageView[contains(@content-desc, \'Swap start and destination\')]')

        horizontal_buttons = self.header_element.find_element_by_class_name('android.widget.HorizontalScrollView')
        horizontal_buttons.find_element_by_xpath('//android.widget.LinearLayout[contains(@content-desc, \'Public transport mode:\')]')
        horizontal_buttons.find_element_by_xpath('//android.widget.LinearLayout[contains(@content-desc, \'Walking mode:\')]')
        horizontal_buttons.find_element_by_xpath('//android.widget.LinearLayout[contains(@content-desc, \'Ride services:\')]')

        for _ in range(2):
            try:
                self.driver.implicitly_wait(1)
                self.driver.find_element_by_xpath('//android.widget.LinearLayout[contains(@content-desc, \'Driving mode\')]')
                break
            except NoSuchElementException:
                self.driver.swipe(100, 200, 222, 200, 500)
        else:
            assert False

        for _ in range(2):
            try:
                self.cycling_button = self.driver.find_element_by_xpath('//android.widget.LinearLayout[contains(@content-desc, \'Cycling mode:\')]')
                break
            except NoSuchElementException:
                self.driver.swipe(222, 200, 100, 200, 500)
        else:
            assert False

        self.driver.implicitly_wait(20)

    def validate_map_items(self):
        self.driver.find_element_by_id('com.google.android.apps.maps:id/above_compass_button').find_element_by_xpath('//android.widget.FrameLayout[contains(@content-desc, \'Layers button\')]')
        self.driver.find_element_by_id('com.google.android.apps.maps:id/mylocation_button')

    def click_steps_and_more(self):
        self.steps_and_more_button.click()

    def click_cycling_option(self):
        self.cycling_button.click()
