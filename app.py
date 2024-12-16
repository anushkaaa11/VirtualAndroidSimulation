import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

# Database connection
def get_db():
    conn = sqlite3.connect('apps.db')
    conn.row_factory = sqlite3.Row
    return conn

# Initialize database
def init_db():
    with get_db() as conn:
        with open('schema.sql', 'r') as f:
            conn.executescript(f.read())

@app.route('/add-app', methods=['POST'])
def add_app():
    data = request.get_json()
    app_name = data.get('app_name')
    version = data.get('version')
    description = data.get('description')

    with get_db() as conn:
        conn.execute('INSERT INTO apps (app_name, version, description) VALUES (?, ?, ?)', 
                     (app_name, version, description))
    return jsonify({"message": "App added successfully"})

@app.route('/get-app/<int:id>', methods=['GET'])
def get_app(id):
    with get_db() as conn:
        app = conn.execute('SELECT * FROM apps WHERE id = ?', (id,)).fetchone()
    
    if app:
        return jsonify({
            "id": app["id"],
            "app_name": app["app_name"],
            "version": app["version"],
            "description": app["description"]
        })
    else:
        return jsonify({"message": "App not found"}), 404

@app.route('/delete-app/<int:id>', methods=['DELETE'])
def delete_app(id):
    with get_db() as conn:
        result = conn.execute('DELETE FROM apps WHERE id = ?', (id,))

    if result.rowcount:
        return jsonify({"message": "App deleted successfully"})
    else:
        return jsonify({"message": "App not found"}), 404

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
