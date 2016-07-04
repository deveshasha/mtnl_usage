from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:/Users/Rashmi/Desktop/chromedriver_win32/chromedriver.exe")
driver.get('http://crestelreg.mtnl.net.in:10080/jsp/Login.jsp')

try:
	userfield = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,'username')))
	userfield.click()
	userfield.send_keys('26365815@a')
	password = driver.find_element_by_name('password')
	password.click()
	password.send_keys('#password')
	login = driver.find_element_by_xpath('//input[@name="Submit2"]').click()
	
	usageinfo = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,'MenuLink3')))
	usageinfo.click()

	submitbtn = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/table[2]/tbody/tr[2]/td/table/tbody/tr[6]/td/input')))
	submitbtn.click()

	usage = driver.find_element_by_xpath('//*[@id="dataTable"]/tbody/tr[13]/td[4]/b')
	usage_text = usage.text
	
	driver.get('http://deveshasha.pythonanywhere.com/mtnl/'+ str(int(float(usage_text))))

except TimeoutException:
	print "The page took too long to load." 