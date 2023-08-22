##Login Through Chrome Browser
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://dev.deepthought.education/login")
#Login with Valid
driver.find_element(By.XPATH,"//input[@id='username']").send_keys("adityaraosutar27@gmail.com")
driver.find_element(By.XPATH,"//input[@id='password']").send_keys("AdityaSutar2799")
driver.find_element(By.XPATH,"//button[@id='login']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//a[@id='dropdownMenuButton']").click()
driver.find_element(By.XPATH,"//form[@class='dropdown-item']").click()
time.sleep(3)
#Login with Invalid credentials
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://dev.deepthought.education/login")

time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='username']").send_keys("adityaraosutar27@gmail.com")
driver.find_element(By.XPATH,"//input[@id='password']").send_keys("AdityaSutar")
driver.find_element(By.XPATH,"//button[@id='login']").click()
time.sleep(5)
