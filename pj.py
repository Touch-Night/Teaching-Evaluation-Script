# 导入相关库
import requests
import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import pyautogui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
username = input('输入你的帐号: ')
password = input('输入你的密码: ')
num = input('请输入所评教的人数：')
# 此驱动应和exe文件或py文件在同目录下
s = Service('msedgedriver.exe')
# 我校教务处官网
web_neuq = 'https://ids.neuq.edu.cn/authserver/login?service=http%3A%2F%2Fjwxt.neuq.edu.cn%2Feams%2FhomeExt.action'
options = webdriver.EdgeOptions()
options.add_argument('--window-size=1960,1080')
driver = webdriver.Edge(service=s, options=options)
driver.get(web_neuq)
user_input = driver.find_element(By.XPATH,'//*[@id="username"]')
pw_input = driver.find_element(By.XPATH,'//*[@id="password"]')
login_btn = driver.find_element(By.XPATH,'//*[@id="casLoginForm"]/div/div[1]/button')
time.sleep(5)
user_input.send_keys(username)
pw_input.send_keys(password)
time.sleep(1)
login_btn.click()
print('等待5s使网页加载完毕')
time.sleep(5)
for i in range(int(num)):
    try:
        # 这是当第一行的老师人数大于1时
        print('开始一类评价')
        element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/table/tbody/tr[1]/td[6]/a[1]/span'))
    )
        element.click()
        print('等待2s...')
        time.sleep(2)
        # 进入评价选项界面,全部选优秀
        driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div[2]/div/div[2]/ul/li[1]/input').click()
        time.sleep(0.5) # 手动设置延时
        driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div[2]/div/div[3]/ul/li[1]/input').click()
        time.sleep(0.5)
        driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div[2]/div/div[4]/ul/li[1]/input').click()
        time.sleep(0.5)
        driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div[2]/div/div[5]/ul/li[1]/input').click()
        time.sleep(0.5)
        driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div[2]/div/div[6]/ul/li[1]/input').click()
        time.sleep(0.5)
        # 此项为输入文字评价
        driver.find_element(By.XPATH,'//*[@id="question_6"]/textarea').click()
        # 调用pyautogui的相关库，模拟键盘打印出中文（第一次用没什么问题，但上次评价时全部输入了英文，这个等待改进
        pyautogui.typewrite('wu')
        pyautogui.press('space')
        time.sleep(1)
        # 点击页面内的提交按钮
        driver.find_element(By.XPATH,'//*[@id="sub"]').click()
        pyautogui.press('enter')
        print("评教1完毕")
    except:
        # 第一行只有一个老师
        print('开始二类评价')
        # 以下代码基本和上一个try里的一样，直接可以封装在一个函数从而精简代码。这个也留时间再说
        element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/table/tbody/tr[1]/td[6]/a/span'))
    )
        element.click()
        time.sleep(20)
        driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div[2]/div/div[2]/ul/li[1]/input').click()
        time.sleep(0.5)
        driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div[2]/div/div[3]/ul/li[1]/input').click()
        time.sleep(0.5)
        driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div[2]/div/div[4]/ul/li[1]/input').click()
        time.sleep(0.5)
        driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div[2]/div/div[5]/ul/li[1]/input').click()
        time.sleep(0.5)
        driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div[2]/div/div[6]/ul/li[1]/input').click()
        time.sleep(0.5)
        driver.find_element(By.XPATH,'//*[@id="question_6"]/textarea').click()
        pyautogui.typewrite('wu')
        pyautogui.press('space')
        time.sleep(1) 
        driver.find_element(By.XPATH,'//*[@id="sub"]').click()
        pyautogui.press('enter')
        print('等待2s...')
        print("评教2完毕")
print('评教完成')



