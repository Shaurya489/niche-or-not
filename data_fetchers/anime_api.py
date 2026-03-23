import requests
def get_anime_data(anime_name):
    url = f"https://api.jikan.moe/v4/anime?q={anime_name}&limit=1"
    response=requests.get(url)
    if(response.status_code==200):
        data=response.json()
        if(data['data']):
            anime_info=data['data'][0]
            features={
                "title":anime_info.get("title"),
                "score":anime_info.get("score"),
                "engagement":anime_info.get("members"),
                "popularity_rank":anime_info.get("popularity"),
                "media_type":"anime"
            }
            return features
        else:
            return {"error":"Anime not found"}
    else:
        return {"error": f"API request failed with status code {response.status_code}"}
    
if __name__ == "__main__":
    print("Testing a mainstream anime:")
    print(get_anime_data("Naruto"))
    
    print("\nTesting a more niche anime:")
    print(get_anime_data("Jujutsu Kaisen"))