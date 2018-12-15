from appium import webdriver
from selenium import webdriver

def get_driver():
    driver = webdriver.Firefox()
    driver.get("http://www.tpshop.com/Home/user/login.html")
    return driver


