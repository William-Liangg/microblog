#!/usr/bin/env python3
"""
Helper script to run the Flask application with virtual environment.
Make sure to activate your virtual environment first:
source venv/bin/activate
"""

from microblog import app

if __name__ == '__main__':
    print("Starting Flask application...")
    print("Make sure your virtual environment is activated!")
    print("To activate: source venv/bin/activate")
    app.run(debug=True, host='0.0.0.0', port=5001) 