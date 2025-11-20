#!/bin/bash
# Munch Assistant - Quick Run Script

echo "🎤 Starting Munch Assistant..."
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed!"
    echo "Please install Python 3.6 or higher"
    exit 1
fi

# Run the application
python3 munch.py
