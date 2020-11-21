from selenium import webdriver


#----------------------------------------------------------------------
# 在这里填入你的学号
your_student_id='2020abcd'
# 你的统一认证登录密码
your_password='your_password'
#----------------------------------------------------------------------




chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--disable-dev-shm-using")
chromeOptions.add_argument("--headless")
chromeOptions.add_argument('--no-sandbox')
driver = webdriver.Chrome(chrome_options=chromeOptions)

# 打开ipgw.neu.edu.cn
driver.get('http://ipgw.neu.edu.cn')

# 关键：点击“学生电子邮件按钮”，帮助解决登录失败的神秘错误
button_student_mail_system=driver.find_element_by_css_selector('a.nav-item:nth-child(3)')
button_student_mail_system.click()

# 填入学号和密码
botton_student_id=driver.find_element_by_css_selector('#un')
botton_student_id.send_keys(your_student_id)
botton_password=driver.find_element_by_css_selector('#pd')
botton_password.send_keys(your_password)

# 点击登录
botton_login=driver.find_element_by_css_selector('#index_login_btn')
botton_login.click()
