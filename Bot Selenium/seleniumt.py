import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import os

driver = webdriver.Chrome(
    executable_path="/Users/TiagoC/Desktop/chromedriver"
)
driver.get("https://trcoelhoo.github.io/AS-FARMWEB/")
f = open("results.txt", "a")
driver.maximize_window()
time.sleep(1)
driver.find_element_by_xpath('/html/body/header/nav/div[1]/div[2]/ul/li[5]/a').click()
time.sleep(1)
#driver.switch_to.frame("textarea_iframe")
driver.find_element_by_id("email").send_keys("test")
time.sleep(1)
driver.find_element_by_id("password").send_keys("testpass")
time.sleep(1)
driver.find_element_by_class_name("btnadmin1").click()
time.sleep(1)
f.write("Dei login como fornecedor!\n")
driver.find_element_by_xpath('/html/body/header/nav/div[1]/div[2]/ul/li[5]/a').click()
time.sleep(1)
driver.find_element_by_class_name("btnadmin3").click()
time.sleep(1)
f.write("Adicionei Produtos da database!\n")
driver.find_element_by_class_name("logo").click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/header/nav/div[1]/div[2]/ul/li[6]/a').click()
time.sleep(1)
f.write("Sai da conta do fornecedor!\n")
driver.find_element_by_xpath('/html/body/header/nav/div[1]/div[2]/ul/li[4]/a').click()
time.sleep(1)
#driver.switch_to.frame("textarea_iframe")
driver.find_element_by_id("email").send_keys("test")
time.sleep(1)
driver.find_element_by_id("password").send_keys("testpass")
time.sleep(1)
driver.find_element_by_class_name("btnadmin1").click()
time.sleep(1)
f.write("Dei login como cliente!\n")
driver.find_element_by_xpath('/html/body/header/nav/div[1]/div[2]/ul/li[2]/a').click()
time.sleep(1)
f.write("Entrei na loja!\n")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)
driver.find_element_by_class_name("add-to-cart").click()
time.sleep(1)
f.write("Adicionei uma banana ao carrinho!\n")
driver.find_element_by_class_name("add-to-cart").click()
time.sleep(1)
f.write("Adicionei duas bananas ao carrinho!\n")
driver.find_element_by_class_name("add-to-cart").click()
time.sleep(1)
f.write("Adicionei tres bananas ao carrinho!\n")
driver.find_element_by_class_name("checkout").click()
time.sleep(1)
f.write("Dei checkout!\n")
driver.find_element_by_link_text("Place Order").click()
time.sleep(1)
f.write("Completei o pedido!\n")
driver.find_element_by_xpath('/html/body/header/nav/div[1]/div[2]/ul/li[3]/a').click()
time.sleep(1)
driver.find_element_by_class_name("fa-gift").click()
time.sleep(1)
f.write("Cheguei a pagina do historico de encomendas!\n")
driver.find_element_by_class_name("track").click()
f.write("Cheguei a pagina de tracking de encomendas!\n")
time.sleep(1)
f.write("Completei o teste!\n")
print (os.path.abspath("results.txt"))
f.close()
driver.quit();