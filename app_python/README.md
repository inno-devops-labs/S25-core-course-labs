## Moscow Time Web Application

### Overview
This Flask-based web application displays the current time in Moscow.

### Installation

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/whatislav/S25-core-course-labs
   cd app_python
   ```
2. **Create a Virtual Environment:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```
3. **Install Dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Run the Application:**
   ```sh
   python app.py
   ```
5. **Access the Web App:**
   Open `http://127.0.0.1:5000/` in your browser.

### File Structure
- `app.py` - Main entry point of the application.
- `services/get_time_service.py` - Service class handling time retrieval.
- `config.py` - Stores configuration settings (timezone).
- `templates/current_time.html` - HTML template for displaying time.


### Docker Support

#### How to Build the Docker Image:
```sh
docker build -t moscow-time-app .
```

#### How to Run the Container:
```sh
docker run -p 5000:5000 moscow-time-app
```

#### How to Pull and Run from Docker Hub:
```sh
docker pull whatislav/moscow-time-app:1.0
docker run -p 5000:5000 whatislav/moscow-time-app:1.0
```
