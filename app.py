import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()
from data_fetchers.anime_api import get_anime_data
from data_fetchers.movie_api import get_movie_data
from data_fetchers.movie_api import get_show_data
from data_fetchers.spotify_api import get_artist_data
from data_fetchers.books_api import get_book_data
from core.classifier import classify_media

st.set_page_config(page_title="Niche or Not")
st.title("Niche or Not")
st.write("Is your taste truly niche like you claim?")

media_type=st.selectbox("What are you looking for?",["Anime","Movie","TV Show","Artist/Band","Book"])

search_term=st.text_input(f"Enter the name of the {media_type}:")
data={}
if(st.button("Check Niche-ness")):
    if search_term:
        if(media_type=="Anime"):
            data=get_anime_data(search_term)
            
        elif(media_type=="Movie"):
            data=get_movie_data(search_term)
            
        elif(media_type=="TV Show"):
            data=get_show_data(search_term)
        elif(media_type=="Artist/Band"):
            data=get_artist_data(search_term)
        elif(media_type=="Book"):
            data=get_book_data(search_term) 
            st.write("DEBUG:", data)
        if "error" not in data:     
            st.markdown(f"""
                        <style>
                        .stApp{{
                            background:transparent;
                        }}
                        @keyframes fadeIn{{
                            0% {{ opacity:0;}}
                            100% {{ opacity:1}}
                        }}
                        
                        .popout-bg{{
                            position:fixed;
                            top:0;
                            left:0;
                            width:100vw;
                            height:100vh;
                            background-image:url('{data["image"]}');
                            background-size:cover;
                            background-position:center;
                            filter:blur(20px) brightness(0.4);
                            z-index:-1;
                            animation:fadeIn 0.8s ease-in-out;
                        }}
                        
                        .main-content{{
                            animation:fadeIn 1.2s ease-in-out;
                        }}
                        h1,h2,h3,p{{
                            color: #f0f0f0;
                            text-shadow:2px 2px 4px rgba(0,0,0,0.5);
                        }}
                        
                        </style>
                        <div class="popout-bg"></div>
                        
                        """,unsafe_allow_html=True) 
            verdict=(classify_media(data))
            col1,col2=st.columns([1,2])
            
            with col1:
                if data.get("image"):
                    st.image(data["image"],width='stretch')
                else:
                    st.write("No Image found")
            with col2:
                st.subheader(data['title'])
                st.write(f"Verdict : {verdict}")
                if(media_type=="Book"):
                    st.write(f" Score: {data['score']}/5")
                    st.write(f"Author: {data['author']}")
                if(media_type!="Artist/Band" and media_type!="Book"):
                    st.write(f" Score: {data['score']}/10")
        else:
            st.warning(f"{media_type} not found")
    else:
        st.warning("Please enter something")

with st.sidebar:
    st.write("Made by Shaurya Pratap Singh")
    st.write("Contact : shauryapratapsingh489@gmail.com")
    st.write("Used TMDB and Jikan APIs")

