function getRecommendations() {
    // Get user inputs
    var dietaryPreference = document.getElementById("dietaryPreference").value;
    var numRecommendations = document.getElementById("numRecommendations").value;

    // Construct request body
    var data = {
        "dietary_preference": dietaryPreference,
        "num_recommendations": numRecommendations
    };

    // Send POST request to Flask backend
    fetch('/recommend', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        // Display recommendations on the web page
        displayRecommendations(data);
    })
    .catch(error => console.error('Error:', error));
}

function displayRecommendations(recommendations) {
    var recommendationsContainer = document.getElementById("recommendations");
    recommendationsContainer.innerHTML = ""; // Clear previous recommendations

    recommendations.forEach(recipe => {
        var recipeDiv = document.createElement("div");
        recipeDiv.classList.add("recipe");

        var recipeName = document.createElement("h2");
        recipeName.textContent = recipe.recipe_name;
        recipeDiv.appendChild(recipeName);

        var ingredientsHeader = document.createElement("h3");
        ingredientsHeader.textContent = "Ingredients:";
        recipeDiv.appendChild(ingredientsHeader);

        var ingredientsList = document.createElement("ul");
        recipe.ingredients.forEach(ingredient => {
            var ingredientItem = document.createElement("li");
            ingredientItem.textContent = ingredient;
            ingredientsList.appendChild(ingredientItem);
        });
        recipeDiv.appendChild(ingredientsList);

        var instructionsHeader = document.createElement("h3");
        instructionsHeader.textContent = "Cooking Instructions:";
        recipeDiv.appendChild(instructionsHeader);

        var instructionsList = document.createElement("ol");
        recipe.cooking_instructions.forEach(instruction => {
            var instructionItem = document.createElement("li");
            instructionItem.textContent = instruction;
            instructionsList.appendChild(instructionItem);
        });
        recipeDiv.appendChild(instructionsList);

        recommendationsContainer.appendChild(recipeDiv);
    });
}
