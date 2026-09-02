import streamlit as st
from movie_recommendation import recommend

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬"
)

st.title("🎬 Movie Recommendation System")
st.write("Enter a movie name to get similar movie recommendations.")

movie_name = st.text_input(
    "Enter Movie Name",
    placeholder="e.g. Avatar"
)

if st.button("Recommend"):
    if movie_name:
        recommendations = recommend(movie_name)

        st.subheader("Recommended Movies:")

        if recommendations:
            for movie in recommendations:
                st.write(movie)
        else:
            st.warning("No recommendations found.")
    else:
        st.warning("Please enter a movie name.")