from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains  # Add this line
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time

@pytest.fixture
def browser():
    driver = webdriver.Chrome()  
    yield driver
    driver.quit()

def scroll_up_slowly(browser):
    total_height = int(browser.execute_script("return document.body.scrollHeight"))
    scroll_height = 0

    while scroll_height < total_height:
        # Scroll up by 10 pixels 
        browser.execute_script(f"window.scrollTo(0, {scroll_height});")
        scroll_height += 10
        time.sleep(0.09)

def test_example(browser):
    browser.get("https://www.thesparksfoundationsingapore.org/")
    browser.maximize_window()
   #  #TestCase 1 - Verifying title of page
   #  print("TestCase 1: ")
   #  expected_title = "The Sparks Foundation | Home"
   #  if browser.title == expected_title:
   #     print(f"Page title is correct: {browser.title}")
   #  else:
   #     assert browser.title == expected_title, f"Expected title: {expected_title}, Actual title: {browser.title}"
   #  #end of TestCase 1
       
    #TestCase 2 - Navigating to About Us page and redirecting to Guiding Principle Page 
   #  print("TestCase 2: ")    
   #  about_link = WebDriverWait(browser, 10).until(
   #  EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-hover="About"]')))
   #  about_link.click()

   #  # Navigating to "Guiding Principles" link 
   #  guiding_principles_link = WebDriverWait(browser, 10).until(
   #  EC.element_to_be_clickable((By.CSS_SELECTOR, '[href="/about/guiding-principles/"]')))
   #  guiding_principles_link.click()

   #  time.sleep(5)
   #  #end of TestCase 2
    
   # #TestCase 3 - Scrolling entire Guiding Principle Page and navigates back to Home Page
   #  print("TestCase 3: ")    
   #  scroll_up_slowly(browser)
   #   #Navigate back to the home page
   #  browser.back()
   #  is_on_home_page = browser.find_elements(By.ID, 'home')

   #  if is_on_home_page:
   #    print("Successfully navigated to the home page.")
   #  else:
   #    print("Not on the home page.")
    #end of TestCase3

    #TestCase 4
    print("TestCase 4: ")    
    hover_element = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-hover="Policies and Code"]'))
    )
    hover_element.click()

   # Click on the desired link
    click_element = WebDriverWait(browser, 10).until(
      EC.element_to_be_clickable((By.CSS_SELECTOR, '[href="/policies-and-code/service-quality-values/"]'))
   )
    click_element.click()
    time.sleep(3)

     # Get the current URL
    current_url = browser.current_url
    print("Current URL:", current_url)

        # Check if the header with class "top-header-agile" exists
    header_exists = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'top-header-agile'))
        )

        # Check if the footer with class "footer-row w3layouts-agile" exists
    footer_exists = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'footer-row.w3layouts-agile'))
        )

        # Print the results
    if header_exists and footer_exists:
            print("Header and Footer exist on the current URL.")
    elif header_exists:
            print("Header exists but Footer is missing.")
    elif footer_exists:
            print("Footer exists but Header is missing.")
    else:
            print("Both Header and Footer are missing.")

   #end of TestCase 4
    browser.quit()
