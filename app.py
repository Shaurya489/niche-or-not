import streamlit as st


from data_fetchers.anime_api import get_anime_data
from data_fetchers.movie_api import get_movie_data
from data_fetchers.movie_api import get_show_data
from data_fetchers.spotify_api import get_artist_data
from data_fetchers.books_api import get_book_data
from core.classifier import classify_media
from core.classifier import normalize

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
                background-image:url("https://w.wallhaven.cc/full/6l/wallhaven-6l5emq.png");
                background-size:cover;
                background-position:center;
                filter:blur(10px) brightness(0.4);
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

st.set_page_config(page_title="Niche or Not")
st.title("Niche or Not")

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
            
            raw_engagement=data.get("engagement",0)
            score=normalize(raw_engagement,media_type)
            niche_meter=100-score
            with col1:
                if data.get("image"):
                    st.image(data["image"],width='stretch')
                else:
                    st.write("Image not found")
            with col2:
                st.subheader(data['title'])
                st.write(f"Verdict : {verdict}")
                if(media_type=="Book"):
                    st.write(f"Author: {data['author']}")
                if(media_type!="Artist/Band" and media_type!="Book"):
                    st.write(f" Score: {data['score']}/10")
            
            st.metric(label="Niche Meter",value=f"{niche_meter:.1f}%")
            st.progress(niche_meter/100)
            
            if(niche_meter>85):
                st.success("Elite taste")
            elif(niche_meter>50):
                st.info("Cultured")
            else:
                st.warning("Mainstream")
            
        else:
            st.warning(f"{media_type} not found")
    else:
        st.warning("Please enter something")
else:
    st.divider()
    st.info("Pick a category and search above to test your taste")
    
with st.sidebar:
    st.write("Made by Shaurya Pratap Singh")
    st.write("Contact : shauryapratapsingh489@gmail.com")
    st.write("Used TMDB,Jikan,OpenLibrary,lastFM,Deezer APIs")

