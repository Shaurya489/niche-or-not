import requests

def get_book_data(book_name):
    
    url=f"https://www.googleapis.com/books/v1/volumes?q={book_name}"
    response=requests.get(url)
    if(response.status_code==200):
        data=response.json()
        results=data.get('items',[])
        if(results):
            book_info=results[0].get('volumeInfo',{})
            images=book_info.get("imageLinks",{}).get('thumbnail')
            features={
                "title":book_info.get("title"),
                "image":images,
                "engagement":book_info.get('ratingsCount',0),
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