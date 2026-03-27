import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_book_data(book_name):
    api_key = os.getenv("BOOKS_API")
    headers = {
         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
         "Accept": "application/json"
    }
    
    
    query = book_name.replace(" ", "+")
    url = f"https://www.googleapis.com/books/v1/volumes?q=intitle:{query}&key={api_key}"
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            results = data.get('items', [])
            if results:
                
                best_match = max(results, key=lambda x: x.get('volumeInfo', {}).get('ratingsCount', 0))
                book_info = best_match.get('volumeInfo', {})
                
            
                authors = book_info.get('authors', ["Unknown Author"])
                author_name = authors[0] if authors else "Unknown Author"
                
            
                img_links = book_info.get("imageLinks", {})
                image = img_links.get('thumbnail') or img_links.get('smallThumbnail')
                if image:
                    image = image.replace("http://", "https://")
                
                return {
                    "title": book_info.get("title", "Unknown Title"),
                    "image": image,
                    "engagement": int(book_info.get('ratingsCount', 0)),
                    "author": author_name,
                    "score": book_info.get('averageRating', 0),
                    "media_type": "book"
                }
            return {"error": "Book not found"}
        return {"error": f"API request failed: {response.status_code}"}
    except Exception as e:
        return {"error": str(e)}