import requests

def get_book_data(book_name):
    url=f"https://openlibrary.org/search.json?q={book_name}&fields=cover_i,author_name,title,edition_count,want_to_read_count,already_read_count,ratings_count,ratings_average&limit=5"
    
    response=requests.get(url)
    
    if response.status_code==200:
        data=response.json()
        docs=data.get('docs',[])

        if docs:
            book=max(docs, key=lambda x: (
                    int(x.get('want_to_read_count', 0))+int(x.get('already_read_count', 0))+int(x.get('ratings_count', 0))
                ))
            
            ratings=book.get('want_to_read_count',0)+book.get('already_count',0)+book.get('ratings_count',0)
            
            
            
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