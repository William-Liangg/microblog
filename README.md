# Microblog Flask Application

This is a Flask web application running in a virtual environment.

## Setup and Usage

### 1. Activate the Virtual Environment
```bash
source venv/bin/activate
```

You should see `(venv)` appear in your terminal prompt, indicating the virtual environment is active.

### 2. Verify Flask Installation
```bash
python -c "import flask; print(f'Flask version: {flask.__version__}')"
```

### 3. Run the Application
You have two options:

**Option A: Run directly**
```bash
python microblog.py
```

**Option B: Use the helper script**
```bash
python run.py
```

### 4. Access the Application
Open your web browser and go to: `http://localhost:5000`

### 5. Deactivate Virtual Environment (when done)
```bash
deactivate
```

## Dependencies

All dependencies are listed in `requirements.txt`:
- Flask 3.1.1 (latest version)
- All required Flask dependencies

## Troubleshooting

If you encounter import errors:
1. Make sure your virtual environment is activated (`source venv/bin/activate`)
2. Verify Flask is installed: `pip list | grep Flask`
3. If Flask is missing, install it: `pip install flask`

## Note

This application is configured to run in a virtual environment, not in Anaconda. Make sure to always activate the virtual environment before running the application. 