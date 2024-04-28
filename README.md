# Recipe Recommendation System

This is a simple Flask application that provides recipe recommendations based on dietary preferences. Users can select their dietary preference (e.g., vegetarian, meat, fish) and specify the number of recipe recommendations they want to receive. The application utilizes machine learning techniques to generate recommendations using TF-IDF vectorization and cosine similarity.

## Features

1. **Dietary Preference Selection:** Users can choose their dietary preference from options like vegetarian, meat, or fish.
2. **Customizable Recommendations:** Users can specify the number of recipe recommendations they want to receive.
3. **Recipe Information:** Users can view detailed information about individual recipes, including ingredients and cooking instructions.

## Tools Used

- **Flask:** Python web framework used for developing the backend of the application.
- **scikit-learn:** Python library used for machine learning tasks, specifically for TF-IDF vectorization and recommendation generation.
- **HTML/CSS/JavaScript:** Frontend technologies used for designing and implementing the user interface.
- **JSON:** Data format used for storing recipe data.
- **Docker:** Containerization tool used for packaging the application and its dependencies into a container for easy deployment.

## Setup Instructions

1. Install Python and Flask on your system.
2. Clone the repository and navigate to the project directory.
3. Run `pip install -r requirements.txt` to install the required dependencies.
4. Run `python app.py` to start the Flask server.
5. Access the application in your web browser at `http://localhost:5000`.

## Usage

1. Visit the homepage of the application.
2. Select your dietary preference from the dropdown menu.
3. Specify the number of recipe recommendations you want to receive.
4. Click the "Get Recommendation" button to view the recommended recipes.
5. Explore individual recipes by clicking on their titles.

## Contributing

Contributions are welcome! Feel free to submit bug reports, feature requests, or pull requests on GitHub.

