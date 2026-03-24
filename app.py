import streamlit as st
from data_fetchers.anime_api import get_anime_data
from data_fetchers.movie_api import get_movie_data
from data_fetchers.movie_api import get_show_data
from core.classifier import classify_media

st.set_page_config(page_title="Niche or Not")
st.title("Niche or Not")
st.write("Is your taste truly niche like you claim?")

media_type=st.selectbox("What are you looking for?",["Anime","Movie","TV Show"])

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
        if "error" not in data:      
            verdict=(classify_media(data))
            col1,col2=st.columns([1,2])
            
            with col1:
                if data.get("image"):
                    st.image(data["image"],use_container_width=True)
                else:
                    st.write("No Image found")
            with col2:
                st.subheader(search_term)
                st.write(f"Verdict : {verdict}")
                st.write(f" Score: {data['score']}/10")
        else:
            st.write(f"Error!! {media_type} not found")
    else:
        st.warning("Please enter something")

    

