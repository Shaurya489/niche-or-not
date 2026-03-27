import requests
import  os
from dotenv import load_dotenv

load_dotenv()

def get_artist_data(artist_name):
    api_key=os.getenv("LASTFM_API_KEY")
    url=f"http://ws.audioscrobbler.com/2.0/?method=artist.search&artist={artist_name}&api_key={api_key}&format=json"
    imageurl=f"https://api.deezer.com/search/artist?q={artist_name}"
    response=requests.get(url)
    imageresponse=requests.get(imageurl)
    if(response.status_code==200):
        data=response.json()
        imagedata=imageresponse.json()
        deezer_results=imagedata.get('data', [])
        results=data.get('results',{}).get('artistmatches',{}).get('artist',[])
        artist_image = deezer_results[0].get('picture_xl')
        if(results):
            artist_info=results[0]
            
            features={
                "title":artist_info.get("name"),
                "image":artist_image, 
                "engagement":int(artist_info.get("listeners",0)),
                "media_type":"music"
            }
            return features
        else:
            return {"error":"Artist not found"}
    else:
        return {"error": f"API request failed with status code {response.status_code}"}
   
if __name__ == "__main__":
    print("Testing a mainstream movie:")
    print(get_artist_data("Nirvana"))
    
    print("\nTesting a more niche movie:")
    
    print(get_artist_data("Taylor swift"))