import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
# from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


# noinspection PyMethodMayBeStatic
def test_case1():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt")
    driver.maximize_window()
    driver.switch_to.frame("iframeResult")
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
    time.sleep(2)
    driver.switch_to.alert.accept()
    time.sleep(2)

    driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
    time.sleep(2)
    driver.switch_to.alert.dismiss()
    time.sleep(2)

    driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
    time.sleep(2)
    driver.switch_to.alert.send_keys("Hello")
    time.sleep(4)
    driver.switch_to.alert.accept()
    time.sleep(2)



    # driver.close()
