import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


# noinspection PyMethodMayBeStatic
class DemoDragDrop:

    def test_case1(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        # driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://jqueryui.com/droppable/")
        driver.maximize_window()
        driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@class='demo-frame']"))
        element1 = driver.find_element(By.ID, "draggable")
        element2 = driver.find_element(By.ID, "droppable")
        ActionChains(driver).drag_and_drop(element1, element2).perform()
        time.sleep(4)


DDD = DemoDragDrop()
DDD.test_case1()

# class DemoDragDrop:
#     pass
