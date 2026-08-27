import pandas as pd
import ast
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies = pd.read_csv("tmdb_5000_movies.csv")
credits = pd.read_csv("tmdb_5000_credits.csv")

movies = movies.merge(credits[["movie_id", "cast", "crew"]], left_on="id", right_on="movie_id", how="left")
def convert_names(text):
    try:
        data = ast.literal_eval(text)
        return " ".join(
            item["name"].replace(" ", "")
            for item in data[:5]
            if "name" in item
        )
    except:
        return ""

movies["cast"] = movies["cast"].fillna("").apply(convert_names)
movies["crew"] = movies["crew"].fillna("").apply(convert_names)

movies["tags"] = (
    movies["title"].fillna("").str.replace(" ", "") + " "
    + movies["cast"] + " "
    + movies["crew"]
)

tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(movies["tags"])

similarity = cosine_similarity(tfidf_matrix)


def recommend(movie_name):

    matches = movies[
        movies["title"].str.lower() == movie_name.lower()
    ]

    if matches.empty:
        print("\nMovie not found!")
        return

    index = matches.index[0]

    scores = list(enumerate(similarity[index]))

    scores = sorted(
        scores,
        key=lambda x: x[1],
        reverse=True
    )

    recommendations = []

def recommend(movie_name):

    matches = movies[
        movies["title"].str.lower() == movie_name.lower()
    ]

    if matches.empty:
        print("\nMovie not found!")
        return []

    index = matches.index[0]

    scores = list(enumerate(similarity[index]))

    scores = sorted(
        scores,
        key=lambda x: x[1],
        reverse=True
    )

    recommendations = []

    for i, score in scores[1:6]:
        recommendations.append(
            (
                movies.iloc[i]["title"],
                round(score * 100, 2),
            )
        )

    return recommendations


if __name__ == "__main__":
    print("\n==============================")
    print("MOVIE RECOMMENDATION SYSTEM")
    print("==============================")

    movie_name = input("\nEnter movie name: ")
    recommend(movie_name)