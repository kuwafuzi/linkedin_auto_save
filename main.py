from selenium import webdriver
from selenium.webdriver.chrome import service as fs
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time

# Get the URL
chrome_driver_path = "*********************"
chrome_service = fs.Service(executable_path=chrome_driver_path)
# driver = webdriver.Chrome(service=chrome_service)
driver = uc.Chrome(use_subprocess=True)
driver.maximize_window()

driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

# get the Session id of the parent.
parentGUID = driver.current_window_handle

# into sign in page
sign_in_button = driver.find_element(By.CLASS_NAME, "nav__button-secondary")
sign_in_button.click()
time.sleep(20)        # wait until appear the google account menu.
sign_in_google = driver.find_element(By.ID, "sign-in-with-google-button")
sign_in_google.click()

# get the All the session id of the browsers
handle_array = driver.window_handles
# print(handle_array[0])
# print(handle_array[1])
driver.switch_to.window(handle_array[1])


# switch the frame. You can access popup google account.
input_mail = driver.find_element(By.ID, "identifierId")
input_mail.send_keys("kuwafuzi110315@gmail.com")
# next_button = driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button')
next_button_first = driver.find_element(By.ID, "identifierNext")
next_button_first.click()
time.sleep(5)
input_password = driver.find_element(By.NAME, "password")
input_password.send_keys("iZufawuk2580")
next_button_second = driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button')
next_button_second.click()
time.sleep(5)

# switch back to the parent window
driver.switch_to.window(parentGUID)
time.sleep(15)


# Scrolls down job list pane to load all listings and then returns to the top
job_list_scroll = driver.find_element(By.CLASS_NAME, "jobs-search__left-rail")
job_list_scroll.click()
html = driver.find_element(By.TAG_NAME, "html")
html.send_keys(Keys.END)
time.sleep(3)
html.send_keys(Keys.HOME)

# Gets all jobs on first page as clickable elements, clicks job, saves job, and repeats
job_list = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")

for job in job_list:
    print("called")
    job.click()
    time.sleep(10)
    try:
        save_button = driver.find_element(By.CLASS_NAME, "jobs-save-button")
        save_button.click()
        time.sleep(10)

    except NoSuchElementException:
        print("No application button, skipped.")
        continue

driver.quit()
