from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com/Instant-Pot-Plus-60-Programmable/dp/B01NBKTPTS/?th=1")

#price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
#price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
#print(f"the price is {price_dollar.text}.{price_cents.text}")

search_bar = driver.find_element( value="q")
print(search_bar.get_attribute("placeholder"))
button = driver.find_element(value="submit")
print(button.size)

#driver.close()
#driver.quit()

