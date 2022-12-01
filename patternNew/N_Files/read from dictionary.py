# from selenium.webdriver.common.by import By
# import time
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium import webdriver
import json
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC

# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.implicitly_wait(2)
# driver.get("http://saviconsultancy.com/")
# #print(driver.title)

'''driver.find_element(By.NAME, 'loginForm:accountId').send_keys("spadmin")
time.sleep(2)
driver.find_element(By.NAME, 'loginForm:password').send_keys("admin")
time.sleep(2)
driver.find_element(By.NAME, 'loginForm:loginButton').click()
print(driver.title)'''

# link_createlink_linktext=driver.find_element(By.XPATH ,"//a[normalize-space()='Services']")
# link_createlink_linktext.click()
# time.sleep(5)



f = open('file2.json')

text=json.load(f)

print("JSON DATA: ", text)

abc=text.get('disp1')
print(abc)

# text=json.load(f)
# print('text')

# with open('file1.json') as f:
#    text = json.load(f)
#     abc=text.get('disp1')
#  print("JSON DATA: ", abc)

