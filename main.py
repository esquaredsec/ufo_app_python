import requests
from bs4 import BeautifulSoup
import json

# Define the URL
url = "https://nuforc.org/webreports/ndxevent.html"

# Send an HTTP GET request
response = requests.get(url)

# Initialize a list to store the hyperlinks
hyperlinks = []

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the table containing the hyperlinks
    table = soup.find("table", {"cellspacing": "1"})

    # Loop through the rows in the table (skip the first row)
    for row in table.find_all("tr")[1:7]:  # Select the first 6 rows
        # Find the hyperlink in the first cell of the row
        hyperlink = row.find("a")

        # Check if a hyperlink was found
        if hyperlink:
            # Extract the href attribute (URL)
            href = hyperlink.get("href")

            # Append the URL to the list
            hyperlinks.append(href)

# Check if there are any hyperlinks
if hyperlinks:
    # Take the first hyperlink (change this index if needed)
    first_hyperlink = hyperlinks[0]

    # Construct the full URL of the first hyperlink
    first_hyperlink_url = f"https://nuforc.org/webreports/{first_hyperlink}"

    # Send an HTTP GET request to the first hyperlink
    response = requests.get(first_hyperlink_url)

    # Initialize a list to store the table data
    table_data = []

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the first hyperlink page
        soup = BeautifulSoup(response.text, "html.parser")

        # Find the table containing the data
        data_table = soup.find("table", {"cellspacing": "1"})

        # Loop through the rows in the table (skip the first row)
        for row in data_table.find_all("tr")[1:6]:  # Select the first 5 rows
            # Find the cells in the row
            cells = row.find_all("td")

            # Extract the data from the cells
            date_time = cells[0].get_text()
            city = cells[1].get_text()
            state = cells[2].get_text()
            country = cells[3].get_text()
            shape = cells[4].get_text()

            # Append the data to the table_data list
            table_data.append({
                "Date/Time": date_time,
                "City": city,
                "State": state,
                "Country": country,
                "Shape": shape
            })

    # Convert the table data to JSON
    table_data_json = json.dumps(table_data)

    # Print the JSON data
    print(table_data_json)
else:
    print("No hyperlinks found.")
