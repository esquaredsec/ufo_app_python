import requests
from bs4 import BeautifulSoup
import json

# Function to extract UFO sightings from a page
def extract_ufo_sightings(page_url):
    ufo_sightings = []

    page_response = requests.get(page_url)
    page_soup = BeautifulSoup(page_response.text, 'html.parser')

    # Find the table containing UFO sightings
    table = page_soup.find('table')

    # Loop through each row in the table
    for row in table.find_all('tr')[1:]:  # Skip the header row
        columns = row.find_all('td')

        # Ensure that there are at least 8 columns in the row before extracting data
        if len(columns) >= 8:
            date = columns[7].text.strip()
            # Join columns 2, 3, and 4 and separate them with commas
            location_parts = [columns[2].text.strip(), columns[3].text.strip(), columns[4].text.strip()]
            location = ', '.join(location_parts)
            description = columns[6].text.strip()

            # Create a dictionary for each UFO sighting
            ufo_sighting = {
                'Date': date,
                'Location': location,
                'Description': description
            }

            # Append the dictionary to the list
            ufo_sightings.append(ufo_sighting)

    # Check if there's a "Next" page link and extract its URL
    next_page_link = page_soup.find('a', string='Next')
    if next_page_link:
        next_page_url = f'https://nuforc.org/{next_page_link["href"]}'
        # Recursively call the function to fetch data from the next page
        ufo_sightings.extend(extract_ufo_sightings(next_page_url))

    return ufo_sightings

# Make a request to the main page
main_url = 'https://nuforc.org/ndx/?id=event'
main_response = requests.get(main_url)

# Parse the HTML content of the main page
main_soup = BeautifulSoup(main_response.text, 'html.parser')

# Find the table containing UFO sighting links
table = main_soup.find('table')

# Extract all links from the table
links = [link['href'] for link in table.find_all('a')]

# Initialize an empty list to store all UFO sightings data
all_ufo_sightings = []

# Loop through each link and fetch data
for link in links:
    # Create the full URL for the subpage
    sub_url = f'https://nuforc.org/{link}'
    
    # Extract UFO sightings from the subpage, including multiple pages if necessary
    ufo_sightings = extract_ufo_sightings(sub_url)

    # Append the UFO sightings data for this link to the master list
    all_ufo_sightings.extend(ufo_sightings)

# Check if there are any UFO sightings data
if all_ufo_sightings:
    # Convert the list of dictionaries to JSON format
    ufo_json = json.dumps(all_ufo_sightings, indent=4)

    # Print or return the JSON data
    print(ufo_json)
else:
    print("No UFO sightings data found on the webpage.")
