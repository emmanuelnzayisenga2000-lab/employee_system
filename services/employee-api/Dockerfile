FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1
ENV EMPLOYEE_DB_PATH=/data/employees.db

WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app

# Ensure entrypoint is executable
RUN chmod +x /app/entrypoint.sh

# Persist database under /data
VOLUME ["/data"]

EXPOSE 5000
CMD ["/app/entrypoint.sh"]
