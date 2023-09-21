from scrape_ufo_sightings import scrape_ufo_sightings
from database_operations import create_database, insert_ufo_sightings

# URL to scrape
main_url = 'https://nuforc.org/ndx/?id=event'

# Scrape UFO sightings
ufo_sightings = []
links = [...]  # Extract links as needed
for link in links:
    sub_url = f'https://nuforc.org/{link}'
    ufo_sightings.extend(scrape_ufo_sightings(sub_url))

# Create the database if it doesn't exist
create_database()

# Insert UFO sightings into the database
insert_ufo_sightings(ufo_sightings)
