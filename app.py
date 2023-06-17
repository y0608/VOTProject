from flask import Flask, render_template
from datetime import datetime
import pytz

app = Flask(__name__)

time_zones = {
    'New York': 'America/New_York',
    'London': 'Europe/London',
    'Tokyo': 'Asia/Tokyo',
    'Sydney': 'Australia/Sydney'
}

@app.route('/')
def home():
    current_times = {}
    for city, tz in time_zones.items():
        dateNow = datetime.now(pytz.timezone(tz))
        current_times[city] = [dateNow.strftime('%Y-%m-%d'),
                               dateNow.strftime('%H:%M:%S')] # easier to format later

    return render_template('index.html', times=current_times)

if __name__ == '__main__':
    app.run()
