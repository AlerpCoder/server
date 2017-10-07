import json
import logging
import sqlite3
import time
from functools import reduce

from flask import Flask, jsonify, render_template, make_response, request

app = Flask(__name__)


def get_json():
    connect = sqlite3.connect("./tempData.db")
    temps = []
    for row in connect.execute("SELECT * FROM temp"):
        temps.append({"date": row[0], "temperature": row[1], "humidity": row[2]})
    return temps


@app.route('/', methods=['GET'])
def index():
    labels = map(lambda x: x['date'], get_json())
    data_temp = map(lambda x: x['temperature'], get_json())
    data_hum = map(lambda x: x['humidity'], get_json())
    return render_template("index.html", labels=map(json.dumps, labels), temp_data=map(json.dumps, data_temp),
                           hum_data=map(json.dumps, data_hum))


@app.route('/contents', methods=['GET'])
def get_temperature():
    return jsonify(get_json())


@app.route('/contents', methods=['POST'])
def create_temperature():
    currentDate = time.strftime('%d.%m.%Y, %H:%m:%s')
    temp = request.json['temperature']
    hum = request.json['humidity']
    connect = sqlite3.connect("./tempData.db")
    cursor = connect.cursor()
    cursor.execute("INSERT INTO temp VALUES(?,?,?)", (currentDate, temp, hum))
    connect.commit()
    connect.close()
    return 'finished', 201


@app.errorhandler(404)
def not_found(exception):
    app.logger.error(exception)
    return make_response(jsonify({'error': request.full_path}), 404)


if __name__ == '__main__':
    logging.basicConfig(filename='server/debug.log', level=logging.DEBUG)
    app.run(host="0.0.0.0", debug=False)
