from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging

logging.basicConfig(
    filename="form_test.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

try:
    with webdriver.Chrome() as driver:
        driver.maximize_window()
        logging.info("Browser launched successfully")

        driver.get("https://demoqa.com/automation-practice-form?utm_source=chatgpt.com")
        print("Browser URL:", driver.current_url)
        print("Browser Title:", driver.title)

        wait = WebDriverWait(driver, 10)

        fn = wait.until(EC.visibility_of_element_located((By.ID, "firstName")))

        logging.info("Page has been loaded successfully")

        fn.send_keys("BVNS")
        logging.info("Entered first name")
        time.sleep(1)


        ln = wait.until(EC.visibility_of_element_located((By.ID, "lastName")))
        ln.send_keys("Kuravi")
        logging.info("Entered last name")
        time.sleep(1)    

        email = wait.until(EC.visibility_of_element_located((By.ID, "userEmail")))
        email.send_keys("bvns@gmail.com")
        logging.info("Entered email")
        time.sleep(1)

        gender = wait.until(EC.element_to_be_clickable((By.ID, "gender-radio-2")))
        gender.click()
        logging.info("Selected gender")
        time.sleep(1)

        phone = wait.until(EC.visibility_of_element_located((By.ID, "userNumber")))
        phone.send_keys("898546789")
        logging.info("Entered phone number")
        time.sleep(1)


        submit_btn = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#submit")))
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        submit_btn.click()
        logging.info("Submitted form")
        time.sleep(1)

        success_title = wait.until(EC.visibility_of_element_located((By.ID, "example-modal-sizes-title-lg")))

        actual_title = success_title.text

        assert actual_title == "Thanks for submitting the form", f"Expected msg not found. Got {actual_title}"

        close = wait.until(EC.element_to_be_clickable((By.ID, "closeLargeModal")))
        close.click()

except Exception as e:
    logging.error("Test failed %s", e)