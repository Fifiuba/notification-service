#!/usr/bin/env
set -e
poetry run pytest -v -s --cov=admin_service tests/ --cov-report=xml
