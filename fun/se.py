def click_by_id(driver, ID):
    obj = driver.find_element_by_id(ID)
    obj.click()

def send_keys_by_xpath(driver, xpath, keys):
    obj = driver.find_element_by_xpath(xpath)
    obj.send_keys(keys)

def click_by_xpath(driver, xpath):
    obj = driver.find_element_by_xpath(xpath)
    obj.click()

def send_keys_by_name(driver, name, keys):
    obj = driver.find_element_by_name(name)
    obj.send_keys(keys)

def click_by_name(driver, name):
    obj = driver.find_element_by_name(name)
    obj.click()
