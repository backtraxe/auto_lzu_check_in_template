from selenium import webdriver

username = ''
password = ''

# 打开网址
options = webdriver.ChromeOptions()
options.add_argument('--headless') # 后台运行
options.add_argument('--disable-gpu')
options.add_argument('user-agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"')
driver = webdriver.Chrome(options=options)
driver.get('http://my.lzu.edu.cn/')

# 自动登录
driver.find_element_by_id('username').send_keys(username)
driver.find_element_by_id('password').send_keys(password)
driver.find_element_by_xpath('//button[@type="submit"]').click()
driver.implicitly_wait(2)

# 健康打卡
driver.find_element_by_xpath('//*[@id="my-apps"]/li[@data-id="76"]').click()
driver.implicitly_wait(2)

driver.switch_to.frame('iframe')
driver.implicitly_wait(2)

# 判断是否二次打卡
try:
    driver.find_element_by_xpath('//*[text()="确定"]').click()
    driver.implicitly_wait(2)
except:
    pass

# 上传
driver.find_element_by_xpath('//*[text()="上报"]').click()
driver.implicitly_wait(2)

# 判断打卡是否成功
try:
    driver.find_element_by_xpath('//*[text()="确定"]')
    print(username, '打卡成功！')
except:
    print(username, '打卡失败！')

# 退出
driver.quit()
