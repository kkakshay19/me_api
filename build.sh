#!/usr/bin/env bash
# Build script for Render deployment

set -o errexit  # Exit on error

echo "Starting build process..."

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Run migrations
echo "Running migrations..."
python manage.py migrate --noinput

# Seed database (optional - comment out if you don't want to seed on every deploy)
echo "Seeding database..."
python manage.py seed || echo "Seed command failed or no seed data"

echo "Build completed successfully!"
