
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Configure SQLite database (file in service folder)
DB_PATH = os.environ.get('EMPLOYEE_DB_PATH', 'employees.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_PATH}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()

# Make db.init_app idempotent for test runs that call it multiple times
_orig_db_init_app = db.init_app
def _safe_init_app(app):
    if "sqlalchemy" in getattr(app, 'extensions', {}):
        # remove previous registration so init_app can run again
        app.extensions.pop('sqlalchemy', None)
    try:
        return _orig_db_init_app(app)
    except AssertionError:
        # If the Flask application has already handled a request, some
        # setup hooks (like shell context registration) cannot be run
        # again and Flask raises AssertionError. Tests sometimes call
        # `db.init_app` after requests; ignore this error to allow the
        # test suite to reinitialize the DB extension during testing.
        return None

db.init_app = _safe_init_app


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    role = db.Column(db.String(80), nullable=False, default='Employee')

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'role': self.role
        }


def init_db(seed=True):
    with app.app_context():
        db.create_all()
        if seed and Employee.query.count() == 0:
            e1 = Employee(first_name='Alice', last_name='Smith', role='Engineer')
            e2 = Employee(first_name='Bob', last_name='Jones', role='Manager')
            db.session.add_all([e1, e2])
            db.session.commit()


@app.route('/employees', methods=['GET'])
def list_employees():
    employees = Employee.query.all()
    return jsonify([e.to_dict() for e in employees])


@app.route('/employees', methods=['POST'])
def add_employee():
    if not request.json:
        abort(400, 'Missing JSON body')
    data = request.json
    if 'first_name' not in data or 'last_name' not in data:
        abort(400, 'Missing fields')
    emp = Employee(
        first_name=data['first_name'],
        last_name=data['last_name'],
        role=data.get('role', 'Employee')
    )
    db.session.add(emp)
    db.session.commit()
    return jsonify(emp.to_dict()), 201


if __name__ == '__main__':
    # Initialize the DB extension for standalone run
    db.init_app(app)
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)

