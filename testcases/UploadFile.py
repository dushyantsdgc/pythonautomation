import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
# from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


# noinspection PyMethodMayBeStatic
def test_case1():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.maximize_window()
    driver.switch_to.frame(0)
    time.sleep(4)
    # driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@class='demo-frame']"))
    # driver.find_element(By.XPATH, "//spman[@id='computer_icone_name']")
    driver.find_element(By.ID, "RESULT_FileUpload-10").send_keys("C://Users/dushyants1/Desktop/My Image.jpg")
    time.sleep(4)
    # driver.close()
