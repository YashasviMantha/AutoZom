from selenium import webdriver
import time
import json


with open("keys", "r") as file:
    raw_file = file.readlines()
    raw_file = "".join(raw_file)
    data = json.loads(raw_file)





driver = webdriver.Firefox()
driver.get("https://login.gitam.edu/Login.aspx")

wait = 3

time.sleep(wait)

driver.find_element_by_id("password").send_keys(data["password"])
driver.find_element_by_id("txtusername").send_keys(data["username"])



# driver.find_element_by_class("btn signin-height btn-orange btn-orange-full-width").click()

driver.find_element_by_id("Submit").click()

time.sleep(wait)

driver.get("https://login.gitam.edu/route.aspx?id=GLEARN&type=S")


# input()
driver.close()