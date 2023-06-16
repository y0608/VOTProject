from flask import Flask, render_template
from datetime import datetime
import pytz

app = Flask(__name__)

# Define the time zones
time_zones = {
    'New York': 'America/New_York',
    'London': 'Europe/London',
    'Tokyo': 'Asia/Tokyo',
    'Sydney': 'Australia/Sydney'
}

@app.route('/')
def home():
    # Get the current time for each time zone
    current_times = {}
    for city, tz in time_zones.items():
        current_times[city] = datetime.now(pytz.timezone(tz)).strftime('%Y-%m-%d %H:%M:%S')

    # Render the template with the current times
    return render_template('index.html', times=current_times)

if __name__ == '__main__':
    app.run(debug=True)
