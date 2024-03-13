# Foodrecipe
## Code institute Milestone Project3

[Click here to launch a game](https://fatimagama20.github.io/Mathgameproject2/)

Organize your Food Recipe (Website), and Categories help you organize and define your recipes. Course, Cuisine, Main Ingredient, can be customized to whatever you'd like! Add, edit, or remove any of the options in these categories and then add them to your recipes to organize your recipe.

![](?raw=true)

# About Foodrecipe

A recipe is a set of instructions that describes how to prepare or make something, especially a dish of prepared food.

##  Foodrecipe goals

This food recipe app allows users to sift through tons of recipes, and check cooking intructions. It also lets users know the main ingredients, and the type of meal, which the user wants to make.

# User Experience (UX)
* ## User stories
  * ### First time visitors goal
    * As a first time visitor, I want to easily understand the main purpose of the game and learn more about the feature of the game 
    * As a first time visitor, I want to look for help page to understand how to play a game
    * Everytime a correct answer is clicked score is incremented by 1
    * User can reset a game at any point and a timer is be reset to zero
    * User can play the game until 30 seconds
    * As a parent, can insist a child to play the game and improve the multiplication skills.
    * user can see the time remaining until the game is over

  * ### Frequent User Goals
    * As a frequent User, I want to see if more questions are added
    * As a Frequent User, I want to see if the developer can be contacted

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
  * ### Home page Wireframe - [View](https://github.com/fatimagama20/TutorMilestoneProject1/blob/main/assets/image/hompage.jpg)
  * ### New recipe Wireframe - [View](https://github.com/fatimagama20/TutorMilestoneProject1/blob/main/assets/image/aboutpage.jpg)
  * ### Ingredients Wireframe - [View](https://github.com/fatimagama20/TutorMilestoneProject1/blob/main/assets/image/contactform.jpg)
  * ### Categories Wireframe - [View](https://github.com/fatimagama20/TutorMilestoneProject1/blob/main/assets/image/contactform.jpg)

# Database Schema

- I have represented the data within an entity relationship diagram.
- ![Entity Relationship Diagram](screenshots/erd_final.png)
- I have structured a database using [PostgreSQL](https://www.postgresql.org/), a object-relational database to support the Foodrecipe app.  
Based on this information, I then created a database structure called foodrecipe db, within which I created 4 tables: category, ingredients, recipe and ingredient_index.
- ![Houseplantr Mongo DB database](screenshots/dbhouseplantr.png)
The 'category' stores the specific fields of information about the categories to which the recipe belongs for e.g. Lunch, dinner, chicken, beef, etc.
- ![foodrecipe category](screenshots/dbhouseplant-records.png)
The 'ingredients' stores the specific fields of information about the ingredients which is used to create a recipe for example, chicken, flour, pepper etc.   
The 'recipe' stores the actual recipe with all the other information for e.g. how the recipe is prepared, what ingredients are used and which category it belongs to
- ![Categories collection](screenshots/dbcategories.png).  
The 'ingredient_index' stores the relation between the recipe and the ingredients of all the recipes for e.g. Chicken recipe and the ingredients of the chicken recipe
- ![Users collection](screenshots/dbregistered-users.png)

# Features

* Responsive on all device sizes

![Responsive Mockup](screenshots/mockups.png). 

* Interactive elements

## Navigation:

I created a menu to help enable the user to navigate the app. The menu is responsive and changes to a user-friendly side panel with dropdown functionality on mobile. Users have access via the menu to an additional category, ingredient pages featuring a dashboard to add, delete and edit.
### Home page desktop
![Home page desktop](screenshots/nav-logged-out-view-mobile.png)
### Home page mobile
![Home page mobile](screenshots/nav-logged-out-view-desktop.png)
### Category desktop
![Category desktop](screenshots/nav-logged-in-user-mobile-view.png)
### Category mobile
![Category mobile](screenshots/nav-logged-in-user-desktop-view.png)
### Ingredient desktop
![Ingredient desktop](screenshots/nav-logged-in-admin-mobile-view.png)
### Ingredient mobile
![Ingredient mobile](screenshots/nav-logged-in-admin-desktop-view.png)

# UX features:
## Modal
- I have added a modal on delete functionality to make user aware of delete action. 

# CRUD 
I have incorporated features to enable Create, Read, Update & Delete functionallity within the Foodrecipe App 
## Add a recipe record
- I created a page called add_recipe.html and added the function in the routes.py file called add_recipe which uses the "GET" and "POST". The GET method is to used to request data , The POST method is used to send the data to the server. I then created and styled input text fields to enable users to input text and also an input field for users to add the recipe details. I used a dropdown list for category and ingredient selection. Specific minimum and maximum entry lengths were applied to each text field.
## Add recipe user interface:
![add_recipe user interface](screenshots/add-houseplant_layout.png)
## Input fields features:
![category drop-down list](screenshots/drop-down-list.png)
![ingredient drop-down list](screenshots/calendar.png)
## add_recipe function:
![add_recipe function](screenshots/add-houseplant-function.png)
## add_category function:
I created a categories page to manage categories with blue button to add categories at the top of the page under the title. On click of "Add category" button it redirects to "Add category" page with the help of an add_category.html template. I then created a function to add categories.  
![add_category function](screenshots/admin-only.png)
## add_ingredients function:
I created a ingredients page to manage ingredients with blue button to add ingredients at the top of the page under the title. On click of "Add ingredient" button it redirects to "Add ingredient" page with the help of an add_ingredients.html template. I then created a function to add ingredients.  
![add_ingredients function](screenshots/admin-only.png)
## Update a recipe:
I created edit_recipe.html to edit a recipe record. I fetch a recipe details based on the recipe id from the database. Once found, then the recipe record is updated with edit recipe button. After that's been updated in the database, I redirect to the home page where the list of recipes are displayed
![Updating a recipe record](screenshots/edit_houseplant-function.png)
## Update categories
I created an edit_category.html template and interface and a function to edit categories. The functionality was created in the same way as the create recipe record.  
## Delete a record:
The user can delete a houseplant by clicking the red delete button at the foot of the houseplant record. To do this I created a function as follows: The @app.route decorator is '/delete_houseplant', which takes the 'houseplant_id' as a variable. I then selected the specific houseplant by the ObjectId that matched the 'houseplant_id' variable. As soon as the record is removed I provide the user with a flash() message "Houseplant successfully deleted".  
![delete_houseplant function](screenshots/delete_houseplant-function.png). 
[Delete houseplant record button]()
## Delete a category:
The user cand delete a record by clicking a delete button for the specific category within the categoires dashboard. To do this, I created a function to delete categories. The functionality was created in the same way as the delete houseplant record, except this was limited to admin use only by using an if statement within the function.  
![delete_category function](screenshots/delete_category-function.png)
# User authentication
- I used Flask together with Werkzeug for security features, specifically "generate_password_hash" and "check_password_hash" for user password security. For additional security, Werkzeug's security features then salted the string with random data to make a password which would be hard to crack. I created a Login template and Registration template each containing a form with relevant input fields and button built using the responsive CSS framework Materialize. I added a link on each page template incase new users were on the Login page or existing users on the Registration page, to enable user to go to the page they required quickly. 
![Login Page](screenshots/loginscreenshot.png) 
![Registraion page](screenshots/regscreenshot.png)

# Technologies Used

## Languages Used

  * [HTML5](https://en.wikipedia.org/wiki/HTML5)
  * [CSS3](https://en.wikipedia.org/wiki/CSS)

  ##  Frameworks, Libraries & Programs Used
  1. [Bootstrap5:](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
     * Bootstrap was used to assist with the responsiveness and styling of the website.
  2. [Font Awesome:](https://fontawesome.com/)
     *  Font Awesome is used to add help icon
  3. [Hover:css:](https://ianlunn.github.io/Hover/)
     * Hover.css was used on the Social Media icons in the footer to add the float transition while being hovered over.
  4. [jQuery:](https://jquery.com/)
     * jQuery came with Bootstrap to make the navbar responsive but was also used for the smooth scroll function in JavaScript.
  5. [Git:](https://git-scm.com/)
     * Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
  6. [GitHub:](https://github.com/)
     * GitHub is used to store the projects code after being pushed from Git.
  7. [Balsamiq:](https://balsamiq.com/)
     * Balsamiq was used to create the [wireframes]() during the design process.
  8. [Am I reponsive:](https://ui.dev/amiresponsive)
     * Am I reponsive was used to create a mockup to add in a README.md file
# Testing
The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.
  * [W3C Markup Validator]() - [Results](https://github.com/fatimagama20/TutorMilestoneProject1/blob/main/assets/image/w3cmarkupvalidatorresult.jpg)
  * [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - [Results](https://github.com/fatimagama20/TutorMilestoneProject1/blob/main/assets/image/cssresult.jpg)
# Testing User Stories from User Experience (UX) Section
 * First Time Visitor Goals

    1. As a First Time Visitor, I want to easily understand the main purpose of the food recipe app and learn more about the recipes.

       * Guide users by providing detailed instructions for preparing various dishes
       
       * Offering comprehensive information on ingredients.

       *  Provide step-by-step cooking procedures

    2. As a First Time Visitor, I want to be able to easily be able to add, edit, and delete ingredients.

        * At the top of each page there is a clean navigation bar, each link describes what the page they will end up at clearly.

    3. As a First Time Visitor, I want to able to add,edit, and delete categories


 *  Frequent User Goals

    1. As a Frequent User, to be able to check to see if there are any newly added reviews about the recipe.

    2. As a Frequent User, to be able to search a recipe.

       * The user would already be comfortable with the website layout and can easily search the recipes.

   2. As a Frequent User, to be able to add recipe by different people.

# Further Testing
* The Website was tested on Google Chrome, Internet Explorer, Microsoft Edge and Safari browsers.
* The website was viewed on a variety of devices such as Desktop, Laptop, iPhone7, iPhone 8 & iPhoneX.
* A large amount of testing was done to ensure that all pages were linking correctly.
* Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.
# Known Bugs
* Hover effects don't work on the navigation bar
  * I tried fixing hover effects on a nav bar but somehow Bootstrap is overriding the CSS. Since there is not much impact on the UX and there are clear redirection provided I left it unfixed
 
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








 