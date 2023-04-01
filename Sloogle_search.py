from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# create a new Chrome driver instance
driver = webdriver.Chrome()

# navigate to Google
driver.get('https://www.google.com')

# wait for the search box element to be visible
wait = WebDriverWait(driver, 10)
search_box = wait.until(EC.visibility_of_element_located((By.NAME, 'q')))

# enter the search query "Python gigs"
search_box.send_keys('Python gigs')

# submit the search query
search_box.submit()

# wait for the search results to load
wait.until(EC.presence_of_element_located((By.ID, 'search')))

# do something
# ...

# close the driver
driver.quit()
