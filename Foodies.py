import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np

# Set standard User-Agent
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}

# Create list of URLs (1 - 9)
pages = np.arange(1, 10, 1)
urls = []
for page in pages:
    url = 'https://www.statecollege.com/business-directory/category/restaurant/page/' + str(page)
    urls.append(url)

# Create variables needed for functions
num_list = []
add_list = []
name_list = []


# Get names of businesses
def get_name():
    for name in soup.select('h2 a'):
        # print(name.text.strip()) # Print to console
        name_list.append(name.text.strip())
    return name_list


# Get addresses of businesses
def get_address():
    for address in soup.select('div.address-info'):
        if 'Address' not in address:
            # print(address.text.strip().replace('Address:', '')) # Print to console
            # Removes 'Addresses' text from data
            add_list.append(address.text.strip().replace('Address:', ''))
    return add_list


# Get phone number of businesses
def get_number():
    for number in soup.select('.wpbdp-field a'):
        # Removes 'WEBSITE' text from data
        if 'WEBSITE' not in number:
            # print(number.text.strip()) # Print to console
            num_list.append(number.text.strip())
    return num_list


# Loop through urls and request HTML data
# Create Dataframe from Pandas in order to create the CSV file

for url in urls:
    result = requests.get(url, headers=headers)
    html = result.content
    soup = BeautifulSoup(html, 'html.parser')
    df = pd.DataFrame(list(zip(*[get_name(), get_address(), get_number()])))
    df.columns = ['Name of Business', 'Address', 'Phone Number']
df.to_csv('State_College_Businesses.csv', index=False)
# print(df) # Print to console
