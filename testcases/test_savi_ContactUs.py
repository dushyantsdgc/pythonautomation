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
time.sleep(2)
#print(driver.title)

'''driver.find_element(By.NAME, 'loginForm:accountId').send_keys("spadmin")
time.sleep(2)
driver.find_element(By.NAME, 'loginForm:password').send_keys("admin")
time.sleep(2)
driver.find_element(By.NAME, 'loginForm:loginButton').click()
print(driver.title)'''

link_createlink_linktext=driver.find_element(By.XPATH ,"//a[normalize-space()='Contact Us']")
link_createlink_linktext.click()
time.sleep(5)

f = open('savi_ContactUs.json')
text=json.load(f)
#print("JSON DATA: ", text)
displayed_value_1=text.get('disp1')
#print(displayed_value_1)
displayed_value_2=text.get('disp2')
displayed_value_3=text.get('disp3')
displayed_value_4=text.get('disp4')
displayed_value_5=text.get('disp5')
displayed_value_6=text.get('disp6')
displayed_value_7=text.get('disp7')
displayed_value_8=text.get('disp8')
displayed_value_9=text.get('disp9')
displayed_value_10=text.get('disp10')
displayed_value_11=text.get('disp11')
displayed_value_12=text.get('disp12')


# with open('file1.json') as f:
#    text = json.load(f)
#    abc=text.get('disp1').
# print("JSON DATA: ", abc)

#link_createlink_linktext.click()
text1=link_createlink_linktext=driver.find_element(By.XPATH,"//h3[normalize-space()='Contact Us']").text
text2=link_createlink_linktext=driver.find_element(By.XPATH,"//a[@href='tel:{ContactConstants.COMPANY_PHONE}']").text
text3=link_createlink_linktext=driver.find_element(By.CLASS_NAME,"mail").text
text4=link_createlink_linktext=driver.find_element(By.XPATH,"//p[contains(text(),'72 Castlegate Grove')]").text
text5=link_createlink_linktext=driver.find_element(By.XPATH,"//input[@id='scslName']").text
text6=link_createlink_linktext=driver.find_element(By.XPATH,"//input[@name='lastName']").text
text7=link_createlink_linktext=driver.find_element(By.XPATH,"//input[@id='scslSender']").text
text8=link_createlink_linktext=driver.find_element(By.XPATH,"//input[@id='scslPhone']").text
text9=link_createlink_linktext=driver.find_element(By.XPATH,"//input[@id='scslSubject']").text
text10=link_createlink_linktext=driver.find_element(By.XPATH,"//textarea[@id='message']").text
text11=link_createlink_linktext=driver.find_element(By.XPATH,"//button[normalize-space()='Send Message']").text
text12=link_createlink_linktext=driver.find_element(By.XPATH,"//h5[normalize-space()='Click below checkbox to verify you are human']").text


#print(text1)
def test_1():
    assert text1 == displayed_value_1
#print(text2)
def test_2():
    assert text2 == displayed_value_2
#print(text3)
def test_3():
    assert text3 == displayed_value_3
#print(text4)
def test_4():
    assert text4 == displayed_value_4
#print(text5)
def test_5():
    assert text5 == displayed_value_5
#print(text6)
def test_6():
    assert text6 == displayed_value_6
#print(text6)
def test_7():
    assert text7 == displayed_value_7
#print(text3)
def test_8():
    assert text8 == displayed_value_8
#print(text4)
def test_9():
    assert text9 == displayed_value_9
#print(text5)
def test_10():
    assert text10 == displayed_value_10
#print(text6)
def test_11():
    assert text11 == displayed_value_11
#print(text6)
def test_12():
    assert text12 == displayed_value_12



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