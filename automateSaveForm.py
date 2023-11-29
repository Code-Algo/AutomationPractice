import requests
from bs4 import BeautifulSoup

# Replace these with your actual URLs
form_urls = [
    'http://localhost:5173/contact',
    'https://example.com/form2',
    # Add all the form URLs
]

# # Read the list of URLs from the file
# with open(urls_file_path, 'r') as file:
#     form_urls = [line.strip() for line in file]

# Replace with the old and new company names
old_company_name = 'OldCompany'
new_company_name = 'NewCompany'

for url in form_urls:
    # Fetch the HTML content of the form
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find and replace the old company name with the new one
    for element in soup.find_all(text=lambda text: text and old_company_name in text):
        element.replace_with(element.replace(old_company_name, new_company_name))

    # Update the form on the server
    updated_content = str(soup)
    response = requests.post(url, data={'form_data': updated_content})

    # Print the result (you might want to add error handling here)
    print(f"Updated {url}. Status code: {response.status_code}")