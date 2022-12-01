import time

from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


# noinspection PyMethodMayBeStatic
def test_case1():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get("https://www.salesforce.com/in/form/signup/freetrial-sales/?d=jumbo1-btn-ft")
    driver.maximize_window()
    dropdwn = driver.find_element(By.NAME, "UserTitle")
    drop_down = Select(dropdwn)
    drop_down.select_by_index(1)
    time.sleep(2)
    drop_down.select_by_value("IT_Manager_AP")
    time.sleep(2)
    drop_down.select_by_visible_text("Developer / Software Engineer / Analyst")
    time.sleep(2)

    # driver.close()
