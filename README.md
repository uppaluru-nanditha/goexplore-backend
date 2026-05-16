# GoExplore Backend 🚀

FastAPI backend powering the GoExplore tourist guide web application.

## Features
- 🌍 REST API serving city data
- ✨ AI-powered city recommendations by category
- 🔍 City search endpoint
- ⚡ Fast and lightweight with FastAPI

## Tech Stack
- Python 3.9
- FastAPI
- Uvicorn
- CORS Middleware

## Getting Started

```bash
# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate

# Install dependencies
pip install "fastapi[all]"

# Run the server
uvicorn main:app --reload
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Health check |
| GET | /cities | Get all cities |
| GET | /cities/search/{query} | Search cities |
| GET | /cities/recommend/{category} | Get AI recommendations |
| GET | /categories | Get all categories |

## Author
**Naga Nanditha Uppaluru**
- GitHub: [@uppaluru-nanditha](https://github.com/uppaluru-nanditha)
- LinkedIn: [nanditha-uppaluru](https://linkedin.com/in/nanditha-uppaluru)