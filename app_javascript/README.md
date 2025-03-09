# Year and Funny Ads API 🎯

## ✨ Features
- Get current year
- Fetch random funny advertisements
- Combined endpoint for both year and ad
- RESTful API design
- JSON responses
- Error handling

## 🔧 Prerequisites
- Node.js (v14 or higher)
- npm (v6 or higher)

## 🚀 Installation

1. Clone the repository:
```bash
git clone git@github.com:SergePolin/S25-core-course-labs.git
cd app_javascript
```

2. Install dependencies:
```bash
npm install
```

3. Start the server:
```bash
npm start
```

For development with auto-reload:
```bash
npm run dev
```

## 💻 Usage

The server runs on `http://localhost:3000` with the following endpoints:

### Get Current Year
```http
GET /year
```

Response:
```json
{
    "year": 2024
}
```

### Get Random Advertisement
```http
GET /ad
```

Response:
```json
{
    "advertisement": "Our coffee is so strong, it can wake up your neighbor's dreams!"
}
```

### Get Both Year and Advertisement
```http
GET /year-and-ad
```

Response:
```json
{
    "year": 2024,
    "advertisement": "Our mattresses are so comfortable, counting sheep will file for unemployment."
}
```

## 🛠 Development

### Code Style
- ESLint configuration for code linting
- Prettier for code formatting
- EditorConfig for consistent coding style
```
