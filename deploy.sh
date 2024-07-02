#!/bin/bash

# Set your application's directory
APP_DIR="/var/www/newai"

# Navigate to the app directory
cd $APP_DIR

# Pull the latest changes from the main branch
git pull origin main

# Activate the virtual environment
source .venv/bin/activate

# Install any new dependencies
pip install -r requirements.txt

# Restart the application (example using systemd)
sudo systemctl restart newai.service

echo "Deployment completed successfully."
