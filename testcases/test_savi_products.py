from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import json
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(2)
driver.get("http://saviconsultancy.com/")
#print(driver.title)

'''driver.find_element(By.NAME, 'loginForm:accountId').send_keys("spadmin")
time.sleep(2)
driver.find_element(By.NAME, 'loginForm:password').send_keys("admin")
time.sleep(2)
driver.find_element(By.NAME, 'loginForm:loginButton').click()
print(driver.title)'''

link_createlink_linktext=driver.find_element(By.LINK_TEXT,"Products")
link_createlink_linktext.click()
time.sleep(5)

f = open('savi_products.json')
text=json.load(f)
print("JSON DATA: ", text)
displayed_value_1=text.get('disp1')
#print(displayed_value_1)
displayed_value_2=text.get('disp2')
displayed_value_3=text.get('disp3')


# with open('file1.json') as f:
#    text = json.load(f)
#    abc=text.get('disp1')
# print("JSON DATA: ", abc)

#link_createlink_linktext.click()
text1=link_createlink_linktext=driver.find_element(By.CLASS_NAME,'title-color').text
text2=link_createlink_linktext=driver.find_element(By.XPATH,"//p[@class='mt-3 mb-md-5 mb-4']").text
text3=link_createlink_linktext=driver.find_element(By.XPATH,"//a[normalize-space()='Get Started']").text

print(text1)
def test_1():
    assert text1 == displayed_value_1
print(text2)
def test_2():
    assert text2 == displayed_value_2
print(text3)
def test_3():
    assert text3 == displayed_value_3



# link_createlink_linktext=driver.find_element(By.CLASS_NAME,'btn-primary')
# link_createlink_linktext.click()
# time.sleep(5)



driver.close()


'''def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5

def test_abc():
    assert 5 == 5

def test_xyz():
    assert 3 == 5

link_createlink_linktext=driver.find_element(By.LINK_TEXT,'Services')
link_createlink_linktext.click()
time.sleep(5)

link_createlink_linktext=driver.find_element(By.LINK_TEXT,'Products')
link_createlink_linktext.click()
time.sleep(5)

link_createlink_linktext=driver.find_element(By.LINK_TEXT,'About Us')
link_createlink_linktext.click()
time.sleep(5)

link_createlink_linktext=driver.find_element(By.LINK_TEXT,'Contact Us')
link_createlink_linktext.click()
time.sleep(5)'''

'''mylinkbtn=driver.find_element(By.ID,'quicklinkButton')
mylinkbtn.click()
link_managelink_id=driver.find_element(By.ID,'quickLinkCategoryManage')
link_managelink_id.click()
link_createlink_linktext=driver.find_element(By.LINK_TEXT,'Create Identity')
link_createlink_linktext.click()
time.sleep(5)
textbox_identityname_xpath=driver.find_element(By.XPATH,'//label[text()="    Identity Name     "]/following-sibling::input').send_keys("Shyam")
#abc=WebDriverWait(driver,10).until(EC.visibility_of_element_located(textbox_identityname_xpath))
#abc.send_keys("Shyam")'''







'''def select_values(element,value):
	select=select(element)
	select.select_by_visible_text(value)'''