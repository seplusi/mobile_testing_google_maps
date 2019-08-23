from src.main.common import gui_with_selected_object


class SelectedAddressGui(gui_with_selected_object.SelectedObjectGui):

    def validate_items_in_map(self):
        compass_container_element = self.driver.find_element_by_id('com.google.android.apps.maps:id/compass_container')
        layers_images = compass_container_element.find_elements_by_class_name('android.widget.ImageView')
        assert len(layers_images) == 2, 'Number of elements = %d' % len(layers_images)
