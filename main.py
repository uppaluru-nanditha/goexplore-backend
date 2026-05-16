from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

cities = [
    {"id": 1, "name": "Paris", "country": "France", "emoji": "🗼", "description": "The city of love and lights, famous for the Eiffel Tower and incredible cuisine.", "category": "romance"},
    {"id": 2, "name": "Tokyo", "country": "Japan", "emoji": "🗾", "description": "A vibrant mix of traditional culture and futuristic technology.", "category": "culture"},
    {"id": 3, "name": "New York", "country": "USA", "emoji": "🗽", "description": "The city that never sleeps, home to Times Square and Central Park.", "category": "adventure"},
    {"id": 4, "name": "Dubai", "country": "UAE", "emoji": "🏙️", "description": "A modern marvel in the desert with stunning skyscrapers and luxury experiences.", "category": "luxury"},
    {"id": 5, "name": "London", "country": "UK", "emoji": "🎡", "description": "A historic city with iconic landmarks like Big Ben and Buckingham Palace.", "category": "culture"},
    {"id": 6, "name": "Sydney", "country": "Australia", "emoji": "🦘", "description": "Famous for its Opera House, beautiful beaches and outdoor lifestyle.", "category": "adventure"},
    {"id": 7, "name": "Rome", "country": "Italy", "emoji": "🏛️", "description": "The eternal city with ancient ruins, art, and world-class food.", "category": "culture"},
    {"id": 8, "name": "Bali", "country": "Indonesia", "emoji": "🌴", "description": "A tropical paradise with stunning temples, rice terraces and beaches.", "category": "romance"},
]

@app.get("/")
def read_root():
    return {"message": "GoExplore API is running!"}

@app.get("/cities")
def get_cities():
    return cities

@app.get("/cities/search/{query}")
def search_cities(query: str):
    results = [c for c in cities if query.lower() in c["name"].lower() or query.lower() in c["country"].lower()]
    return results

@app.get("/cities/recommend/{category}")
def recommend_cities(category: str):
    matches = [c for c in cities if c["category"] == category.lower()]
    if not matches:
        return random.sample(cities, min(3, len(cities)))
    return matches

@app.get("/categories")
def get_categories():
    return ["romance", "culture", "adventure", "luxury"]