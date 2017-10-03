from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)

tasks = [{
    'id': 1,
    'temp': 38,
    'hum': 49,
    'done': False
}, {
    'id': 2,
    'temp': 44,
    'hum': 88,
    'done': False
}]


@app.route('/contents', methods=['GET'])
def get_tasks():

    return jsonify({'tasks': tasks})


@app.route('/contents', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'temp': request.json['title'],
        'hum': request.json.get('descritpion', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': 'Not fetch'}), 404)


if __name__ == '__main__':
    app.run(debug=True)
