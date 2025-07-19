import time
import random
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc

logging.basicConfig(level=logging.INFO)

def get_chrome_driver():
    options = uc.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/129 Safari/537.36")
    options.add_argument("--lang=en-US")

    return uc.Chrome(options=options)  

def simulate_human_behavior(driver):
    try:
        actions = ActionChains(driver)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight * arguments[0]);", random.uniform(0.3, 0.7))
        time.sleep(random.uniform(1.5, 3.5))
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(random.uniform(0.7, 2.2))
        actions.move_by_offset(random.randint(100, 300), random.randint(100, 300)).perform()
    except Exception as e:
        logging.warning(f"Error in human simulation: {str(e)}")

def hide_webdriver(driver):
    try:
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', { get: () => undefined });")
    except Exception as e:
        logging.warning(f"Error hiding WebDriver: {str(e)}")

def scrape_jobs():
    driver = get_chrome_driver()
    
    url = "https://www.upwork.com/freelance-jobs/sql/" 
    driver.get(url)

    hide_webdriver(driver)
    simulate_human_behavior(driver)

    wait = WebDriverWait(driver, 60)
    wait.until(EC.presence_of_all_elements_located((By.XPATH, '//section[contains(@class, "up-card-section") and contains(@class, "up-card-list-section")] | //div[contains(@class, "job-tile")] | //div[@data-test="job-tile"]')))
    job_tiles = driver.find_elements(By.XPATH, '//section[contains(@class, "up-card-section") and contains(@class, "up-card-list-section")] | //div[contains(@class, "job-tile")] | //div[@data-test="job-tile"]')

    jobs = []
    for job in job_tiles:
        try:
            title_elem = job.find_elements(By.XPATH, './/h4[@class="my-0"]/a | .//a[contains(@class, "job-title")] | .//a[@data-test="job-title-title"]')
            title = title_elem[0].text if title_elem else "Not found"
            url_link = title_elem[0].get_attribute("href") if title_elem else "Not found"

            company_elem = job.find_elements(By.XPATH, './/span[@data-test="company-name"]')
            location_elem = job.find_elements(By.XPATH, './/span[@data-test="location"]')
            posted_elem = job.find_elements(By.XPATH, './/span[@data-test="posted-date"]')

            company = company_elem[0].text if company_elem else "Not found"
            location = location_elem[0].text if location_elem else "Not found"
            posted_date = posted_elem[0].text if posted_elem else "Not found"

            jobs.append({
                "title": title,
                "company": company,
                "location": location,
                "url_link": url_link,
                "posted_date": posted_date
            })
        except Exception as e:
            logging.warning(f"Error parsing a job: {e}")
            continue

    driver.quit()
    return jobs
