import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
import mysql.connector
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
options.add_argument("--start-maximized")
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
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight * arguments[0]);", random.uniform(0.3, 0.7))
        time.sleep(random.uniform(1.5, 3.5))
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(random.uniform(0.7, 2.2))
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

def is_job_exists(job_link):
    """Check if job link already exists in the database."""
    try:
        conn = mysql.connector.connect(
           host="127.0.0.1",
            user="sherry",  
            password="mysql123",  
            database="uamsdb"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM job WHERE job_link = %s", (job_link,))
        count = cursor.fetchone()[0]
        return count > 0
    except Exception as e:
        logging.error(f"Error checking job existence: {str(e)}")
        return False
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def save_to_database(job_data):
    """Save job data to the MySQL database."""
    try:
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="sherry",  
            password="mysql123",  
            database="uamsdb"
        )
        cursor = conn.cursor()
        sql = """
            INSERT INTO job (title, description, category, skills_required, duration_days, posted_date, deadline, rating, 
                             payment_type, payment_amount, min_payment, max_payment, experience_level, job_link, country)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
            title=VALUES(title), description=VALUES(description), category=VALUES(category),
            skills_required=VALUES(skills_required), duration_days=VALUES(duration_days),
            posted_date=VALUES(posted_date), deadline=VALUES(deadline), rating=VALUES(rating),
            payment_type=VALUES(payment_type), payment_amount=VALUES(payment_amount),
            min_payment=VALUES(min_payment), max_payment=VALUES(max_payment),
            experience_level=VALUES(experience_level), job_link=VALUES(job_link), country=VALUES(country)
        """
        cursor.execute(sql, (
            job_data['title'], job_data['description'], job_data['category'], job_data['skills_required'],
            job_data['duration_days'], job_data['posted_date'], job_data['deadline'], job_data['rating'],
            job_data['payment_type'], job_data['payment_amount'], job_data['min_payment'], job_data['max_payment'],
            job_data['experience_level'], job_data['job_link'], job_data['country']
        ))
        conn.commit()
        logging.info(f"Saved job to database: {job_data['title']}")
    except mysql.connector.IntegrityError as e:
        logging.info(f"Duplicate job skipped: {job_data['title']} (job_link: {job_data['job_link']})")
    except Exception as e:
        logging.error(f"Error saving to database: {str(e)}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

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
        url = "https://www.upwork.com/freelance-jobs/sql/"
        driver.get(url)
        time.sleep(15)  # Inspect page manually
        logging.info("Navigated to Upwork Python jobs page")

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

                    # Skip if title is "Not found"
                    if title == "Not found":
                        logging.info("Skipped job due to 'Not found' title")
                        continue

                    description_elem = job.find_elements(By.XPATH, './/span[@data-test="job-description-text"] | .//div[contains(@class, "description")] | .//p[contains(@class, "job-description")] | .//div[@data-test="job-description"]')
                    description = description_elem[0].text.strip() if description_elem else "Not found"

                    category_elem = job.find_elements(By.XPATH, './/span[contains(@class, "category")] | .//div[@data-test="job-category"]')
                    category = category_elem[0].text.strip() if category_elem else "Not found"

                    skills_elem = job.find_elements(By.XPATH, './/div[@data-test="skills"]//a | .//div[contains(@class, "skills")]//span | .//span[@data-test="skill"]')
                    skills_required = ", ".join([skill.text.strip() for skill in skills_elem]) if skills_elem else "None"

                    duration_elem = job.find_elements(By.XPATH, './/span[contains(@class, "duration")] | .//div[@data-test="job-duration"]')
                    duration_days = duration_elem[0].text.strip().split()[0] if duration_elem else 0

                    posted_date_elem = job.find_elements(By.XPATH, './/span[contains(@class, "posted")] | .//div[@data-test="posted-date"]')
                    posted_date = posted_date_elem[0].text.strip() if posted_date_elem else datetime.now().strftime('%Y-%m-%d')

                    deadline_elem = job.find_elements(By.XPATH, './/span[contains(@class, "deadline")] | .//div[@data-test="deadline"]')
                    deadline = deadline_elem[0].text.strip() if deadline_elem else None

                    rating_elem = job.find_elements(By.XPATH, './/span[contains(@class, "rating")] | .//div[@data-test="job-rating"]')
                    rating = float(rating_elem[0].text.strip().split()[0]) if rating_elem and rating_elem[0].text.strip() else 0.0

                    pay_elem = job.find_elements(By.XPATH, './/span[@data-test="job-type"] | .//div[contains(@class, "job-type")]//span | .//span[contains(@class, "budget")]')
                    pay_text = pay_elem[0].text.strip() if pay_elem else "Not specified"
                    payment_type = "Hourly" if "hr" in pay_text.lower() else "Fixed" if "fixed" in pay_text.lower() else "Not specified"
                    payment_amount = float(pay_text.split()[0].replace('$', '').replace(',', '')) if '$' in pay_text and pay_text.split()[0].replace('$', '').replace(',', '').replace('.', '').isdigit() else 0.0

                    min_payment = payment_amount if payment_type == "Hourly" else 0.0
                    max_payment = payment_amount if payment_type == "Fixed" else 0.0

                    experience_level_elem = job.find_elements(By.XPATH, './/span[contains(@class, "experience")] | .//div[@data-test="experience-level"]')
                    experience_level = int(experience_level_elem[0].text.strip().split()[0]) if experience_level_elem else 0

                    job_url_elem = job.find_elements(By.XPATH, './/h4[@class="my-0"]/a | .//a[contains(@class, "job-title")] | .//a[@data-test="job-title"]')
                    job_link = job_url_elem[0].get_attribute('href') if job_url_elem else "Not found"

                    country_elem = job.find_elements(By.XPATH, './/span[contains(@class, "country")] | .//div[@data-test="job-country"]')
                    country = country_elem[0].text.strip() if country_elem else "Not found"

                    job_data = {
                        'title': title,
                        'description': description,
                        'category': category,
                        'skills_required': skills_required,
                        'duration_days': duration_days,
                        'posted_date': posted_date,
                        'deadline': deadline,
                        'rating': rating,
                        'payment_type': payment_type,
                        'payment_amount': payment_amount,
                        'min_payment': min_payment,
                        'max_payment': max_payment,
                        'experience_level': experience_level,
                        'job_link': job_link,
                        'country': country
                    }

                    # Check if job already exists before saving
                    if job_link != "Not found" and not is_job_exists(job_link):
                        all_jobs.append(job_data)
                        save_to_database(job_data)
                        logging.info(f"Scraped and saved job: {title}")
                    else:
                        logging.info(f"Skipped duplicate job: {title} (job_link: {job_link})")

                except Exception as e:
                    logging.error(f"Error scraping job: {str(e)}")
                    continue

            # Check for next page
            try:
                next_button = driver.find_element(By.XPATH, '//li[contains(@class, "next")]/a | //a[contains(@aria-label, "Next")] | //button[contains(@class, "next")]')
                if 'disabled' in next_button.get_attribute('class') or not next_button.is_enabled():
                    logging.info("No more pages to scrape")
                    break
                driver.execute_script("arguments[0].click();", next_button)
                logging.info("Navigated to next page")
                time.sleep(random.uniform(6, 12))
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

if __name__ == "__main__":
    logging.info("Starting Upwork job scraper")
    jobs = scrape_jobs()
    if jobs:
        print(f"Scraped and saved {len(jobs)} jobs to database")
    else:
        print("No jobs scraped. Check the log file for details.")
    logging.info("Scraping completed")