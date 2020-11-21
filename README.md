NEU ipgw 东北大学 IP控制网关 模拟浏览器登录 解决认证失败(Login Excetion)问题

一、介绍

​    在使用其它ipgw登录工具时，经常出现登陆失败的现象，从此持续较长一段时
间内，手动在网页端用统一身份认证登录会提示portal not response，并提示登
录失败。经过一番摸索，我发现在https://ipgw.neu.edu.cn 页面点击“学生电子邮
件”按钮后，再次登录即可登录成功。因此我写了一段简单脚本来模拟此登录过程。



二、使用条件

​    本脚本通过使用selenium的webdriver创建无头浏览器并登录，因此在使用前需要：

​    1.保证你已安装Firefox/Chromium/Chrome/Edge/Internet Explorer/Safari/
Opera浏览器之一。

​    2.安装selenium包。
​      pip install selenium

​    3.安装WebDriver（跨平台）以提供对浏览器的控制。
​      (在这儿)https://www.selenium.dev/documentation/en/webdriver/driver_requirements/#quick-reference



三、使用方法

​    1.打开login_ipgw.py并填入你的学号和密码。

​    2.如果你的浏览器不是Chromium/Chrome，需要简单地修改代码以适配浏览器。

​      (像这样)https://www.selenium.dev/documentation/en/webdriver/driver_requirements/#chromiumchrome
