from flask import render_template, request, url_for, redirect
from foodreceipe import app, db
from foodreceipe.models import Category, Receipe, Ingredients


@app.route("/")
def home():
    return render_template("receipe.html")


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
    ingredients = ingredients.query.get_or_404(ingredients_id)
    db.session.delete(ingredients)
    db.session.commit()
    return redirect(url_for("ingredients"))


@app.route("/add_receipe", methods=["GET", "POST"])
def add_receipe():
    categories = list(Category.query.order_by(Category.category_name).all())
    ingredients = list(Ingredients.query.order_by(Ingredients.ingredient_name).all())
    if request.method == "POST":
        receipes = Receipe(
            receipe_name=request.form.get("receipe_name"),
            receipe_description=request.form.get("receipe_description"),
            prep_method=request.form.get("prep_method"),
            ingredients_id=request.form.get("ingredients_id"),
            category_id=request.form.get("category_id")
        )
        db.session.add(receipes)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add_receipe.html", categories=categories, ingredients=ingredients)