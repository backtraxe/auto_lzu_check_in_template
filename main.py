from selenium import webdriver
from selenium.webdriver.common.by import By

username = secrets.USERNAME
password = secrets.PASSWORD

# 打开网址
options = webdriver.ChromeOptions()
options.add_argument('--headless') # 后台运行
options.add_argument('--disable-gpu')
options.add_argument('user-agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"')

driver = webdriver.Chrome(options=options)
driver.get('http://my.lzu.edu.cn/')

# 自动登录
driver.find_element(By.ID, 'username').send_keys(username)
driver.find_element(By.ID, 'password').send_keys(password)
driver.find_element(By.XPATH, '//button[@type="submit"]').click()
driver.implicitly_wait(2)

# 健康打卡
driver.find_element(By.XPATH, '//*[@id="my-apps"]/li[@data-id="76"]').click()
driver.implicitly_wait(2)

# 右边子页面
driver.switch_to.frame('iframe')
driver.implicitly_wait(2)

# 判断是否二次打卡
try:
    driver.find_element(By.XPATH, '//*[text()="确定"]').click()
    driver.implicitly_wait(2)
except:
    ...

# 上传
driver.find_element(By.XPATH, '//*[text()="上报"]').click()
driver.implicitly_wait(2)

# 判断打卡是否成功
try:
    driver.find_element(By.XPATH, '//*[text()="确定"]')
    flag = 1
except:
    flag = 0

msg = 'SUCCEEDED!' if flag == 1 else 'FAILED!'
n = len(username) + len(msg) + 5
print('#' * n)
print('#', username, msg, '#')
print('#' * n)

# 退出
driver.quit()
