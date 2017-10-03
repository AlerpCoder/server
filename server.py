from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)

@app.route('/contents', methods=['GET'])
def get_temperature():
    return jsonify({'tasks': tasks})


@app.route('/contents', methods=['POST'])
def create_tempearture():
    if not request.json or not 'temperature' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'temp': request.json['title'],
        'hum': request.json.get('descritpion', ""),
        'done': False
    }
    cursor = sqlite3.connect("./tempData.db").cursor()
    cursor.execute('''insert into running values('')''')


    return jsonify({'task': task}), 201


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': 'Not fetch'}), 404)


if __name__ == '__main__':
    app.run(debug=True)
