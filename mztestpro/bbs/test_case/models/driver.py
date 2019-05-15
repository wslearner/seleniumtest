from selenium.webdriver import Remote
from selenium import webdriver


# 启动浏览器
def browser():
    host = '127.0.0.1:4444'
    dc = {'browserName': 'firefox'}
    driver = Remote(command_executor='http://'+host+'/wd/hub',
                    desired_capabilities=dc)
    return driver


