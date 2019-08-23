class routePreviewGui(object):
    def __init__(self, driver):
        self.driver = driver
        self.driver.find_element_by_id('com.google.android.apps.maps:id/header_container')
        self.driver.find_element_by_xpath('//android.widget.TextView[@text=\'Route preview\']')
        self.bottommapoverlay_container = self.driver.find_element_by_id('com.google.android.apps.maps:id/bottommapoverlay_container')

    def navigate_backwards_to_start_point(self, directions_list):
        directions_list.pop(0)
        while len(directions_list) > 1:
            header_container = self.driver.find_element_by_id('com.google.android.apps.maps:id/header_container').find_element_by_class_name('androidx.viewpager.widget.ViewPager')

            if directions_list[-1] in [element.text for element in header_container.find_elements_by_xpath('//android.widget.TextView')]:
                self.bottommapoverlay_container.find_element_by_xpath('//android.widget.ImageView[contains(@content-desc, \'Show previous\')]').click()
                check_dups = True
            elif check_dups:
                check_dups = False
                directions_list.pop()
            else:
                print([element.text for element in header_container.find_elements_by_xpath('//android.widget.TextView')])
                print(directions_list)
                assert False

        assert directions_list[0] in [element.text for element in header_container.find_elements_by_xpath('//android.widget.TextView')]
        print('Back to origin OK')