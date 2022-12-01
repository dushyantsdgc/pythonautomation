from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


def test_login_troups():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(3)
    driver.get("https://truopssit33.sdgc.com/identityiq/login.jsf?prompt=true")
    driver.find_element(By.NAME,'loginForm:accountId').send_keys("spadmin")
    time.sleep(8)
    driver.find_element(By.NAME,'loginForm:password').send_keys("admin")
    time.sleep(8)
    driver.find_element(B.y.NAME,'loginForm:loginButton').click()
    print(driver.title)

    time.sleep(8)
    driver.quit()