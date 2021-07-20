import os
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

def get_driver():
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.cache.disk.enable", False)
    profile.set_preference("browser.cache.memory.enable", False)
    profile.set_preference("browser.cache.offline.enable", False)
    profile.set_preference("network.http.use-cache", False)

    profile.set_preference('network.proxy.type', 1)
    profile.set_preference('network.proxy.socks', "127.0.0.1")
    profile.set_preference('network.proxy.socks_port', 9050)

    binary = FirefoxBinary(os.path.abspath("firefox/firefox.exe"))
    driver = webdriver.Firefox(profile,firefox_binary=binary)
    return driver

