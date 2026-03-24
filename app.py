import streamlit as st
from data_fetchers.anime_api import get_anime_data
from data_fetchers.movie_api import get_movie_data
from core.classifier import classify_media

st.set_page_config(page_title="Niche or Not")
st.title("Niche or Not")
st.write("Is your taste truly niche like you claim?")

media_type=st.selectbox("What are you looking for?",["Anime","Movie"])

search_term=st.text_input(f"Enter the name of the {media_type}:")
data={}
if(st.button("Check Niche-ness")):
    if search_term:
        if(media_type=="Anime"):
            data=get_anime_data(search_term)
            
        elif(media_type=="Movie"):
            data=get_movie_data(search_term)
    else:
        st.warning("Please enter something")
        
verdict=(classify_media(data))
if(verdict=="Mainstream"):
    st.write("Your choice is highly popular!")

elif (verdict=="Popular"):
    st.write("Your choice is popular")
    
elif(verdict=="LesserKnown"):
    st.write("Your choice is lesser known")
    
elif(verdict=="Niche"):
    st.write("Your choice is Niche. Congrats you won.")

