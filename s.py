import time
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.bezorgdekrant.nl/en/all-jobs"

# Use Chrome driver (download and provide the path if not in PATH)
driver = webdriver.Chrome()

driver.get(url)

# Wait for some time to let the dynamic content load
time.sleep(10)

# Scroll down to load more content
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Wait for some additional time after scrolling
time.sleep(5)

soup = BeautifulSoup(driver.page_source, 'html.parser')

# Find all span elements with the class 'job-city' and get the text content
city_elements = soup.select('span.job-city')
cities = [city.get_text(strip=True) for city in city_elements]

driver.quit()

if cities:
    # Creating a DataFrame
    cities_df = pd.DataFrame(cities, columns=['Cities'])

    # Save to CSV file
    cities_df.to_csv('cities_data.csv', header=True, index=False)

    print(f"City information saved to 'cities_data.csv'. Found {len(cities)} cities.")
else:
    print("No city information found on the webpage.")
