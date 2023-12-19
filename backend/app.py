from flask import Flask, request, jsonify
from content_based_recommender import contents_based_recommender
from flask_cors import CORS  # Import CORS from flask_cors

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


@app.route('/api/content-base-recommend', methods=['POST'])
def content_based_recommend_movies():
    try:
        data = request.get_json()
        movie_title = data.get('movie_title')

        # Get recommended movies as a list of titles
        recommended_movies = contents_based_recommender(movie_title, num_of_recomm=10)

        return jsonify({'recommendations': recommended_movies})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(port=5000)