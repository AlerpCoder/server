from flask import Flask, jsonify, render_template, make_response, request
import sqlite3
import time

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")


@app.route('/contents', methods=['GET'])
def get_temperature():
    connect = sqlite3.connect("./tempData.db")
    temps = []
    for row in connect.execute("SELECT * FROM temp"):
        temps.append({"date": row[0], "temperature": row[1], "humidity": row[2]})
    return jsonify(temps)


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
def not_found(error):
    return make_response(jsonify({'error': error}), 404)


@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': error}), 400)


if __name__ == '__main__':
    app.run(debug=False)
