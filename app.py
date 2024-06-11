from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return tasks

@app.route("/tasks", methods=["POST"])
def add_task():
    task = request.json.get("task")
    
    if task:
        tasks.append({"task": task, 'completed': False})
        return jsonify({"msg": "Task added"}), 201
    return jsonify({"msg": "No task provided"}), 400

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
        return jsonify({"msg": "Task deleted"}), 200
    return jsonify({"msg": "Task not found"}), 404

@app.route('/tasks/<int:task_id>/complete', methods=['PATCH'])
def complete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]['completed'] = True
        return jsonify({'message': 'Task marked as complete!'}), 200
    return jsonify({'message': 'Task not found!'}), 404

if __name__ == "__main__":
    app.run(debug=True)