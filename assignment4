from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#1
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
browser = webdriver.Firefox(executable_path="c:\\geckodriver.exe")

driver.get("https://www.ynet.co.il")
#2

title = driver.title
sleep(3)
driver.refresh()
if title==driver.title:
    print("looks good")

#3
# no change in elements between browsers

#4
driver.get("https://translate.google.com")
driver.find_element_by_id("source").send_keys("אנציקלופדיה")
sleep(3)
#5

driver.get("https://www.youtube.com/")
driver.find_element_by_id("search").send_keys("liquid tension experiment")
driver.find_element_by_id("search-icon-legacy").click()
sleep(3)
#6
#driver.get("https://translate.google.com")
#button1 = driver.find_element_by_xpath("//*[@id="sugg-item-en"]")
#button2 = (driver.find_element_by_xpath("//*[@id="sugg-item-es"]"))
#print(button1 + button2)

#7
driver.get("https://www.facebook.com/")
driver.find_element_by_id("email").send_keys("bla@bla.com")
driver.find_element_by_id("pass").send_keys("thisisnotmypassword")
driver.find_element_by_id("loginbutton").click()

###EXTRA###
driver.get("https://www.ynet.co.il")
driver.delete_all_cookies()
cookies_list = driver.get_cookies()
cookies_dict = {}
for cookie in cookies_list:
    cookies_dict[cookie['name']] = cookie['value']

print(cookies_dict)

###2
driver.get("https://github.com")
driver.find_element_by_name("q").send_keys("selenium")
driver.find_element_by_name("q").send_keys(u'\ue007')

###3
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
browser = webdriver.Chrome(executable_path=path_to_Ie, chrome_options=chrome_options)
