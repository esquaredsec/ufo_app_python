from flask import Flask, jsonify

app = Flask(__name__)

# Dummy UFO sightings data
ufo_sightings = [
    {
        'id': 1,
        'location': 'Los Angeles, CA',
        'date': '2023-07-15',
        'details': 'Saw a bright light in the sky.'
    },
    {
        'id': 2,
        'location': 'New York, NY',
        'date': '2023-07-20',
        'details': 'Multiple lights moving in formation.'
    }
]

# Endpoint to retrieve all UFO sightings
@app.route('/api/sightings', methods=['GET'])
def get_sightings():
    return jsonify(ufo_sightings)

if __name__ == '__main__':
    app.run(debug=True)
