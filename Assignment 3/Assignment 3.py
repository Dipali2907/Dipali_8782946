# Importing required libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Bluenotes homepage
driver.get("https://blnts.com/")
driver.maximize_window()  # Maximizing the browser window
time.sleep(5)

# Clicking on the "Today's Offers" link on the header
todays_offers_link = driver.find_element("xpath","/html/body/div[3]/div/header/div/nav/ul/li[1]")
todays_offers_link.click()

# Waiting for the page to load
time.sleep(5)

# Clicking on "3 for $21" link
three_for_21_link = driver.find_element("xpath","/html/body/div[3]/div/header/div/nav/ul/li[1]/div/ul/li[2]/a")
three_for_21_link.click()

# Waiting for the page to load
time.sleep(10)

# # Selecting a product from the  results
# # Product_link = driver.find_element_by_css_selector("span[data-component-type='s-product-image'] a")
product_link = driver.find_element("xpath","/html/body/div[3]/main/div[6]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/a/img[2]")
# # Product_link = driver.find_element("By.CSS_SELECTOR","span[data-component-type='s-product-image'] a")
product_link.click()
#
#
# # Waiting for the product details page to load
time.sleep(10)


# Clicking on the "L/G" size button
size_button = driver.find_element("xpath", "/html/body/div[3]/main/div[1]/div[2]/div[2]/div[2]/div[1]/form/div[1]/div[2]/div[2]/label[3]/span")
size_button.click()

# Waiting for the size selection to take effect
time.sleep(10)

# # Adding the Product to the wishlist
add_to_wishlist_button = driver.find_element("xpath","/html/body/div[3]/main/div[1]/div[2]/div[2]/div[2]/div[1]/form/div[6]/div/input[2]")
add_to_wishlist_button.click()
time.sleep(5)

# # Clicking on the login button
Login_button = driver.find_element("xpath","/html/body/div[3]/main/div/form/p/a[2]")
Login_button.click()
time.sleep(5)


# Closing the webdriver
driver.quit()
