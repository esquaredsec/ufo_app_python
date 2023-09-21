import sqlite3

# Function to create the database and table if they don't exist
def create_database():
    try:
        conn = sqlite3.connect('ufo.db')
        cursor = conn.cursor()

        # Create a table to store UFO sightings data
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS ufo_sightings (
                Date TEXT,
                Location TEXT,
                Description TEXT,
                LastScrapedDate TEXT
            )
        ''')

        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Error creating database: {str(e)}")

# Function to insert UFO sightings into the database
def insert_ufo_sighting(date, location, description, last_scraped_date):
    try:
        conn = sqlite3.connect('ufo.db')
        cursor = conn.cursor()

        # Insert a single UFO sighting into the database
        cursor.execute('''
            INSERT INTO ufo_sightings (Date, Location, Description, LastScrapedDate)
            VALUES (?, ?, ?, ?)
        ''', (date, location, description, last_scraped_date))

        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Error inserting UFO sighting: {str(e)}")

# Function to retrieve all UFO sightings from the database
def get_ufo_sightings():
    try:
        conn = sqlite3.connect('ufo.db')
        cursor = conn.cursor()

        # Retrieve all UFO sightings from the database
        cursor.execute('SELECT Date, Location, Description, LastScrapedDate FROM ufo_sightings')
        sightings = cursor.fetchall()

        conn.close()

        ufo_sightings = []
        for sighting in sightings:
            date, location, description, last_scraped_date = sighting
            ufo_sighting = {
                'Date': date,
                'Location': location,
                'Description': description,
                'LastScrapedDate': last_scraped_date
            }
            ufo_sightings.append(ufo_sighting)

        return ufo_sightings
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
        return []
    except Exception as e:
        print(f"Error retrieving UFO sightings: {str(e)}")
        return []
