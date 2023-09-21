import requests
from bs4 import BeautifulSoup
import sqlite3

# Function to scrape UFO sightings and update the last scraped date
def scrape_ufo_sightings(page_url, last_scraped_date):
    try:
        response = requests.get(page_url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        # Your scraping logic here
        ufo_sightings = []

        table = soup.find('table', {'class': 'maintext'})
        for row in table.find_all('tr')[1:]:  # Skip the header row
            columns = row.find_all('td')
            if len(columns) >= 8:  # Ensure there are at least 8 columns
                date = columns[7].get_text(strip=True)  # Date is in the 8th column
                location = ', '.join(columns[2:5])  # Join columns 2, 3, and 4 with commas
                description = columns[6].get_text(strip=True)  # Description is in the 7th column

                ufo_sighting = {
                    "Date": date,
                    "Location": location,
                    "Description": description,
                    "LastScrapedDate": last_scraped_date
                }

                ufo_sightings.append(ufo_sighting)

        return ufo_sightings
    except Exception as e:
        print(f"Failed to retrieve data from the page: {page_url}")
        print(f"Error: {str(e)}")
        return []

# Function to extract links from the main UFO sightings page
def extract_links(main_url):
    try:
        response = requests.get(main_url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract links from the page
        links = []
        table = soup.find('table', {'class': 'maintext'})
        for row in table.find_all('tr')[1:]:  # Skip the header row
            columns = row.find_all('td')
            if len(columns) >= 8:
                link = columns[0].find('a')['href']
                links.append(link)

        return links
    except Exception as e:
        print(f"Failed to extract links from the page: {main_url}")
        print(f"Error: {str(e)}")
        return []

# Function to update the last scraped date in the database
def update_last_scraped_date(last_scraped_date):
    try:
        conn = sqlite3.connect('ufo.db')
        cursor = conn.cursor()

        # Update the last scraped date in the database
        cursor.execute("UPDATE last_scraped SET date = ?", (last_scraped_date,))
        conn.commit()

        conn.close()
    except Exception as e:
        print(f"Failed to update last scraped date in the database.")
        print(f"Error: {str(e)}")
