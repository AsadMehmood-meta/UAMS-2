import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
import csv
import logging
from datetime import datetime

# Setup logging
logging.basicConfig(
    filename=f'upwork_scraper_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Setup Chrome options for human-like behavior
options = uc.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--start-maximized")  # Maximize window as requested
options.add_argument("--disable-infobars")
options.add_argument("--disable-notifications")
options.add_argument("--disable-popup-blocking")
options.add_argument("--ignore-certificate-errors")
options.add_argument(f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36")
options.add_argument("--lang=en-US")
options.add_argument("--accept-lang=en-US,en;q=0.9")

def simulate_human_behavior(driver):
    """Simulate human-like interactions: scrolling and mouse movements."""
    try:
        actions = ActionChains(driver)
        # Random scrolling
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight * arguments[0]);", random.uniform(0.3, 0.7))
        time.sleep(random.uniform(1.5, 3.5))
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(random.uniform(0.7, 2.2))
        # Random mouse movement
        actions.move_by_offset(random.randint(100, 300), random.randint(100, 300)).perform()
        time.sleep(random.uniform(0.8, 2))
        logging.info("Simulated human-like scrolling and mouse movement")
    except Exception as e:
        logging.warning(f"Error in human simulation: {str(e)}")

def hide_webdriver(driver):
    """Inject JavaScript to hide WebDriver detection."""
    try:
        driver.execute_script("""
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            });
        """)
        logging.info("Injected JavaScript to hide WebDriver")
    except Exception as e:
        logging.warning(f"Error hiding WebDriver: {str(e)}")

def scrape_jobs():
    driver = None
    all_jobs = []

    try:
        # Initialize driver
        driver = uc.Chrome(options=options, version_main=138)
        logging.info("Chrome driver initialized")
        
        # Hide WebDriver property
        hide_webdriver(driver)
        
        url = "https://www.upwork.com/freelance-jobs/python-script/"
        driver.get(url)
        time.sleep(15)  # Inspect page manually
        logging.info("Navigated to Upwork Python jobs page")

        # Save screenshot for debugging
        driver.save_screenshot("initial_page.png")
        logging.info("Screenshot saved as initial_page.png")

        # Simulate human behavior
        simulate_human_behavior(driver)

        # Wait for job tiles with retry logic
        max_retries = 3
        for attempt in range(max_retries):
            try:
                WebDriverWait(driver, 90).until(
                    EC.presence_of_all_elements_located((
                        By.XPATH,
                        '//section[contains(@class, "up-card-section") and contains(@class, "up-card-list-section")] | //div[contains(@class, "job-tile")] | //div[@data-test="job-tile"]'
                    ))
                )
                logging.info("Job tiles loaded successfully")
                break
            except Exception as e:
                logging.warning(f"Attempt {attempt + 1} failed to load job tiles: {str(e)}")
                driver.save_screenshot(f"error_attempt_{attempt + 1}.png")
                logging.info(f"Screenshot saved as error_attempt_{attempt + 1}.png")
                if attempt == max_retries - 1:
                    logging.error("Failed to load job tiles after all retries")
                    return all_jobs
                time.sleep(random.uniform(8, 15))

        while True:
            # Simulate human behavior on each page
            simulate_human_behavior(driver)

            # Find all job tiles
            job_tiles = driver.find_elements(
                By.XPATH,
                '//section[contains(@class, "up-card-section") and contains(@class, "up-card-list-section")] | //div[contains(@class, "job-tile")] | //div[@data-test="job-tile"]'
            )
            logging.info(f"Found {len(job_tiles)} job tiles on current page")

            for job in job_tiles:
                try:
                    # Extract job details with fallback
                    title_elem = job.find_elements(By.XPATH, './/h4[@class="my-0"]/a | .//a[contains(@class, "job-title")] | .//a[@data-test="job-title"]')
                    title = title_elem[0].text.strip() if title_elem else "Not found"

                    summary_elem = job.find_elements(By.XPATH, './/span[@data-test="job-description-text"] | .//div[contains(@class, "description")]')
                    summary = summary_elem[0].text.strip() if summary_elem else "Not found"

                    pay_elem = job.find_elements(By.XPATH, './/span[@data-test="job-type"] | .//div[contains(@class, "job-type")]//span | .//span[contains(@class, "budget")]')
                    pay = pay_elem[0].text.strip() if pay_elem else "Not specified"

                    skills_elem = job.find_elements(By.XPATH, './/div[@data-test="skills"]//a | .//div[contains(@class, "skills")]//span | .//span[@data-test="skill"]')
                    skills = ", ".join([skill.text.strip() for skill in skills_elem]) if skills_elem else "None"

                    job_url_elem = job.find_elements(By.XPATH, './/h4[@class="my-0"]/a | .//a[contains(@class, "job-title")] | .//a[@data-test="job-title"]')
                    job_url = job_url_elem[0].get_attribute('href') if job_url_elem else "Not found"

                    job_data = {
                        'title': title,
                        'summary': summary,
                        'pay': pay,
                        'skills': skills,
                        'url': job_url,
                        'scraped_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    }
                    all_jobs.append(job_data)
                    logging.info(f"Scraped job: {title}")

                except Exception as e:
                    logging.error(f"Error scraping job: {str(e)}")
                    continue

            # Save partial results
            if all_jobs:
                save_to_csv(all_jobs)

            # Check for next page
            try:
                next_button = driver.find_element(By.XPATH, '//li[contains(@class, "next")]/a | //a[contains(@aria-label, "Next")] | //button[contains(@class, "next")]')
                if 'disabled' in next_button.get_attribute('class') or not next_button.is_enabled():
                    logging.info("No more pages to scrape")
                    break
                driver.execute_script("arguments[0].click();", next_button)
                logging.info("Navigated to next page")
                time.sleep(random.uniform(6, 12))  # Longer random delay
                WebDriverWait(driver, 90).until(
                    EC.presence_of_all_elements_located((
                        By.XPATH,
                        '//section[contains(@class, "up-card-section") and contains(@class, "up-card-list-section")] | //div[contains(@class, "job-tile")] | //div[@data-test="job-tile"]'
                    ))
                )
            except Exception as e:
                logging.info(f"No next page or error navigating: {str(e)}")
                break

    except Exception as e:
        logging.error(f"Critical error during scraping: {str(e)}")
        if driver:
            driver.save_screenshot("critical_error.png")
            logging.info("Screenshot saved as critical_error.png")

    finally:
        if driver:
            try:
                driver.quit()
                logging.info("Browser closed successfully")
            except Exception as e:
                logging.error(f"Error closing browser: {str(e)}")
        else:
            logging.warning("Driver was not initialized")

    return all_jobs

def save_to_csv(jobs):
    filename = f'upwork_jobs_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['title', 'summary', 'pay', 'skills', 'url', 'scraped_at'])
        writer.writeheader()
        for job in jobs:
            writer.writerow(job)
    logging.info(f"Saved {len(jobs)} jobs to {filename}")

if __name__ == "__main__":
    logging.info("Starting Upwork job scraper")
    jobs = scrape_jobs()
    if jobs:
        print(f"Scraped {len(jobs)} jobs and saved to CSV")
    else:
        print("No jobs scraped. Check the log file and screenshots for details.")
    logging.info("Scraping completed")