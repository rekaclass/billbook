def login(driver, user, password):
    userName = driver.find_element_by_name("uname").send_keys(user)
    password = driver.find_element_by_name("pass").send_keys(password)
    enterkey = driver.find_element_by_xpath("//*[@id='sign_in']/div[3]/button").click()
