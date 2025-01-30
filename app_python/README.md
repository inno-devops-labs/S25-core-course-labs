# Moscow Time Display

## Overview
A simple web app that shows the current time in Moscow. Built with Flask, updates automatically, and looks nice!

## Features
- Shows current Moscow time
- Updates automatically
- Works on phones too
- Nice clean design

## How to Install

1. Clone this repo
```bash
git clone <your-repo-url>
```

2. Go to the project folder
```bash
cd app_python
```

3. Install what you need (better use a virtual environment)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

4. Run it!
```bash
python app.py
```

5. Open http://127.0.0.1:8000 in your browser

## Pull Requests
I made 2 PRs for this project:
1. Initial setup with basic time display
2. Added auto-updates and better design

## Tech Used
- Python + Flask
- HTML & CSS
- pytz for Moscow time

## Local Setup Tips
- Make sure you have Python 3.x
- Virtual environment recommended
- Check requirements.txt for dependencies
- Needs internet for Moscow timezone data

## Notes
- Time is always Moscow time (MSK)
- Refreshes every second
- Works offline once loaded

Made with ☕ and Python
