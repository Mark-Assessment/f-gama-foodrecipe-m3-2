from flask import render_template, request, url_for, redirect
from foodrecipe import app, db
from foodrecipe.models import Category, Recipe, Ingredients, Ingredient_index


@app.route("/")
def home():
    recipes = list(Recipe.query.order_by(Recipe.id).all())
    return render_template("recipe.html", recipes=recipes)


@app.route("/categories")
def categories():
    categories = list(Category.query.order_by(Category.category_name).all())
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("add_category.html")


@app.route("/ingredients")
def ingredients():
    ingredients = list(Ingredients.query.order_by(Ingredients.ingredient_name).all())
    return render_template("ingredients.html", ingredients=ingredients)


@app.route("/add_ingredients", methods=["GET", "POST"])
def add_ingredients():
    if request.method == "POST":
        ingredients = Ingredients(ingredient_name=request.form.get("ingredient_name"))
        db.session.add(ingredients)
        db.session.commit()
        return redirect(url_for("ingredients"))
    return render_template("add_ingredients.html")


@app.route("/edit_category/<int:category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    category = Category.query.get_or_404(category_id)
    if request.method == "POST":
        category.category_name = request.form.get("category_name")
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("edit_category.html", category=category)


@app.route("/edit_ingredients/<int:ingredients_id>", methods=["GET", "POST"])
def edit_ingredients(ingredients_id):
    ingredients = Ingredients.query.get_or_404(ingredients_id)
    if request.method == "POST":
        ingredients.ingredient_name = request.form.get("ingredient_name")
        db.session.commit()
        return redirect(url_for("ingredients"))
    return render_template("edit_ingredients.html", ingredients=ingredients)


@app.route("/delete_category/<int:category_id>")
def delete_category(category_id):
    category = Category.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for("categories"))


@app.route("/delete_ingredients/<int:ingredients_id>")
def delete_ingredients(ingredients_id):
    ingredients = Ingredients.query.get_or_404(ingredients_id)
    db.session.delete(ingredients)
    db.session.commit()
    return redirect(url_for("ingredients"))


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    categories = list(Category.query.order_by(Category.category_name).all())
    ingredients = list(Ingredients.query.order_by(Ingredients.ingredient_name).all())
    if request.method == "POST":
        recipes = Recipe(
            recipe_name=request.form.get("recipe_name"),
            recipe_description=request.form.get("recipe_description"),
            prep_method=request.form.get("prep_method"),
            category_id=request.form.get("category_id")
        )
        db.session.add(recipes)
        db.session.commit()
        ingredients_id=request.form.getlist("ingredients_id")
        #print('The list ',request.form.getlist("ingredients_id"))
        for ingredient_id in ingredients_id:
            index_entry = Ingredient_index(
            recipe_id=recipes.id,
            ingredient_id=ingredient_id)
            db.session.add(index_entry)
            db.session.commit()
        return redirect(url_for("home"))
    return render_template("add_recipe.html", categories=categories, ingredients=ingredients)


@app.route("/edit_recipe/<int:recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    categories = list(Category.query.order_by(Category.category_name).all())
    allingredients = list(Ingredients.query.order_by(Ingredients.ingredient_name).all())
    recipeingredients = Ingredient_index.query.with_entities(Ingredient_index.ingredient_id).all()
    print('ids',Ingredient_index.query.with_entities(Ingredient_index.ingredient_id).all())
    if request.method == "POST":
        recipe.recipe_name = request.form.get("recipe_name"),
        recipe.recipe_description=request.form.get("recipe_description"),
        recipe.prep_method=request.form.get("prep_method"),
        recipe.category_id=request.form.get("category_id")
        db.session.commit()
        ingredients_id=request.form.getlist("ingredients_id")
        for ingredient_id in ingredients_id:
            index_entry = Ingredient_index(
            recipe_id=recipe.id,
            ingredient_id=ingredient_id)
            db.session.add(index_entry)
            db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit_recipe.html", recipe=recipe, categories=categories, allingredients=allingredients, recipeingredients=recipeingredients)


@app.route("/delete_recipe/<int:recipe_id>")
def delete_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    db.session.delete(recipe)
    db.session.commit()
    return redirect(url_for("home"))


@app.route('/get_ingredients/<int:recipe_id>')
def get_ingredients(recipe_id):
    try:
        # Assuming you have a Recipe model
        recipe = Recipe.query.get(recipe_id)
        if not recipe:
            return "Recipe not found."

        # Split the ingredients_ids (assuming it's a comma-separated string)
        ingredient_ids = recipe.ingredients_ids.split(',')

        # Query Ingredients based on ingredient IDs
        ingredients = Ingredients.query.filter(Ingredients.id.in_(ingredient_ids)).all()

        # Extract ingredient names
        ingredient_names = [ingredient.ingredient_name for ingredient in ingredients]

        return ', '.join(ingredient_names)  # Comma-separated list of ingredient names
    except Exception as e:
        return str(e)