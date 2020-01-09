from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://way2automation.com/way2auto_jquery/index.php")
with open('page.html', 'w') as file:
    file.write(driver.page_source)
driver.close()