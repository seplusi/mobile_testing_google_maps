class InitialGui(object):
    def __init__(self, driver):
        self.driver = driver
        self.text_box = self.driver.find_element_by_id('com.google.android.apps.maps:id/search_omnibox_text_box')

    def insert_place_and_search(self, place):
        self.text_box.click()
        self.text_box = self.driver.find_element_by_id('com.google.android.apps.maps:id/search_omnibox_edit_text')
        self.text_box.send_keys(place)

    def validate_search_result(self, place, address):
        self.selection = self.driver.find_element_by_xpath("//android.widget.TextView[@text='%s']/../.." % place)
        self.selection.find_element_by_xpath("//android.widget.TextView[@text='%s']" % place)
        self.selection.find_element_by_xpath("//android.widget.TextView[contains(@text, '%s')]" % address)
        self.selection.find_element_by_xpath("//android.widget.TextView[contains(@text, 'mi')]")

    def click_validated_option(self):
        self.selection.find_element_by_class_name('android.widget.ImageView')
        self.selection.click()
