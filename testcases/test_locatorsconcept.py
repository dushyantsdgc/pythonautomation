from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(2)
driver.get("https://truopssit33.sdgc.com/identityiq/login.jsf?prompt=true")
print(driver.title)

driver.find_element(By.NAME, 'loginForm:accountId').send_keys("spadmin")
time.sleep(2)
driver.find_element(By.NAME, 'loginForm:password').send_keys("admin")
time.sleep(2)
driver.find_element(By.NAME, 'loginForm:loginButton').click()
print(driver.title)

mylinkbtn=driver.find_element(By.ID,'quicklinkButton')
mylinkbtn.click()
link_managelink_id=driver.find_element(By.ID,'quickLinkCategoryManage')
link_managelink_id.click()
link_createlink_linktext=driver.find_element(By.LINK_TEXT,'Create Identity')
link_createlink_linktext.click()
time.sleep(5)
textbox_identityname_xpath=driver.find_element(By.XPATH,'//label[text()="    Identity Name     "]/following-sibling::input').send_keys("Shyam")
#abc=WebDriverWait(driver,10).until(EC.visibility_of_element_located(textbox_identityname_xpath))
#abc.send_keys("Shyam")







'''def select_values(element,value):
	select=select(element)
	select.select_by_visible_text(value)'''