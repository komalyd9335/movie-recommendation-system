import streamlit as st
from movie_recommendation import recommend

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬"
)

st.title("🎬 Movie Recommendation System")
st.write("Find movies similar to your favourite movie.")

movie = st.text_input("Enter Movie Name")

if st.button("Recommend"):
    if movie:
        recommendations = recommend(movie)

        if recommendations:
            st.subheader("Recommended Movies")

            for item in recommendations:
                st.write(item)
        else:
            st.warning("Movie not found. Please try another movie.")
    else:
        st.warning("Please enter a movie name.")