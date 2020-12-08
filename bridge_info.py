from selenium import webdriver
import time
from tkinter import *


driver = webdriver.PhantomJS(executable_path=r'C:\phantomjs-2.1.1-windows\bin\phantomjs.exe ')
driver.get('https://www.glslw-glvm.com/R2/jsp/NiaBrdgStatus15min.jsp?language=E')
# time.sleep(5)

x = driver.find_elements_by_class_name("lgtextblack")
y = driver.find_elements_by_class_name("lgtextblack10")
z = driver.find_elements_by_id("status")

bridge_name = []
bridge_number = []
bridge_status = []

for i in x:
    bridge_name.append(i.text)
for i in y:
    bridge_number.append(i.text)
for i in z:
    bridge_status.append(i.text)

bridge_info = dict(zip(zip(bridge_name, bridge_number), bridge_status))

message = ("\n".join("{}\t{}".format(k, v) for k, v in bridge_info.items()))

# f = driver.find_element_by_xpath("(//*[@id='status'])[2]")

while True:
    print(message)
    time.sleep(10)
