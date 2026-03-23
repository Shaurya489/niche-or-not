def classify_media(data):
    if "error" in data:
        return data["error"]
    engagement = data.get("engagement")
    media_type = data.get("media_type")
    
    if media_type=="anime":
        if(engagement>=2000000):
            return "Mainstream"
        elif(1000000<=engagement<2000000):
            return "Popular"
        elif(100000<=engagement<1000000):
            return "LesserKnown"
        else:
            return "Niche"
    elif media_type=="movie":
        if(engagement>=30000):
            return "Mainstream"
        elif(10000<=engagement<20000):
            return "Popular"
        elif(1000<=engagement<10000):
            return "LesserKnown"
        else:
            return "Niche"
    elif media_type=="game":
        pass
    else:
        return "Unknown media type."
    
    
if(__name__=="__main__"):
    from data_fetchers.movie_api import get_movie_data
    
    live_data=get_movie_data("Top Gun")
    
    print(f"Data:{live_data}")
    print(f"Verdict:{classify_media(live_data)}")