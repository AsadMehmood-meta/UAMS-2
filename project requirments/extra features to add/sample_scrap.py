import undetected_chromedriver as uc

from selenium.webdriver.support.ui import WebDriverWait     #used for random delay
from selenium.webdriver.support import expected_conditions as EC       #wait untill certain things comeup
from selenium.webdriver.common.by import By     #readymade object with which you can go to specific portion of web/html
from selenium.webdriver.common.keys import Keys     #used for special keys like ctrl+altr+r
from selenium.webdriver.common.action_chains import ActionChains      #set sequence of operation or chains of actions

#setup chrome driver
options = uc.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--start-maximized") 

driver = uc.Chrome(option=options , version_main=138)    #version must match yout chrome (chrome://version)

# driver.get("https://www.investing.com/")    #version must match yout chrome (chrome://version)

driver.get("https://www.upwork.com/freelance-jobs/data-analysis/")

try:
    WebDriverWait(driver , 60).until(
    # EC.presence_of_element_located((By.ID , "login"))
    # EC.presence_of_element_located((By.CLASS_NAME , "nav-bar"))
    EC.presence_of_element_located((By.XPATH , '//body//section/div[@class="job-tile-content"]'))       #to define indirect path to reach exact class/id 
    )
    print("Page loaded")

finally:
    driver.quit()






