from foodrecipe import db


class Category(db.Model):
    # schema for the Category model
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(50), unique=True, nullable=False)
    recipes = db.relationship("Recipe", backref="category", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.category_name


class Ingredients(db.Model):
    # schema for the Ingredients model
    id = db.Column(db.Integer, primary_key=True)
    ingredient_name = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.ingredient_name



class Recipe(db.Model):
    # schema for the Recipe model
    id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(50), unique=True, nullable=False)
    recipe_description = db.Column(db.Text, nullable=False)
    prep_method = db.Column(db.Text, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.recipe_name

class Ingredient_index(db.Model):
    # schema for the Ingredient_index model
    id = db.Column(db.Integer, primary_key=True)
    recipe_id =  db.Column(db.Integer, db.ForeignKey("recipe.id", ondelete="CASCADE"), nullable=False)
    ingredient_id = db.Column(db.Text, db.ForeignKey("ingredients.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.id