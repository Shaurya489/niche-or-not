import requests
import  os
from dotenv import load_dotenv

load_dotenv()

def get_movie_data(movie_name):
    token=os.getenv("TMDB_API_KEY")
    url=f"https://api.themoviedb.org/3/search/movie"
    params={
        "api_key":token,
        "query":movie_name
    }
    response=requests.get(url,params=params)
    if(response.status_code==200):
        data=response.json()
        if(data['results']):
            movie_info=data['results'][0]
            features={
                "title":movie_info.get("title"),
                "score":movie_info.get("vote_average"),
                "engagement":movie_info.get("vote_count"),
                "media_type":"movie"
            }
            return features
        else:
            return {"error":"Movie not found"}
    else:
        return {"error": f"API request failed with status code {response.status_code}"}
  
def get_show_data(show_name):
    token=os.getenv("TMDB_API_KEY")
    url=f"https://api.themoviedb.org/3/search/tv"
    params={
        "api_key":token,
        "query":show_name
    }
    response=requests.get(url,params=params)
    if(response.status_code==200):
        data=response.json()
        if(data['results']):
            show_info=data['results'][0]
            features={
                "title":show_info.get("title"),
                "score":show_info.get("vote_average"),
                "engagement":show_info.get("vote_count"),
                "media_type":"show"
            }
            return features
        else:
            return {"error":"Show not found"}
    else:
        return {"error": f"API request failed with status code {response.status_code}"}
    
if __name__ == "__main__":
    print("Testing a mainstream movie:")
    print(get_movie_data("Inception"))
    
    print("\nTesting a more niche movie:")
    print(get_movie_data("Top Gun"))