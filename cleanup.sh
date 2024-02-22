#!/bin/bash

# Deactivate the virtual environment (if activated)
deactivate 2>/dev/null

# Remove the virtual environment
rm -rf venv

# Remove installed dependencies (if requirements.txt exists)
if [ -f requirements.txt ]; then
    pip uninstall -r requirements.txt -y
fi
