import time
# from selenium.webdriver import ActionChains
from selenium.webdriver.common import alert
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


def test_case1():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get("https://www.tricentis.com/lp/testim-trial-test-automation-ppc?utm_source=google&utm_medium=paidsearch&utm_campaign=Testim_Search_Nonbrand_Low_EMEA_EN&utm_term=website%20testing%20software&gclid=EAIaIQobChMIp6OegJnA-wIVpu_tCh13Ug_1EAAYASAAEgK4NvD_BwE")
    driver.maximize_window()

    # alert.accept()
    switch_to_frame("MktoForms2XDIframe")
    drop_down_1 = driver.find_element(By.ID, "Country")
    country = Select(drop_down_1)
    country.select_by_index(1)
    time.sleep(5)

    drop_down_2 = driver.find_element(By.ID, "Role__c")
    role = Select(drop_down_2)
    role.select_by_visible_text("Enterprise Architect")
    time.sleep(5)

    driver.find_element(By.ID, "emailOptin").click()
    driver.find_element(By.ID, "Free_Trial_Opt_In__c").click()
    time.sleep(5)

