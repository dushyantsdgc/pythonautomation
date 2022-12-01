# from selenium.webdriver.common.by import By
# import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


def test_login_google():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get("http://www.google.com")
    assert driver.title == "Google"
    driver.quit()


def test_login_facebook():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get("http://www.facebook.com")
    print(driver.title)
    assert driver.title == "Facebook – log in or sign up"
    driver.quit()


def test_login_insta():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get("http://www.instagram.com")
    assert driver.title == "Instagram"
    driver.quit()


def test_login_gmail():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get("http://www.gmail.com")
    assert driver.title == "Gmail"
    driver.quit()