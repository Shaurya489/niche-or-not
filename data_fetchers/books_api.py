import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_book_data(book_name):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    api_key=os.getenv("BOOKS_API")
    url=f"https://www.googleapis.com/books/v1/volumes?q=intitle:{book_name}&key={api_key}"
    response=requests.get(url,headers=headers)
    if(response.status_code==200):
        data=response.json()
        results=data.get('items',[])
        if(results):
            best_match = max(results, key=lambda x: x.get('volumeInfo', {}).get('ratingsCount', 0))
            book_info=best_match.get('volumeInfo',{})
            images=book_info.get("imageLinks",{}).get('thumbnail')
            features={
                "title":book_info.get("title"),
                "image":images,
                "engagement":int(book_info.get('ratingsCount',0)),
                "author":book_info.get('authors',[]),
                "score":book_info.get('averageRating',''),
                "media_type":"book"
            }
            return features
        else:
            return {"error":"Book not found"}
    else:
        return {"error": f"API request failed with status code {response.status_code}"}
    
if __name__ == "__main__":
    print("Testing a mainstream movie:")
    print(get_book_data("The Hobbit"))
    
    print("\nTesting a more niche movie:")
    
    print(get_book_data("Harry Potter"))