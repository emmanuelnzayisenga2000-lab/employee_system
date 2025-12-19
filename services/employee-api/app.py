from flask import Flask, jsonify, request, abort
app = Flask(__name__)

# simple in-memory store
EMPLOYEES = [
    {"id": 1, "first_name": "Alice", "last_name": "Smith", "role": "Engineer"},
    {"id": 2, "first_name": "Bob", "last_name": "Jones", "role": "Manager"}
]

@app.route('/employees', methods=['GET'])
def list_employees():
    return jsonify(EMPLOYEES)

@app.route('/employees', methods=['POST'])
def add_employee():
    if not request.json:
        abort(400, 'Missing JSON body')
    data = request.json
    if 'first_name' not in data or 'last_name' not in data:
        abort(400, 'Missing fields')
    new_id = max(e['id'] for e in EMPLOYEES) + 1 if EMPLOYEES else 1
    emp = {
        'id': new_id,
        'first_name': data['first_name'],
        'last_name': data['last_name'],
        'role': data.get('role', 'Employee')
    }
    EMPLOYEES.append(emp)
    return jsonify(emp), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
