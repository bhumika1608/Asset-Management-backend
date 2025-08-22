#!/bin/bash
gunicorn asset_management_backend.wsgi:application --bind 0.0.0.0:8000
