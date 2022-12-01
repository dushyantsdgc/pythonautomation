import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


class DemoDropDownMultiSelect:
    def demo_dropdown(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("URL")
        driver.maximize_window()
        dd_demo = driver.find_element(By.ID, "")
        dd_multi = Select(dd_demo)
        dd_multi.select_by_index(1)
        time.sleep(2)
        dd_multi.select_by_value("IT_Manager_AP")
        time.sleep(2)
        dd_multi.select_by_visible_text("Developer / Software Engineer / Analyst")
        time.sleep(2)

Demo_MultiSelect = DemoDropDownMultiSelect()
Demo_MultiSelect.demo_dropdown()
