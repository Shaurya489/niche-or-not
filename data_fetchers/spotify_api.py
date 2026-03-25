import requests
import  os
from dotenv import load_dotenv

load_dotenv()

def get_artist_data(artist_name):
    api_key=os.getenv("LASTFM_API_KEY")
    url=f"http://ws.audioscrobbler.com/2.0/?method=artist.search&artist={artist_name}&api_key={api_key}&format=json"
    response=requests.get(url)
    if(response.status_code==200):
        data=response.json()
        results=data.get('results',{}).get('artistmatches',{}).get('artist',[])
        if(results):
            artist_info=results[0]
            images=artist_info.get("image",[])
            image_url=images[-1].get("#text") if images else None
            features={
                "title":artist_info.get("name"),
                "image":image_url, 
                "engagement":artist_info.get("listeners",0),
                "media_type":"music"
            }
            return features
        else:
            return {"error":"Movie not found"}
    else:
        return {"error": f"API request failed with status code {response.status_code}"}
   
if __name__ == "__main__":
    print("Testing a mainstream movie:")
    print(get_artist_data("Nirvana"))
    
    print("\nTesting a more niche movie:")
    print(get_artist_data("Taylor swift"))