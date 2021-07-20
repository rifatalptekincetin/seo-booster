from selenium.webdriver.common.keys import Keys
from torcontrol import renew_ip,start_tor
from firefoxcontrol import get_driver
from random import randrange
import time

keywords=["totobo","totobo giris"]

target="totoboiletisim.com"

target_xpath="/html/body/div/div/div/div/div/div/div/div/div//a[contains(@href,'{}')]".format(target)

google="https://www.google.com/"

depth=5

bl=[]
with open("blacklist.txt","r") as f:
    [bl.append(i) for i in f.read().split("\n") if i]

def my_ip(driver):
    driver.get("https://api.ipify.org/")
    return driver.find_elements_by_xpath("/html/body")[0].text

def exposed(driver):
    return "sıra dışı bir trafik algıladı" in driver.find_elements_by_xpath("/html/body")[0].text

def restart(driver):
    driver.quit()
    renew_ip()
    time.sleep(2)
    return get_driver()

start_tor()
time.sleep(5)
driver=get_driver()

while 1:
    for keyword in keywords:
        try:
            ip=my_ip(driver)
            if ip in bl:
                driver = restart(driver)
            else:
                driver.get(google)
                ke = driver.find_elements_by_xpath("//*[contains(text(), 'Kabul ediyorum')]")
                if ke:
                    ke[0].click()
                sb=driver.find_elements_by_xpath("//input[@name='q']")
                if sb:
                    sb[0].click()
                    sb[0].send_keys(keywords[0])
                    sb[0].send_keys(Keys.ENTER)
                time.sleep(3)
                if exposed(driver):
                    with open("blacklist.txt","a") as f:
                        f.write("\n"+ip)
                    bl.append(ip)
                else:
                    for i in range(depth):
                        my_target=results=driver.find_elements_by_xpath(target_xpath)
                        if my_target:
                            my_target[0].click()
                            time.sleep(10)
                            print("amin")
                            break
                        else:
                            nextbtn=driver.find_elements_by_xpath("//*[@id='pnnext']")
                            if nextbtn:
                                nextbtn[0].click()
                                time.sleep(3)
                    #last page
                    my_target=results=driver.find_elements_by_xpath(target_xpath)
                    if my_target:
                        my_target[0].click()
                        time.sleep(10)
                        print("amin")
                driver = restart(driver)
        except:
            driver = restart(driver)
            
            

##driver.find_elements_by_xpath("//span[contains(text(), 'Kabul ediyorum')]/ancestor::button")


##while 1:
##    try:
##        driver=get_driver()
##        driver.get(url)
##        butonkabul=driver.find_elements_by_xpath("//span[contains(text(), 'Kabul ediyorum')]/ancestor::button")
##        if(butonkabul):
##            butonkabul[0].click()
##        time.sleep(2)
##        try:
##            video = driver.find_element_by_id('movie_player')
##        except:
##            video=0
##        if(video):
##            video.send_keys(Keys.SPACE) #hits space
##            for i in range(randrange(2,10)):
##                video.send_keys(Keys.ARROW_RIGHT)
##                time.sleep(1)
##                butonreklam=driver.find_elements_by_xpath("//span[contains(text(), 'Reklamları Atla')]/ancestor::button")
##                if(butonreklam):
##                    butonreklam[0].click()
##                    i=0
##    except:
##        continue
##    finally:
##        driver.quit()
##        renew_ip()
    
