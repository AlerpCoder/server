from flask import Flask, jsonify, abort, make_response, request
import sqlite3
from datetime import datetime, date, time

app = Flask(__name__)


@app.route('/contents', methods=['GET'])
def get_temperature():
    connect = sqlite3.connect("./tempData.db")
    temps = []
    for row in connect.execute("select * from temp"):
        temps.append({"date": row[0], "temperature": row[1], "humidity": row[2]})
    return jsonify(temps)


@app.route('/contents', methods=['POST'])
def create_temperature():
    currentDate = datetime.now().strftime('%d.%m.%Y, %H:%m:%s')
    temp = request.json['temperature']
    hum = request.json['humidity']
    connect = sqlite3.connect("./tempData.db")
    cursor = connect.cursor()
    cursor.execute("insert into temp values(?,?,?)", (currentDate, temp, hum))
    connect.commit()
    connect.close()
    return 'finished', 201


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': error}), 404)


@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': error}), 400)


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=False)
