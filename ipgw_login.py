from selenium import webdriver


#----------------------------------------------------------------------
# 在这里填入你的学号
your_student_id='2020abcd'
# 你的统一认证登录密码
your_password='your_password'
#----------------------------------------------------------------------



# 用于已安装Chromium/Chrome浏览器及相应驱动
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--disable-dev-shm-using")
chromeOptions.add_argument("--headless")
chromeOptions.add_argument('--no-sandbox')
driver = webdriver.Chrome(chrome_options=chromeOptions)

# 用于已安装Firefox浏览器及相应驱动（未测试）
#driver = webdriver.Firefox()

# 打开ipgw.neu.edu.cn
driver.get('http://ipgw.neu.edu.cn')
driver.save_screenshot('1.png')

# 关键：点击“学生电子邮件按钮”，此时浏览器转跳到一个充满神秘参数的网址，
#       应该是这些参数解决了登录失败的错误。
# 由于那段文本只是一个超链接，因此直接转到对应地址
driver.get('http://stu.neu.edu.cn')
print('redirected to: '+driver.current_url)
driver.save_screenshot('2.png')

# 如果已经登录，则会转跳到学生邮箱登录界面，程序结束
if driver.current_url == 'https://stu.neu.edu.cn/':
    print('you may have been logged!')
    exit()


# 点击“连接到网络”按钮，进入登录界面
button_connect_network=driver.find_element_by_css_selector('a.btn:nth-child(1)')
button_connect_network.click()
driver.save_screenshot('3.png')

# 填入学号和密码
botton_student_id=driver.find_element_by_css_selector('#un')
botton_student_id.send_keys(your_student_id)
botton_password=driver.find_element_by_css_selector('#pd')
botton_password.send_keys(your_password)
driver.save_screenshot('4.png')

# 点击登录
botton_login=driver.find_element_by_css_selector('#index_login_btn')
botton_login.click()
driver.save_screenshot('5.png')
