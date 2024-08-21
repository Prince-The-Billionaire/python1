from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://moodle.cu.edu.ng/")

input_element = driver.find_element(By.LINK_TEXT,"Log in")

input_element.click()

next_element = driver.find_element(By.ID,'username')
next_element.send_keys('daniel.princewill@stu.cu.edu.ng')
pass_element = driver.find_element(By.ID, 'password')
pass_element.send_keys('princewill2005')

button_element = driver.find_element(By.ID,"kc-login")

button_element.click()
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH,"//*[@id=\"page-container-0\"]/div/div/div[1]/a"))
)

card_element = driver.find_element(By.XPATH,"//*[@id=\"page-container-0\"]/div/div/div[1]/a")
card_element.click()

text_heading = driver.find_element(By.XPATH,"//*[@id=\"page-header\"]/div/div/div/div[1]/div[1]/div/div/h1")
text = text_heading.text
course_title = text.split(':')
course_code = course_title[0]

course_eval = driver.find_element(By.LINK_TEXT,"2023/2024 OMEGA SEMESTER COURSE EVALUATION")
course_eval.click()

time.sleep(10)
