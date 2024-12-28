from flask import Flask, render_template, jsonify
from api_methods import get_all_airports

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('map.html')

@app.route('/airports')
def airports():
    airports = get_all_airports()
    return jsonify(airports)

if __name__ == '__main__':
    app.run(debug=True)
