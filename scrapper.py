from selenium import webdriver
import pandas as pd 
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
driver = webdriver.Chrome("C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe")
driver.maximize_window()

data = pd.DataFrame(columns=["Title","Location","Company","Salary","Date","Description"])

for page in range(0,10,10):
    driver.get('https://www.indeed.ca/jobs?q=developer&start='+str(page))
    
    for job in driver.find_elements_by_class_name('result'):
        soup = BeautifulSoup(job.get_attribute('innerHTML'),'html.parser')
        
        title = soup.findAll("a",{"class": "jobtitle turnstileLink"})
        if len(title) != 0:
          title = title[0].text.replace("\n","").strip()
        else:
          title = "NaN" 
          
        location = soup.find(class_="location")
        if location != NULL:
          location = location.text.replace("\n","").strip()
        else:
          location = "NaN" 
          
        company = soup.find(class_="company")
        if company != NULL:
          company = company.text.replace("\n","").strip()
        else:
          company = "NaN" 
          
        salary = soup.find(class_="salary")
        if salary != NULL:
          salary = salary.text.replace("\n","").strip()
        else:
          salary = "NaN" 
        
        date = soup.find("span",class_="date")
        if date != NULL:
          date = date.text.replace("\n","").strip()
        else:
          date = "NaN" 
        
        		
        summary = job.find_element_by_xpath('./div[3]')
        try:
            summary.click()
        except:
            close_button = driver.find_elements_by_class_name('popover-x-button-close')[0]
            close_button.click()
            summary.click()
            
        
        job_desc = driver.find_element_by_id('vjs-desc')
        job1=job_desc.text.replace("\n","")
        print(job1)
       
    
        data = data.append({'Title':title,'Location':location,"Company":company,"Salary":salary,"Date":date,"Description":job1},ignore_index=True)
        
        
        

data.to_csv("indeed.csv",index=False)	