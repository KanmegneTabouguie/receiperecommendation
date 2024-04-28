from flask import Flask, jsonify, request, render_template
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

app = Flask(__name__)

# Load recipe data from JSON file
with open('recipes.json', 'r') as f:
    recipes = json.load(f)

# Preprocess data
def preprocess_data(recipes):
    processed_recipes = []
    for recipe in recipes:
        # Combine recipe attributes into a single string
        attributes = ' '.join(recipe['ingredients']) + ' ' + ' '.join(recipe['cooking_instructions'])
        processed_recipes.append(attributes)
    return processed_recipes

processed_data = preprocess_data(recipes)

# TF-IDF vectorization
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(processed_data)

# Recommendation function
def get_recommendations(dietary_preference, num_recommendations=5):
    indices = []
    for idx, recipe in enumerate(recipes):
        if dietary_preference in recipe['dietary_tags']:
            indices.append(idx)

    if len(indices) == 0:
        return []

    recommendations = []
    for idx in indices[:num_recommendations]:
        recipe_details = {
            'recipe_name': recipes[idx]['recipe_name'],
            'ingredients': recipes[idx]['ingredients'],
            'cooking_instructions': recipes[idx]['cooking_instructions']
        }
        recommendations.append(recipe_details)

    return recommendations

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recipes', methods=['GET'])
def get_all_recipes():
    return jsonify(recipes)

@app.route('/recipes/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    if recipe_id < 0 or recipe_id >= len(recipes):
        return jsonify({"error": "Recipe not found"}), 404
    return jsonify(recipes[recipe_id])

@app.route('/recommend', methods=['POST'])
def recommend_recipes():
    data = request.json
    dietary_preference = data.get('dietaryPreference')
    num_recommendations = int(data.get('numRecommendations', 5))

    if not dietary_preference:
        return jsonify({"error": "Dietary preference not provided"}), 400

    recommendations = get_recommendations(dietary_preference, num_recommendations)
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run()


