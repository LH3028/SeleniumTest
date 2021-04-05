from utils.read_ini import ReadIni
import os


class FindElement(object):
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, key):
        read_ini = ReadIni()
        data = read_ini.get_value(key)
        by = data.split(':')[0]
        value = data.split(':')[1]
        try:
            if by == "id":
                return self.driver.find_element_by_id(value)
            elif by == "name":
                return self.driver.find_element_by_name(value)
            elif by == "className":
                return self.driver.find_element_by_class_name(value)
            elif by == "xpath":
                return self.driver.find_element_by_xpath(value)
        except Exception as e:
            dir = os.path.dirname(os.getcwd())
            images_dir = os.path.join(dir, "Png")
            self.driver.save_screenshot(images_dir+"/%s.png" %value)
            return None


