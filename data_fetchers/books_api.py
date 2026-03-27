import requests

def get_book_data(book_name):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    url=f"https://www.googleapis.com/books/v1/volumes?q=intitle:{book_name}"
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
                "engagement":book_info.get('ratingsCount',0),
                "author":book_info.get('authors')[0],
                "score":book_info.get('averageRating'),
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