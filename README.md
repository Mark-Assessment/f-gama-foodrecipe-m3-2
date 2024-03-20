# Foodrecipe
## Code institute Milestone Project3

[Click here to launch a game](https://foodrecipe-798974a40ee6.herokuapp.com/)

Organize your Food Recipe (Website), and Categories help you organize and define your recipes. Course, Cuisine, Main Ingredient, can be customized to whatever you'd like! Add, edit, or remove any of the options in these categories and then add them to your recipes to organize your recipe.

![](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/static/Features/recipewebsite.png?raw=true)

# About Foodrecipe

A recipe is a set of instructions that describes how to prepare or make something, especially a dish of prepared food.

##  Foodrecipe goals

This food recipe app allows users to sift through tons of recipes, and check cooking intructions. It also lets users know the main ingredients, and the type of meal, which the user wants to make.

# User Experience (UX)
* ## User stories
  * ### First time visitors goal
    * As a first time visitor, I want to easily understand the main purpose of the app and learn more about the feature of the app 
    * As a first time visitor, I want to look for different recipes and then add the recipes along with ingredients and categories.
    * Look to edit a recipe, ingredients and categories
    * User can delete recipe, category and ingredient at any time
    * Guide users by providing detailed instructions for preparing various dishes       
    * Offering comprehensive information on ingredients.
    * Provide step-by-step cooking procedures

  * ### Frequent User Goals
    * As a frequent User, I want to see if the preparation time
    * As a Frequent User, I want to see calories
    * As a Frequent User, I want to see who added the recipe
    * As a Frequent User, I want to see the reviews
    

* ## Design
  * ### Colour Scheme
    
    I have chosen to use the blue and white as the main colour, alongside grey and black, as well as using the accent colours red and light green.   
    Red is used as a warning colour on buttons used for deletion. Green accent is used for the edit button to easily differentiate the buttons.
  
    * Card colour - #03a9f4
    * Delete button - #888e5f
    * Edit button - #F44336
    * Text colour - #fff


  * ### Typography

    * Default fonts is used throughtout the website. I haven't use google fonts

  * ### Imagery
    * On the Homepage, I have used a professionally presented food image to suit the purpose of the website, which is providing a good impression for the visitors.
  
* ## Wireframes
  * ### Home page Wireframe - [View](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/static/wireframes/Home.png)
  * ### New recipe Wireframe - [View](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/static/wireframes/Newrecipe.png)
  * ### Ingredients Wireframe - [View](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/static/wireframes/Ingredients.png)
  * ### Categories Wireframe - [View](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/static/wireframes/Categories.png)

# Database Schema

- I have represented the data within an entity relationship diagram.
![Entity Relationship Diagram](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/static/tablestructure/tablestructure.png?raw=true)
- I have structured a database using [PostgreSQL](https://www.postgresql.org/), a object-relational database to support the Foodrecipe app.  
Based on this information, I then created a database structure called foodrecipe db, within which I created 4 tables: category, ingredients, recipe and ingredient_index.
![Foodrecipe database](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/static/tablestructure/foodrecipedb.png?raw=true)
- The 'category' stores the specific fields of information about the categories to which the recipe belongs for e.g. Lunch, dinner, chicken, beef, etc.
![foodrecipe category](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/static/tablestructure/categorytable.png?raw=true)
- The 'ingredients' stores the specific fields of information about the ingredients which is used to create a recipe for example, chicken, flour, pepper etc. 
![Ingredients collection](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/static/tablestructure/ingredientstable.png?raw=true)  
- The 'recipe' stores the actual recipe with all the other information for e.g. how the recipe is prepared, what ingredients are used and which category it belongs to
![Recipe collection](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/static/tablestructure/recipetable.png?raw=true).  
- The 'ingredient_index' stores the relation between the recipe and the ingredients of all the recipes for e.g. Chicken recipe and the ingredients of the chicken recipe
![Ingredients index](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/static/tablestructure/ingredient_indextable.png?raw=true)

# Features

* Responsive on all device sizes

![Responsive Mockup](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/static/Features/recipewebsite.png?raw=true). 

* Interactive elements

## Navigation:

I created a menu to help enable the user to navigate the app. The menu is responsive and changes to a user-friendly side panel with dropdown functionality on mobile. Users have access via the menu to an additional category, ingredient pages featuring a dashboard to add, delete and edit.
### Home page desktop
![Home page desktop](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/static/Features/Homepage.png?raw=true)
### Home page mobile
![Home page mobile](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/static/Features/iPad10th.png?raw=true)
### Category desktop
![Category desktop](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/static/Features/Categorieslist.png?raw=true)
### Category mobile
![Category mobile](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/static/Features/categoriesmobile.png?raw=true)
### Ingredient desktop
![Ingredient desktop](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/static/Features/ingredientlist.png?raw=true)
### Ingredient mobile
![Ingredient mobile](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/static/Features/ingredientsmobile.png?raw=true)

# UX features:
## Modal
- I have added a modal on delete functionality to make user aware of delete action. 

# CRUD 
I have incorporated features to enable Create, Read, Update & Delete functionallity within the Foodrecipe App 
## Add a recipe record
- I created a page called add_recipe.html and added the function in the routes.py file called add_recipe which uses the "GET" and "POST". The GET method is to used to request data , The POST method is used to send the data to the server. I then created and styled input text fields to enable users to input text and also an input field for users to add the recipe details. I used a dropdown list for category and ingredient selection. Specific minimum and maximum entry lengths were applied to each text field.
## Add recipe user interface:
![add_recipe user interface](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/static/Features/Nwerecipe.png?raw=true)
## Input fields features:
![category drop-down list](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/static/crudscreenshots/Categoryfield.png?raw=true)
![ingredient drop-down list](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/static/crudscreenshots/ingredientfield.png?raw=true)
## add_recipe function:
![add_recipe function](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/static/crudscreenshots/Addrecipefunction.png?raw=true)
## add_category function:
I created a categories page to manage categories with blue button to add categories at the top of the page under the title. On click of "Add category" button it redirects to "Add category" page with the help of an add_category.html template. I then created a function to add categories.  
![add_category function](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/static/crudscreenshots/Addcategoryfunction.png?raw=true)
## add_ingredients function:
I created a ingredients page to manage ingredients with blue button to add ingredients at the top of the page under the title. On click of "Add ingredient" button it redirects to "Add ingredient" page with the help of an add_ingredients.html template. I then created a function to add ingredients.  
![add_ingredients function](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/static/crudscreenshots/AddIngredientfunction.png?raw=true)
## Update a recipe:
I created edit_recipe.html to edit a recipe record. I fetch a recipe details based on the recipe id from the database. Once found, then the recipe record is updated with edit recipe button. After that's been updated in the database, I redirect to the home page where the list of recipes are displayed
![Updating a recipe record](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/static/crudscreenshots/Editrecipefunction.png?raw=true)
## Update categories
I created an edit_category.html template and interface and a function to edit categories. The functionality was created in the same way as the create recipe record.
![Updating a cateory record](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/static/crudscreenshots/Editcategoryfunction.png?raw=true)
## Update ingredients
I created an edit_ingredients.html template and interface and a function to edit ingredients. The functionality was created in the same way as the create recipe record.
![Updating a ingredient record](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/static/crudscreenshots/EditIngredientfunction.png?raw=true)
## Delete a recipe:
The user can delete a recipe by clicking the red delete button at the foot of the recipe record. To do this I created a function as follows: The @app.route decorator is '/delete_recipe', which takes the 'recipe_id' as a variable. I then selected the specific recipe by the ObjectId that matched the 'recipe_id' variable. As soon as the record is removed I redirect the user to home page where the list of recipes are shown.  
![delete_recipe function](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/static/crudscreenshots/deleterecipefunction.png?raw=true). 
## Delete a category:
The user can delete a record by clicking a delete button for the specific category within the categoires dashboard. To do this, I created a function to delete categories. The functionality was created in the same way as the delete recipe record
![delete_category function](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/static/crudscreenshots/deletecategoryfunction.png?raw=true)
## Delete a ingredient:
The user can delete a record by clicking a delete button for the specific ingredient within the ingredients dashboard. To do this, I created a function to delete ingredients. The functionality was created in the same way as the delete recipe record
![delete_ingredient function](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/static/crudscreenshots/DeleteIngredientfunction.png?raw=true)

# Technologies Used

## Languages Used

  * [HTML5](https://en.wikipedia.org/wiki/HTML5)
  * [CSS3](https://en.wikipedia.org/wiki/CSS)
  * [JS](https://en.wikipedia.org/wiki/JavaScript)
  * [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

  ##  Frameworks, Libraries & Programs Used
  1. [Materialize 1.0.0:](https://materializecss.com/)
     * Materialize is a modern responsive CSS framework based on Material Design by Google. Materialize was used to assist with the responsiveness and styling of the website; especially useful in this project  are the features for creating forms.
  2. [Font Awesome:](https://fontawesome.com/)
     *  Font Awesome is used to add help icon
  3. [Heroku:](https://www.heroku.com/)
     * The project was deployed to Heroku. Heroku is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.
  4. [PostgreSQL:](https://www.postgresql.org/)
     * PostgreSQL was used to store the data required for the project. It is a object-relational database used for data storage.
  5. [Git:](https://git-scm.com/)
     * Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
  6. [GitHub:](https://github.com/)
     * GitHub is used to store the projects code after being pushed from Git.
  7. [Balsamiq:](https://balsamiq.com/)
     * Balsamiq was used to create the [wireframes]() during the design process.
  8. [Am I reponsive:](https://ui.dev/amiresponsive)
     * Am I reponsive was used to create a mockup to add in a README.md file
 
# Deployment
GitHub Pages
The project was deployed to GitHub Pages using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/fatimagama20/TutorMilestoneProject1)
2. At the top of the Repository (not top of page), locate the "Settings" Button on the menu.
   * Alternatively Click Here for a GIF demonstrating the process starting from Step 2.
3. Scroll down the Settings page until you locate the "GitHub Pages" Section.
4. Under "Source", click the dropdown called "None" and select "Master Branch".
5. The page will automatically refresh.
6. Scroll back down through the page to locate the now published site link in the "GitHub Pages" section.
# Forking the GitHub Repository
By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/fatimagama20/TutorMilestoneProject1)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.
# Making a Local Clone
1. Log in to GitHub and locate the [GitHub Repository](https://github.com/fatimagama20/TutorMilestoneProject1)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type git clone, and then paste the URL you copied in Step 3.

   $ git clone https://github.com/fatimagama20/TutorMilestoneProject1
7. Press Enter. Your local clone will be created.

   $ git clone https://github.com/fatimagama20/TutorMilestoneProject1

> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
Click Here to retrieve pictures for some of the buttons and more detailed explanations of the above process.

# Deployment 
## Setting up a GitHub caccount
- I set up a [GitHub account](https://github.com/)
- Used the Chrome browser
- Created the Project GitHub repository
- Clicked the green GitPod button in the top right hand cornner of the repository to create a new [workspace](https://gitpod.io/workspaces) to enable me to work locally'
## Set up the database with PostgreSQL
I Create an account with ElephantSQL 
- Navigate to ElephantSQL.com and click “Log in”:
- Select “Sign in with GitHub”.
- Authorise ElephantSQL with your selected GitHub account.
- In the Create new team form:
    - Add a team name (your own name is fine)
    - Read and agree to the Terms of Service
    - Select Yes for GDPR
    - Provide your email address
    - Click “Create Team”
- Create a database.
    - Click “Create New Instance”
    - Set up your plan
       - Give your plan a Name (this is commonly the name of the project)
       - Select the Tiny Turtle (Free) plan
       - You can leave the Tags field blank
    - Select “Select Region”
    - Select a data center near you
    - Then click “Review”
    - Check your details are correct and then click “Create instance”
    - Return to the ElephantSQL dashboard and click on the database instance name for this project
    - In the URL section, clicking the copy icon will copy the database URL to your clipboard
    - Leave this tab open, we will come back here later
- Preparing your code for Deployment
    Now you have a database, we need to make some modifications to the code in your IDE.In your IDE workspace
    Before we can build our application on Heroku, we need to create a few files that Heroku will need to run our application:
    - A requirements.txt file which contains a list of the Python dependencies that our project needs in order to run successfully.
    - A Procfile which contains the start command to run the project.
    - Generate the requirements.txt file with the following command in the terminal. After you run this command a new file called requirements.txt should appear in your root directory
      - pip freeze --local > requirements.txt
   - Heroku requires a Procfile containing a command to run your program. Inside the root directory of your project create the new file. It must be called Procfile with a capital P, otherwise Heroku won’t recognise it
   - Inside the file, add the following command
      - web: python run.py
- whitelisted IP address and selected allow Access From Anywhere.
- Once the cluster was fully provisioned, I created a new database called houseplantr_db to store the data that will be used with the app.
### Set up collections and add category document:
- I created three collections within the database: Categories, Houseplants and Users.
- In the Categories collection, I inserted a document and created a key value pair: category_name:Flowering. (At this stage only one houseplant category was needed just to get the app set up. The rest of the categories were added later).
### Add houseplant document to a collection:
- In the houseplants collection I set up a document. The first key was category_name:“Flowering” as before. Then add additional fields were added: horticultural name, common name, description, date, created_by, image_url, and houseplant_care. 
- The relevant houseplant data was added as key value pairs as in the screenshot below. Again, only one houseplant document was needed just to get the app set up, and new documents would be created within the app.  
![Key Value Pairs within a document](screenshots/example-key-value-pairs.png)

### Create the Flask Application
To create the Flask application I did the following:
- Created a new repository in [GitHub](https://github.com/RachelFurlong-dev/milestone-project3-v1)
- in the Terminal typed; 'pip3 install Flask' so that Flask functionality was ready to be imported.
- created the app.py file which would run the application.
- created an env.py in which to store sensitive data.
- created a gitignore file which was set up to ignore env.py as well as the the '__pycache__/' directory.so that data that must be kept secure such as secret keys would not be saved to GitHub.
- imported os to set up default environment variables in the env.py file, as in the screenshot below:  
![Environment Variables](screenshots/environment-variables.png)
- in app.py import Flask 
- imported the env package so Heroku would be able to find the environment variables as they would not be pushed to GitHub.
- created an instance of Flask, stored in a variable called 'app'.
- told the app how and where to run the application as in the screenshot below:  
![Run application](screenshots/app-run.png)
- the final parameter was set to debug=True, during development, so I could see any actual errors that may appear, instead of a generic server warning. I changed this back to debug=False prior to final deployment.
- set up a test function to check the app was working correctly in advance of connecting the app to MongoDB.

### Deploy application to Heroku:
I Create an account with ElephantSQL 
- Navigate to ElephantSQL.com and click “Log in”:
- Select “Sign in with GitHub”.
- Authorise ElephantSQL with your selected GitHub account.
- In the Create new team form:
    - Add a team name (your own name is fine)
    - Read and agree to the Terms of Service
    - Select Yes for GDPR
    - Provide your email address
    - Click “Create Team”
- Create a database.
    - Click “Create New Instance”
    - Set up your plan
       - Give your plan a Name (this is commonly the name of the project)
       - Select the Tiny Turtle (Free) plan
       - You can leave the Tags field blank
    - Select “Select Region”
    - Select a data center near you
    - Then click “Review”
    - Check your details are correct and then click “Create instance”
    - Return to the ElephantSQL dashboard and click on the database instance name for this project
    - In the URL section, clicking the copy icon will copy the database URL to your clipboard
    - Leave this tab open, we will come back here later
- Preparing your code for Deployment
    Now you have a database, we need to make some modifications to the code in your IDE.In your IDE workspace
    Before we can build our application on Heroku, we need to create a few files that Heroku will need to run our application:
    - A requirements.txt file which contains a list of the Python dependencies that our project needs in order to run successfully.
    - A Procfile which contains the start command to run the project.
    - Generate the requirements.txt file with the following command in the terminal. After you run this command a new file called requirements.txt should appear in your root directory
      - pip freeze --local > requirements.txt
   - Heroku requires a Procfile containing a command to run your program. Inside the root directory of your project create the new file. It must be called Procfile with a capital P, otherwise Heroku won’t recognise it
   - Inside the file, add the following command
      - web: python run.py
   - Open your __init__.py file
   - Add an if statement before the line setting the SLQALCHEMY_DATABASE_URI and, in the else, set the value to reference a new variable, DATABASE_URL. [database_url](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/static/Features/database_uri.png?raw=true)
   - To ensure that SQLAlchemy can also read our external database, its URL needs to start with “postgresql://”, but we should not change this in the environment variable. Instead, we’ll make an addition to our else statement from the previous step to adjust our DATABASE_URL in case it starts with postgres://:[postgresql](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/static/Features/postgresql.png?raw=true)
   - Save all your files and then add, commit and push your changes to GitHub
- Connecting the database to the hosting platform
   - Log into Heroku.com and click “New” and then “Create a new app”
   - Choose a unique name for your app, select the region closest to you and click “Create app”
   - Go to the Settings tab of your new app
   - Click Reveal Config Vars
   - Return to your ElephantSQL tab and copy your database URL
   - Back on Heroku, add a Config Var called DATABASE_URL and paste your ElephantSQL database URL in as the value. Make sure you click “Add”
   - Add each of your other environment variables except DEVELOPMENT and DB_URL from the env.py file as a Config Var
- Deploying the app
   - Navigate to the “Deploy” tab of your app
   - In the Deployment method section, select “Connect to GitHub”
   - Search for your repo and click Connect
   - Optional: You can click Enable Automatic Deploys in case you make any further changes to the project. This will trigger any time code is pushed to your GitHub repository
   - As we already have all our changes pushed to GitHub, we will use the Manual deploy section and click Deploy Branch. This will start the build process. When finished, it should look something like this
   - Now, we have our project in place, and we have an empty database ready for use. As you may remember from our local development, we still need to add our tables to our database. To do this, we can click the “More” button and select “Run console”
   - Type python3 into the console and click Run
   - This opens the Python terminal, in the same way as it would if we typed python3 into the terminal within our IDE. Let’s now create the tables with the commands we used before
     - from taskmanager import db
     - db.create_all()
   - Exit the Python terminal, by typing exit() and hitting enter, and close the console. Our Heroku database should now have the tables and columns created from our models.py file.
   - The app should be up and running now, so click the “Open app” button
Congratulations! You have successfully deployed your app to Heroku! [live site](https://foodrecipe-798974a40ee6.herokuapp.com/).


### Connect Flask to MongoDB:
To connect Flask to [MongoDB](https://www.mongodb.com/) I did the following:
- set up a working connection between my application and the database and installed a third party library called flask-pymongo.
- installed 'dnspython' in order to use the Mongo SRV connection string.
- updated the requirements.txt file to allow Heroku to detect the new requirements for running the app.
- added the additional imports at the top of app.py to reflect the new installations.("from flask_pymongo import PyMongo").
- added "from bson.objectid import ObjectId"(because MongoDB stores its data in a JSON-like format called BSON).
- additional configuration was added in app.py to connect to MongoDb as in the screenshot below:  
![MongoDB congiuration app.py](screenshots/mdb-configuration-req.png)
- from MongoDB cluster copied the MONGO_URI connection string, updating database name and password to replace the angle brackets placeholder content.
- copied the completed string to env.py file to complete the MONGO_URI environment variable.
- copied the completed string to the MONGO_URI variable in Heroku Config Vars.
- tested the app to see if it was connecting with the database successfully.  

### Display data from MongoDB on template page:
To test data from MongoDB would display on a template page within the app I did the following:
- set up an instance of PyMongo, and added the app into that using a constructor method "mongo = PyMongo(app)".
- tested to check the app was connecting with MongoDB by creating a function with a decorator that includes a route to that app. 
- created a template houseplants.html and generated data from the houseplants collection to the template. 
- ran the app to check the correct data was visible on the houseplants.html file which indicated that the app had connected with MongoDB successfully.
- With MongoDB and Heroku set up correctly with the app, I was able to set up the templates, design the interface, create, edit and delete records to the app. 
- Once testing was complete, I changed debug=True (the setting required to be able to detect errors) to debug=False prior to final deployment.

## How to run this project locally 
### Cloning project into GitPod
1. Set up a [GitHub account](https://github.com/)
2. Use the Chrome browser.
3. Install browser extensions for Chrome.
4. After installation restart the browser.
5. Log into GitPod with your gitpod account
6. Navigate to the Project GitHub [repository](https://github.com/RachelFurlong-dev/milestone-project3-v1).
7. Click the green GitPod button in the top right hand cornner of the repository to create a new [workspace](https://gitpod.io/workspaces) to enable you to work locally'
8. More information about cloning is available [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) 
## Set up the database on [MongoDB Atlas](https://www.mongodb.com/)
Do the following:
1. Create a cluster on which a database can run.
2. Add a new database user with username and password.
3. Set privileges as Read and Write to the database.
4. Whitelist IP address and select allow Access From Anywhere.
5. Once the cluster is fully provisioned, create a new database called houseplantr_db to store the data that will be used with the app.
### Set up collections:
1. Create three collections within the database: Categories, Houseplants and Users.
2. In the Categories collection, Insert a Document and create a key value pair: category_name:Flowering. At this stage only one houseplant category is needed just to get the app set up. The rest of the categories will be added later.
### Add document:
1. In the houseplants collection set up a document: The first key is category_name:“Flowering” as before. 
2. Add additional fields: horticultural name, common name, description, date, created_by, image_url, and houseplant_care. The relevant houseplant data should be added as key value pairs as in the screenshot below. Again, only one houseplant document is needed at this stage to get the app set up, and new documents will be created within the app.  
![Key Value Pairs within a document](screenshots/example-key-value-pairs.png)
## Create the Flask Application
To create the Flask application:
1. in the Terminal type; 'pip3 install Flask' so that Flask functionality is ready to be imported.
2. create an env.py in which to store sensitive data.
3. create a gitignore file to ignore env.py as well as the the '__pycache__/' directory - data that must be kept secure such as secret keys must not be saved to GitHub.
4. import os to set up default environment variables in the env.py file, as in the screenshot below:  
![Environment Variables](screenshots/environment-variables.png)
5. update the env package in app.py so Heroku will be able to find the corrrect environment variables as they are not be pushed to GitHub.
6. set the final parameter to debug=True during development, in order to detect errors that may appear, instead of a generic server warning. Change this back to debug=False prior to final deployment.
7. set up a test function to check the app is working correctly in advance of connecting the app to MongoDB.
## Deploy application to Heroku:
To deploy the application to [Heroku](https://www.heroku.com/):
1. create a requirements.txt file where the dependencies required to run the app will be stored.
2. create a Procfile where Heroku can get the information needed to run the app.
3. create a new app in Heroku and give it a name.
4. select location nearest to you.
5. connect to GitHub within the app using the GitHub connect option.
6. select Settings > Reveal Config Vars, and type in the variables from the env.py file into the fields in MongoDB – leave the MONGO_URI field contents empty for now.
7. in GitHub push the two new files (requirements.txt and Procfile) to the repository.
8. select the Deploy Tab in Heroku, then Enable Automatic Deploys and Deploy Branch. This enables Heroku to receive the code from GitHub and build the app using the required packages.
## Connect Flask to MongoDB:
To connect Flask to MongoDB complete the following:
1. set up a working connection between your application and your database. 
2. install a third party library called flask-pymongo.
3. install 'dnspython' in order to use the Mongo SRV connection string.
4. update the requirements.txt file to allow Heroku to detect the new requirements for running the app.
5. add the additional imports at the top of app.py to reflect the new installations.("from flask_pymongo import PyMongo").
6. add "from bson.objectid import ObjectId"(MongoDB stores its data in a JSON-like format called BSON).
7. update configuration in app.py to connect to MongoDB. 
8. in your MongoDB cluster copy the MONGO_URI connection string, updating database name and password with your chosen settings to replace the angle brackets placeholder content.
9. copy the completed string to env.py file to complete the MONGO_URI environment variable.
10. copy the completed string to the MONGO_URI variable in Heroku Config Vars.
11. To test the app to see if it is connecting with the database successfully, run the app to check the correct data from the houseplants collection is visible on the houseplants.html file. This indicates that the app has connected with MongoDB successfully.
12. Deployment of the app is complete. Add more records to the app to create the layout of the home page. 

# Accessibility
Accessible features include:
- Adding alt tags via the jinga templating language to user uploaded images.
- For linked icons, I used aria labels indicating the link destination.
- Created responsive layouts which I tested across multiple screen sizes. 
- Validated code - see [Testing section](/TESTING.md)

# Credits
## Code
* [Bootstrap 5.0:](https://getbootstrap.com/docs/5.0/getting-started/introduction/) Bootstrap was used significantly throughout the project to make it responsive. I used the Grid system as well as inputting a fixed-top navbar, a progress bar and contact form.

* [Stack Overflow](https://stackoverflow.com/) was used to help me style the navbar text colour and was used in HTML to close the navbar when a link is clicked on mobile.

* [W3Schools](https://www.w3schools.com/) was used to provide a smooth scroll to the website and to style the contact form and the submit button.

* [Courses.Code Institute](https://learn.codeinstitute.net/ci_program/level5diplomainwebappdevelopment) was used to style the progress bars and I used the demonstrated jQuery for the contact form.

## Content
* [Google :](https://www.google.co.uk/) Some content was searched from google
* Some content by the developer.

## Media
* [Google:](https://www.google.co.uk/) Some Images were downloaded from google.
* [Unsplash:](https://unsplash.com/) Some image are taken from Unsplash

## Acknowledgements
* My Mentor for continuous helpful feedback.
* Tutor support at Code Institute for their support.








 