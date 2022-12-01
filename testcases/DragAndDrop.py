import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdrivermanager.chrome import ChromeDriverManager


def test_drag_drop():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get("https://jqueryui.com/droppable/")
    driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@class='demo-frame']"))
    element1 = driver.find_element(By.ID, "draggable")
    element2 = driver.find_element(By.ID, "draggable")
    ActionChains(driver).drag_and_drop(element1, element2).perform()
    time.sleep(4)

# class DemoDragDrop:
# DDD = DemoDragDrop()
# DDD.drag_drop()
