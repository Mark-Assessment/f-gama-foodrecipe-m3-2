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