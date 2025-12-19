#!/bin/sh
set -e

# Path to DB inside container (default to /data/employees.db)
DB_PATH=${EMPLOYEE_DB_PATH:-/data/employees.db}
DB_DIR=$(dirname "$DB_PATH")
mkdir -p "$DB_DIR"

if [ ! -f "$DB_PATH" ]; then
	echo "Database not found at $DB_PATH. Initializing..."
	python - <<PY
from app import init_db
init_db()
print('Database initialized')
PY
else
	echo "Database found at $DB_PATH. Skipping initialization."
fi

# Start Gunicorn
exec gunicorn -b 0.0.0.0:5000 app:app
