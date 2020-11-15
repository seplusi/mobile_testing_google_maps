class SelectedObjectGui(object):
    def __init__(self, driver, place, horiz_button_lst, vertical_text_list, footer_title):
        self.driver = driver
        self.omnibox_container_element = None
        self.driver.find_elements_by_id('com.google.android.apps.maps:id/mainmap_container')
        self.validate_omnibox_container(place)
        self.validate_items_in_map()
        self.horizontal_bottom_buttons = self.driver.find_element_by_class_name(
            'android.widget.HorizontalScrollView').find_elements_by_class_name('android.widget.Button')
        self.validate_footer_container(horiz_button_lst, vertical_text_list, footer_title)

    def validate_omnibox_container(self, place_address):
        omnibox_container_element = self.driver.find_element_by_id('com.google.android.apps.maps:id/search_omnibox_container')
        omnibox_container_element.find_element_by_id('com.google.android.apps.maps:id/search_omnibox_menu_button')
        omnibox_container_element.find_element_by_xpath("//android.widget.TextView[contains(@text, '%s')]" % place_address)
        omnibox_container_element.find_element_by_id('com.google.android.apps.maps:id/search_omnibox_text_clear')
        omnibox_container_element.find_element_by_class_name('android.widget.ImageButton')
        self.omnibox_container_element = omnibox_container_element

    def validate_items_in_map(self):
        compass_container_element = self.driver.find_element_by_id('com.google.android.apps.maps:id/compass_container')
        layers_images = compass_container_element.find_elements_by_class_name('android.widget.ImageView')
        assert len(layers_images) == 2, 'Number of elements = %d' % len(layers_images)
        self.driver.find_element_by_xpath('//android.widget.Button[@text=\'See similar places\']')

    def click_direction_button(self):
        for button in self.horizontal_bottom_buttons:
            if button.text == 'Directions':
                break
        else:
            assert False

        button.click()

    def select_starting_point(self):
        self.driver.find_element_by_id('com.google.android.apps.maps:id/directions_startpoint_textbox').click()
        self.driver.find_element_by_id('com.google.android.apps.maps:id/recycler_view').find_elements_by_class_name('android.widget.FrameLayout')[0].click()

    def validate_footer_container(self, horiz_button_lst, vertical_text_list, footer_title):
        footer_container_element = self.driver.find_element_by_xpath('//android.view.ViewGroup//android.widget.RelativeLayout')
        assert self.driver.find_element_by_id('com.google.android.apps.maps:id/title').text == footer_title

        text_elements = footer_container_element.find_elements_by_xpath('//android.widget.LinearLayout//android.widget.TextView')
        for costum_text in vertical_text_list:
            for element in text_elements:
                if costum_text in element.text:
                    break
            else:
                print([element.text for element in text_elements])
                print(vertical_text_list)
                print(costum_text)
                assert False

        for button in self.horizontal_bottom_buttons:
            if button.text not in horiz_button_lst:
                print(horiz_button_lst)
                print(self.horizontal_bottom_buttons)
                print(button.text)
                assert False

        self.driver.find_element_by_id('com.google.android.apps.maps:id/street_view_thumbnail')
        zoom_images = self.driver.find_element_by_id('com.google.android.apps.maps:id/mylocation_button').find_elements_by_xpath('//android.widget.ImageView')
        assert len(zoom_images) == 2, 'Number of zoom images is %d' % len(zoom_images)

        for button in self.horizontal_bottom_buttons:
            if button.text == 'Directions':
                break
        else:
            assert False
