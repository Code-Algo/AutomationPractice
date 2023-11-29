from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Replace with the path to your file containing the URLs
urls_file_path = 'urls.txt'

# Replace with the old and new company names
old_company_name = 'OldCompany'
new_company_name = 'NewCompany'

# Create a new instance of the Chrome driver (replace with the appropriate driver for your browser)
driver = webdriver.Chrome()

# Read the list of URLs from the file
with open(urls_file_path, 'r') as file:
    form_urls = [line.strip() for line in file]

for url in form_urls:
    driver.get(url)

    # Find and replace the old company name with the new one
    old_company_name_element = driver.find_element(By.XPATH, "//*[contains(text(), 'Community Realty Management')]")
    old_company_name_element.clear()
    old_company_name_element.send_keys('enos')

    # Submit the form (this may vary depending on the form structure)
    save_button = driver.find_element(By.XPATH, "//button[@type='save']")
    save_button.click()

    # Wait for the form to be processed and removed from the list
    time.sleep(5)  # Adjust the wait time based on the actual behavior of the webpage

    # Refresh the list of forms
    driver.refresh()

    # Print the result (you might want to add error handling here)
    print(f"Updated {url}.")

# Close the browser window
driver.quit()