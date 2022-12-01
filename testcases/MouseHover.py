import time

from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
# from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


# noinspection PyMethodMayBeStatic
def test_case1():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get("https://www.canva.com/")
    driver.maximize_window()
    action = ActionChains(driver)
    action.move_to_element(driver.find_element(By.ID, "__a11yId1"))
    action.perform()
    driver.find_element(By.XPATH, "//span[normalize-space()='Poster maker']").click()
    time.sleep(2)

    # driver.close()
