import json
# import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdrivermanager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().download_and_install())
driver.implicitly_wait(2)
driver.get("http://saviconsultancy.com/")

# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


class MyTestCase1:
    f = open('savi_home.json')
    text = json.load(f)
    # print(driver.title)
    # time.sleep(5)
    # print("JSON DATA: ", text)

    def test_one(self):
        displayed_value_1 = self.text.get('disp1')
        text1 = driver.find_element(By.XPATH, "//a[normalize-space()='Home']").text
        assert text1 == displayed_value_1, 'Not Matched'

    def test_two(self):
        displayed_value_2 = self.text.get('disp2')
        text2 = driver.find_element(By.XPATH, "//a[normalize-space()='Services']").text
        assert text2 == displayed_value_2

    def test_three(self):
        displayed_value_3 = self.text.get('disp3')
        text3 = driver.find_element(By.XPATH, "//a[normalize-space()='Products']").text
        assert text3 == displayed_value_3

    def test_four(self):
        displayed_value_4 = self.text.get('disp4')
        text4 = driver.find_element(By.XPATH, "//a[normalize-space()='About Us']").text
        assert text4 == displayed_value_4

    def test_five(self):
        displayed_value_5 = self.text.get('disp5')
        text5 = driver.find_element(By.XPATH, "//a[normalize-space()='Contact Us']").text
        assert text5 == displayed_value_5

    def test_six(self):
        displayed_value_6 = self.text.get('disp6')
        text6 = driver.find_element(By.XPATH, "//h1[normalize-space()='SAVI Consultancy Services Limited Welcomes You']").text
        assert text6 == displayed_value_6

    def test_seven(self):
        displayed_value_7 = self.text.get('disp7')
        text7 = driver.find_element(By.XPATH, "//p[@class='mt-3 mb-md-5 mb-4']").text
        assert text7 == displayed_value_7

    def test_eight(self):
        displayed_value_8 = self.text.get('disp8')
        text8 = driver.find_element(By.CLASS_NAME, "btn-primary").text
        assert text8 == displayed_value_8

    driver.close()
# with open('file1.json') as f:
#    text = json.load(f)
#    abc=text.get('disp1')
# print("JSON DATA: ", abc)

# link_createlink_linktext.click()


# print(text1)
# def test_1():
#     assert text1 == displayed_value_1
# print(text2)
# def test_2():
#     assert text2 == displayed_value_2
# print(text3)
# def test_3():
#     assert text3 == displayed_value_3
# print(text4)
# def test_4():
#     assert text4 == displayed_value_4
# print(text5)
# def test_5():
#     assert text5 == displayed_value_5
# print(text6)
# def test_6():
#     assert text6 == displayed_value_6
# print(text6)
# def test_7():
#     assert text7 == displayed_value_7
# print(text8)
# def test_8():
#     assert text8 == displayed_value_8
