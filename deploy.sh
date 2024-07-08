#!/bin/bash

# Navigate to the project directory
cd /var/www/newai

# Pull the latest changes from the repository
git pull origin main

# Activate the virtual environment
source .venv/bin/activate

# Install any new dependencies
pip install -r requirements.txt

# Restart the application server (Assuming you are using gunicorn)
sudo systemctl restart newai

echo "Deployment complete!"
