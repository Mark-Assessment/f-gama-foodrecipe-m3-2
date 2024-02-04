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
        print("success")
    return render_template("add_category.html")


@app.route("/ingredients")
def ingredients():
    return render_template("ingredients.html")


@app.route("/add_ingredients", methods=["GET", "POST"])
def add_ingredients():
   return render_template("add_ingredients.html")