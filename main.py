# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
import json
import os
from pathlib import Path


def waitUntilVisible(browser: WebDriver, by_: By, selector: str, time_to_wait: int = 10):
    """Wait until visible"""
    WebDriverWait(browser, time_to_wait).until(
        ec.visibility_of_element_located((by_, selector)))

def click_mission(email,pwd):
    start_time=time.time()
    # 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
    driver = webdriver.Chrome()# 谷歌
    #登录

    driver.get('https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=14&id=264960&wreply=https%3a%2f%2fcn.bing.com%2fsecure%2fPassport.aspx%3fedge_suppress_profile_switch%3d1%26requrl%3dhttps%253a%252f%252fcn.bing.com%252f%253fwlexpsignin%253d1%26sig%3d349CFDF412B8677F2425EEB213526600%26nopa%3d2&wp=MBI_SSL&lc=2052&pcexp=false&CSRFToken=8acdec74-02ec-491e-a870-2833ff74dcfe&aadredir=1&nopa=2')

    time.sleep(3)
    print("login on pc")
    driver.find_element(By.ID,'i0116').send_keys(email)
    # Click next
    driver.find_element(By.ID, 'idSIButton9').click()

    # Enter password
    time.sleep(3)
    waitUntilVisible(driver, By.ID, 'loginHeader', 10)
    x=1
    #确保pc上能搜到
    while x:
        try:
            driver.find_element(By.ID, "i0118")
            x=0
        except:
            x=1

    driver.find_element(By.ID, "i0118").send_keys(pwd)
    time.sleep(2)

    driver.find_element(By.ID, 'idSIButton9').click()
    time.sleep(2)
    # driver.find_element(By.ID, 'idBtn_Back').click()
    #driver.quit()#退出
    time.sleep(2)
    driver.get('https://bing.com/')
    time.sleep(5)
    x=1
    star_point=0
 #输出开始时的分数
    while x or star_point==0:
        try:
            star_point = int(driver.find_element(
                By.ID, 'id_rc').get_attribute('innerHTML'))
            x=0
        except:
            time.sleep(1)
            try:
            #确保bing上已经登录了
                driver.find_element(
                    By.ID, 'id_rc').click()
                x=1

            except:
                driver.refresh()
                x=1


    print(email+"  start point="+str(star_point))
    print("search mission on pc")
    #pc 搜索
    for i in range(37):
        try:
            url_x="https://cn.bing.com/search?q=abc"+str(i)
            driver.get(url_x)
            time.sleep(0.5)
        except:
            continue






    driver.get('https://rewards.bing.com/')
    m=len(driver.find_elements(By.CLASS_NAME,'ds-card-sec'))
# 依次点击m次任务
    print("click mission on pc")
    for i in range(m):
        if i == 6 or i == 7:# 每周天气那个会出错，还未解决
            continue
        driver.find_elements(By.CLASS_NAME,'ds-card-sec')[i].click()
    try:
        driver.find_elements(By.CLASS_NAME, 'ds-card-sec')[6].click()
    except:
        print("6")
    try:
        driver.find_elements(By.CLASS_NAME, 'ds-card-sec')[7].click()
    except:
        print("6")
    time.sleep(2)
    driver.quit()

    print("login phone")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('mobileEmulation', {'deviceName': 'iPhone X'})  # 模拟iPhone X浏览
    driver = webdriver.Chrome(options=options)
    # 登录
    driver.get('https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=14&id=264960&wreply=https%3a%2f%2fcn.bing.com%2fsecure%2fPassport.aspx%3fedge_suppress_profile_switch%3d1%26requrl%3dhttps%253a%252f%252fcn.bing.com%252f%253fwlexpsignin%253d1%26sig%3d349CFDF412B8677F2425EEB213526600%26nopa%3d2&wp=MBI_SSL&lc=2052&pcexp=false&CSRFToken=8acdec74-02ec-491e-a870-2833ff74dcfe&aadredir=1&nopa=2')
    time.sleep(3)
    driver.find_element(By.ID, 'i0116').send_keys(email)
    # Click next
    driver.find_element(By.ID, 'idSIButton9').click()

    # Enter password
    time.sleep(3)
    waitUntilVisible(driver, By.ID, 'loginHeader', 10)
    x = 1
    while x:
        try:
            driver.find_element(By.ID, "i0118")
            x = 0
        except:
            x = 1

    driver.find_element(By.ID, "i0118").send_keys(pwd)
    time.sleep(2)

    driver.find_element(By.ID, 'idSIButton9').click()
    time.sleep(2)


    driver.get('https://bing.com/')

    time.sleep(1)
    time.sleep(5)
    x = 1

    print("get point")
    while x:
        try:
            driver.find_element(By.ID, 'mHamburger').click()
            x = 0
        except:
            x = 1
            print(1)
    time.sleep(5)
#搜索24次
    print("search mission on phone")
    for i in range(24):
        try:
            url_x="https://cn.bing.com/search?q=aaa"+str(i)
            driver.get(url_x)
            time.sleep(0.5)
            driver.find_element(By.ID, 'mHamburger').click()
            time.sleep(0.5)
        except:
            continue
 #获取分数
    time.sleep(2)
    x=1
    while x:
        try:
            driver.find_element(By.CLASS_NAME,'hb_value_col')
            point = int(driver.find_element(
                By.ID, 'fly_id_rc').get_attribute('innerHTML'))
            x=0
            print(0)
        except:
            x = 1
            driver.find_element(By.ID, 'mHamburger').click()
            print(1)
    point = int(driver.find_element(
        By.ID, 'fly_id_rc').get_attribute('innerHTML'))
    print(email+"  finish point="+str(point))
    time.sleep(3)
    driver.quit()


    # time.sleep(2)




    # print(end_point)#  结束时的point
    # earn_point=90+60+12+end_point-star_point
    # log=email+":"+str(earn_point)+"\n"+"当前分数："+str(end_point)
    # print(earn_point)
    #退出

    # print(f"the running time is :{end_time-start_time}s")
    end_time=time.time()

if __name__ == '__main__':
    global ACCOUNTS, ACCOUNTS_PATH
    ACCOUNTS_PATH = Path(__file__).parent / 'accounts.json'
    ACCOUNTS = json.load(open(ACCOUNTS_PATH, "r"))

    for ACCOUNT in ACCOUNTS:
        email = ACCOUNT['username']
        pwd = ACCOUNT['password']
        click_mission(email, pwd)
