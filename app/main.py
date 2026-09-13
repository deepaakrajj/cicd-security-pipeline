from flask import Flask, jsonify, request

app = Flask(__name__)

todos = []


@app.route("/todos", methods=["GET"])
def get_todos():
    return jsonify(todos)


@app.route("/todos", methods=["POST"])
def add_todo():
    data = request.get_json()
    if not data or "task" not in data:
        return jsonify({"error": "task field required"}), 400
    todos.append({"id": len(todos) + 1, "task": data["task"]})
    return jsonify(todos[-1]), 201


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(debug=False, host="127.0.0.1", port=5000)
