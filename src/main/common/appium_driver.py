from appium import webdriver


class AppiumDriver(object):
    def __init__(self, implicit_wait=20, **kwargs):
        desired_caps = {}
        desired_caps['platformName'] = kwargs.get('plafformName', 'Android')
        desired_caps['platformVersion'] = kwargs.get('platformVersion', '6')
        desired_caps['deviceName'] = kwargs.get('deviceName', 'Moto E')
        desired_caps['noReset'] = kwargs.get('noReset', 'true')
        desired_caps['appPackage'] = kwargs.get('appPackage', 'com.google.android.apps.maps')
        desired_caps['appActivity'] = kwargs.get('appActivity', 'com.google.android.maps.MapsActivity')
        if kwargs.get('browserName'):
            desired_caps['browserName'] = kwargs.get('browserName', 'Chrome')

        desired_caps['automationName'] = kwargs.get('automationName', 'UiAutomator2')

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(implicit_wait)
