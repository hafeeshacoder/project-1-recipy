from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dictionary to store recipe data
recipes = {
	"chicken_biryani": {
		"name": "Chicken Biryani",
		"ingredients": ["2 cups Basmati rice🍚🍚", "1 pound Boneless, skinless chicken or lamb🍗", "1/2 cup Plain yogurt","2 teaspoons Garam masala powder","1 teaspoon Cumin powder","1 teaspoon Coriander powder",
        " 1/2 teaspoon Turmeric powder","1/2 teaspoon Red chili powder"," 1/2 teaspoon Salt🧂","1/4 teaspoon Black pepper🧂","2-3 Green cardamom pods"," 2 tablespoons Ghee or oil🛢","1 cup Chopped fresh cilantro","4 cups Wate🫗"],
		"steps": [" Prepare the rice", "Marinate the meat", "Make the biryani masala","Cook the meat","Assemble the biryani","Dum cooking","Serve🥘"]

	},
	"palak_paneer": {
		"name": "Parotta",
		"ingredients": ["2 cups all-purpose flour", "1 teaspoon salt", "1/4 teaspoon sugar🫙","1/2 teaspoon active dry yeast","1/4 cup ghee or oil🛢","1/2 cup lukewarm water🫗","1 egg, beaten (optional)"],
		"steps": ["Mix dry ingredients", "Add ghee or oil", "Combine and cook","Rest the dough","Divide the doug","Roll out each portion","Fold and layer","Roll out again","Cook on a tava"," Serve"]

	},
	"veg_pulao": {
		"name": "Fride Rice",
		"ingredients": ["2 cups Cooked rice🍚🍚", "1 tablespoon Vegetable oil", "1 small Onion, diced🧅"," 2 cloves Garlic, minced🧄"," 1 cup Mixed vegetables🥗 (e.g., peas, carrots, corn)"," 1 cup Cooked chicken🍗, shrimp, or tofu (optional)"," 2 teaspoons Soy sauce","1 teaspoon Oyster sauce 🫙(optional)","Salt and pepper, to taste🧂🧂","2 green Onions, chopped 🧅🧅(optional)"],
		"steps": ["Heat oil in a wok or skillet", "Add aromatics", "Add mixed vegetables"," Add cooked protein","Add cooked rice","Add seasoning","Taste and adjust","Transfer to a serving platter","Serve"]

	}
}

@app.route("/")
def index():
	return render_template("recipi.html")

@app.route("/select_recipe", methods=["POST"])
def select_recipe():
	recipe_name = request.form["recipe"]
	return redirect(url_for("display_recipe", recipe_name=recipe_name))

@app.route("/display_recipe/<recipe_name>")
def display_recipe(recipe_name):
	recipe_data = recipes[recipe_name]
	return render_template("recipi1.html", recipe_data=recipe_data)

if __name__=="__main__":
	app.run(debug=True)