#!/bin/bash

# Navigate to the project directory
cd /var/www/newai

# Pull the latest changes from the repository
git pull origin main

# Activate the virtual environment
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Restart the Flask app (you may need to adjust this to match your setup)
sudo systemctl restart newai
