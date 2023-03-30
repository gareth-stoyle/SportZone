from get_sports import get_fixtures
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome'

@app.route('/sports')
def sports():
    url = "https://www.tvsportguide.com"
    fixtures = get_fixtures(url)
    return render_template("sports.html", fixture_data=fixtures)


app.run(host='0.0.0.0', port=81)