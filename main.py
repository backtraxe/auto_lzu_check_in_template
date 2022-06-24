from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import sys

# 打开网址
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # 后台运行
options.add_argument('--disable-gpu')
options.add_argument("user-agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36'")

driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.get('http://my.lzu.edu.cn/')

# 自动登录
driver.find_element(By.ID, 'username').send_keys(sys.argv[1])
driver.find_element(By.ID, 'password').send_keys(sys.argv[2])
driver.find_element(By.XPATH, '//button[@type="submit"]').click()
driver.implicitly_wait(2)

# 查看全部应用
driver.find_element(By.CLASS_NAME, 'right').click()
driver.implicitly_wait(2)

# 健康打卡
driver.find_element(By.XPATH, '//*[@id="my-apps"]/li[@data-id="76"]').click()
driver.implicitly_wait(2)

# 切换到右侧弹出的子页面
driver.switch_to.frame('iframe')
driver.implicitly_wait(2)

# 判断是否二次打卡
try:
    driver.find_element(By.XPATH, '//*[text()="确定"]').click()
    driver.implicitly_wait(2)
except:
    # 不处理，直接跳过
    ...

# 点击上报进行打卡
driver.find_element(By.XPATH, '//*[text()="上报"]').click()
driver.implicitly_wait(2)

# 判断打卡是否成功
button = driver.find_element(By.XPATH, '//*[text()="确定"]')

# 退出
driver.quit()
