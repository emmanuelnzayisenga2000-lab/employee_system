Employee Management System - DevOps Project

Unique DevOps identifier: `25RP18224-nzayisenga`

Overview

This repository contains an example Employee Management microservice (Flask), containerization, Kubernetes manifests, CI/CD pipeline, Ansible playbook for VM provisioning, and monitoring manifests (Prometheus/Grafana). Use this as the basis for your assignment; adapt and expand as required.

Structure

- `services/employee-api` - Flask microservice
- `k8s/` - Kubernetes manifests (namespace uses `25RP18224-nzayisenga`)
- `.github/workflows/ci.yml` - CI pipeline
- `ansible/` - Playbook and roles for VM provisioning
- `monitoring/` - Prometheus/Grafana configs
- `docs/` - Report template and submission materials
- `evidence/` - Evidence folder for screenshots/logs

Quick start (local using docker-compose)

1. Build image:

   docker build -t employee-api:25RP18224-nzayisenga ./services/employee-api

2. Run the app:

   docker run -p 5000:5000 employee-api:25RP18224-nzayisenga

Run tests (local)

- Node syntax check and Python tests (runs Docker):

   ```bash
   npm test
   ```

This will perform a Node syntax check for `services/index` and then build the `employee-api` image and run the service unit tests inside a container. Docker must be available on your machine for `npm test` to run the Python tests.

API

- GET /employees - list employees
- POST /employees - add employee (json payload)

See `docs/report-template.md` for the full technical report template and submission checklist.
