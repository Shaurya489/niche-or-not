from data_fetchers.anime_api import get_anime_data
from data_fetchers.movie_api import get_movie_data
from core.classifier import classify_media

print("Anime or Movie")
choice=input("Enter your choice:")
choice.lower()
if(choice=="anime"):
    anime=input("Enter your anime:")
    live_data=get_anime_data(anime)
    print(classify_media(live_data))
elif(choice=="movie"):
    movie=input("Enter your movie:")
    live_data=get_movie_data(movie)
    print(classify_media(live_data))
else:
    print("Invalid Choice")