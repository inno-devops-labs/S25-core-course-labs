# Python MSK Time Application

## Overview

A simple Python web application built with Flask that displays the current time in Moscow (MSK). The time updates upon every page refresh.

## Features

- **Real-Time MSK**: Pulls the current time in Moscow and renders it in the browser.
- **Lightweight & Simple**: Only requires Flask and pytz to run.
- **Well-Documented**: This README and PYTHON.md explain setup, usage, and best practices.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/MohamadSafi/S25-core-course-labs.git
   cd S25-core-course-labs
   ```

2. **Create and activate a virtual environment** (recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # or
   venv\Scripts\activate  # Windows
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Flask application**:

   ```bash
   python main.py
   ```

2. **Open a browser** at http://127.0.0.1:5000/ (default Flask port).

   You should see the current time in Moscow displayed. Refresh the page to watch it update.
