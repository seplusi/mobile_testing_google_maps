import time
import unittest
from src.main.common import appium_driver
from src.main.page_obj import initial_gui
from src.main.page_obj import gui_with_selected_place
from src.main.page_obj import gui_with_selected_address
from src.main.page_obj import gui_with_route_map
from src.main.page_obj import steps_and_more_gui
from src.main.page_obj import route_preview_gui

# due to appium 1.14.2 not being able to deal with send_keys, I have to use an older version of appium
# (Appium-linux-1.13.0.AppImage). Be sure to have this appium running and be sure not to choose uiautomator2
# These tests are passing for android moto E

class GoogleMapsTests(unittest.TestCase):
    def setUp(self):
        self.driver = appium_driver.AppiumDriver(platformVersion='6').driver
        self.initial_gui = initial_gui.InitialGui(self.driver)

    def tearDown(self):
        self.driver.quit()

#    @unittest.skip('')
    def test_place_steps_and_more_flow(self):
        self.initial_gui.insert_place_and_search('Swan Leisure')
        self.initial_gui.validate_search_result('Swan Leisure', 'Rathmines Square, Rathmines Road Lower, Dublin 6')
        self.initial_gui.click_validated_option()

        self.selected_place_gui = gui_with_selected_place.SelectedPlaceGui(self.driver, 'Swan Leisure, Rath',
                                                                           ['Directions', 'Start', 'Call', 'Share'],
                                                                           ['Open · Closes', 'Sports complex', 'min'],
                                                                           'Swan Leisure')
        self.selected_place_gui.click_direction_button()

        self.selected_place_route_gui = gui_with_route_map.SelectedPlaceRouteGui(self.driver, 'Swan Leisure')
        self.selected_place_route_gui.click_cycling_option()
        self.selected_place_route_gui.click_steps_and_more()

        self.steps_and_more_gui = steps_and_more_gui.StepsAndMoreGui(self.driver)

    @unittest.skip('')
    def test_street_steps_and_more1(self):
        self.initial_gui.insert_place_and_search('80A windmill road, crumlin')
        self.initial_gui.validate_search_result('80A Windmill Road', 'Crumlin, Dublin 12')
        self.initial_gui.click_validated_option()

        self.selected_place_gui = gui_with_selected_address.SelectedAddressGui(self.driver, '80A Windmill Road, Crumlin',
                                                                               ['Directions', 'Start', 'Save', 'Share'],
                                                                               ['Crumlin, Dublin 12, D12 Y5Y2', 'At this address:', '\xa0Crumlin Swimming Pool'],
                                                                               '80A Windmill Rd')
        self.selected_place_gui.click_direction_button()

        self.selected_place_route_gui = gui_with_route_map.SelectedPlaceRouteGui(self.driver, '80A Windmill Rd')
        self.selected_place_route_gui.click_cycling_option()
        self.selected_place_route_gui.click_steps_and_more()

        self.steps_and_more_gui = steps_and_more_gui.StepsAndMoreGui(self.driver)
        self.steps_and_more_gui.scroll_2_page_end('80A Windmill Rd, Crumlin')
        self.steps_and_more_gui.navigate_to_destination()

        self.route_preview_gui = route_preview_gui.routePreviewGui(self.driver)
        self.route_preview_gui.navigate_backwards_to_start_point(self.steps_and_more_gui.directions_lst)


    @unittest.skip('')
    def test_street_steps_and_more(self):
        self.initial_gui.insert_place_and_search('17 clanwilliam terrace, dublin')
        self.initial_gui.validate_search_result('17 Clanwilliam Terrace', 'Dublin')
        self.initial_gui.click_validated_option()

        self.selected_place_gui = gui_with_selected_address.SelectedAddressGui(self.driver, '17 Clanwilliam Terrace, Dublin',
                                                                               ['Directions', 'Start', 'Save', 'Share'],
                                                                               ['Dublin', 'min'],
                                                                               '17 Clanwilliam Terrace')
        self.selected_place_gui.click_direction_button()

        self.selected_place_route_gui = gui_with_route_map.SelectedPlaceRouteGui(self.driver, '17 Clanwilliam Terrace')
        self.selected_place_route_gui.click_cycling_option()
        self.selected_place_route_gui.click_steps_and_more()

        self.steps_and_more_gui = steps_and_more_gui.StepsAndMoreGui(self.driver)
        self.steps_and_more_gui.scroll_2_page_end('17 Clanwilliam Terrace')
        self.steps_and_more_gui.navigate_to_destination()

        self.route_preview_gui = route_preview_gui.routePreviewGui(self.driver)
        self.route_preview_gui.navigate_backwards_to_start_point(self.steps_and_more_gui.directions_lst)

        self.driver.find_element_by_android_uiautomator()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(GoogleMapsTests)
    unittest.TextTestRunner(verbosity=1).run(suite)