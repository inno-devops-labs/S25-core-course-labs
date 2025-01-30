# Moscow Time Display

A modern web application that displays the current time in Moscow, Russia, built with FastAPI and Python.

## 🌟 Features

- Real-time display of Moscow time
- RESTful API endpoints
- Type-safe implementation
- Comprehensive error handling

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1.Clone the repository:

```bash
git clone git@github.com:SergePolin/S25-core-course-labs.git
cd app_python
```

2.Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3.Install dependencies:

```bash
pip install -r requirements.txt
```

### Running the Application

1. Start the development server:

```bash
python main.py
```

2.Open your browser and navigate to:

- Web Interface: <http://localhost:8000>
- API Documentation: <http://localhost:8000/docs>

## 🛠️ Technical Stack

- **Backend Framework**: FastAPI
- **Template Engine**: Jinja2
- **Time Management**: pytz
- **Configuration**: pydantic-settings
- **Development Server**: uvicorn

## 📚 API Documentation

### Endpoints

1. `GET /`
   - Renders the main page with Moscow time
   - Response: HTML

2. `GET /get_time`
   - Returns current Moscow time in JSON format
   - Response:

     ```json
     {
       "moscow_time": "HH:MM:SS",
       "current_time": "YYYY-MM-DD HH:MM:SS TZ"
     }
     ```

## 📦 Project Structure

```bash
app_python/
├── main.py              # Main application file
├── config.py            # Configuration settings
├── requirements.txt     # Project dependencies
├── .env                 # Environment variables
├── README.md           # Project documentation
├── PYTHON.md           # Python best practices
├── templates/          # HTML templates
│   └── index.html     # Main page template
└── .gitignore         # Git ignore rules
```

## 👥 Author

- Sergei Polin - Initial work

## 🙏 Acknowledgments

- FastAPI team for the excellent framework
- Python community for the amazing ecosystem
