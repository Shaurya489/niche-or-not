import requests

def get_book_data(book_name):
    url=f"https://openlibrary.org/search.json?q={book_name.replace(' ', '+')}"
    
    response=requests.get(url)
    
    if response.status_code==200:
        data=response.json()
        docs=data.get('docs',[])

        if docs:
            book=max(docs, key=lambda x: (
                    int(x.get('edition_count', 0))
                ))
            
            ratings=book.get('edition_count',0)
            
            
            
            cover_id=book.get('cover_i')
            image=f"https://covers.openlibrary.org/b/id/{cover_id}-L.jpg" 
            
            avg_rating=book.get('ratings_average',0)
            
            return{
                "title":book.get("title","Unknown"),
                "image":image,
                "engagement":int(ratings),
                "author":book.get("author_name",["Unknown"])[0],
                "score":round(float(avg_rating)*2,1) if avg_rating else 0,
                "media_type":"book"
            }
    return {"error":"Book not found"}  