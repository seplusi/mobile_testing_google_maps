from appium.webdriver.common.touch_action import TouchAction


class StepsAndMoreGui(object):
    def __init__(self, driver):
        self.driver = driver
        self.driver.find_element_by_xpath('//androidx.viewpager.widget.ViewPager[contains(@content-desc, \'walking directions\')]')
        self.steps_box = self.driver.find_element_by_id('com.google.android.apps.maps:id/details_cardlist')
        self.move_start_point = self.steps_box.find_element_by_xpath('//android.widget.TextView[@text=\'Your location\']')
        self.driver.find_element_by_id('com.google.android.apps.maps:id/start_button')
        self.driver.find_element_by_id('com.google.android.apps.maps:id/persistent_footer_secondary_button')
        self.destination_nav_button = None
        self.directions_lst = None

    def scroll_2_page_end(self, address):
        self.directions_lst = [element.text for element in self.driver.find_elements_by_xpath('//android.support.v7.widget.RecyclerView/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView')]
        self.driver.implicitly_wait(2)
        for _ in range(100):
            try:
                current_directions = [element.text for element in self.driver.find_elements_by_xpath('//android.support.v7.widget.RecyclerView/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView')]
                print('current_direction = %s' % str(current_directions))
                if self.directions_lst[-1] != current_directions[-1]:
                    self.directions_lst.append(current_directions[-1])
                    print('Added another direction')

                self.driver.find_element_by_xpath('//android.widget.TextView[@text=\'%s\']' % address)
                self.directions_lst.append(address)
                print('Just appended %s. Final list of directions: \n%s' % (address, str(self.directions_lst)))
                break
            except Exception as e:
                self.driver.swipe(100, 350, 100, 100)
        else:
            assert False, 'Element //android.widget.TextView[@text=\'%s\'] wasn\'t found' % address

        self.driver.implicitly_wait(20)
        self.driver.swipe(100, 350, 200, 100)
        self.destination_nav_button = self.driver.find_element_by_xpath('//android.widget.TextView[@text=\'%s\']/../../../android.widget.FrameLayout/android.widget.ImageView' % address)

    def navigate_to_destination(self):
        self.destination_nav_button.click()
