from flask import Flask, jsonify, abort

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


@app.route('/contents/<int:task_id>', methods=['GET'])
def get_tasks(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'tasks': task[0]})


if __name__ == '__main__':
    app.run(debug=True)
