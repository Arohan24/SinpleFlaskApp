from flask import Flask, jsonify
import json
import os


app = Flask(__name__)
filename = 'data.txt'
default_data = [
    {"id": 1, "name": "apple", "color": "red"},
    {"id": 2, "name": "banana", "color": "yellow"},
    {"id": 3, "name": "cherry", "color": "red"},
    {"id": 4, "name": "mango", "color": "orange"},
    {"id": 5, "name": "grape", "color": "purple"}
]


@app.route('/api')
def get_data():
    if not os.path.exists(filename):
        with open(filename, 'w') as file:
            json.dump(default_data, file, indent=2)


    with open(filename, 'r') as file:
        data = json.load(file)


    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
