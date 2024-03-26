

## Tested Add Category form validation and feature
[Add category]()
- Tested all the fields are required fields and cannot be left blank
- Tested that minimum and maximum length
- Tested that on adding category it's redirected to categories form and at the same time the added category is listed.
![Add category form](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/screenshots/newcategory.png?raw=true)
![Required field](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/screenshots/categoryfieldisrequiried.png?raw=true)
![Minimum length](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/screenshots/minimum_categorylength.png?raw=true)

## Tested Edit/Delete Category form validation
[Categories]()
- Tested that category name field is prefilled with the data needs to be edited.
- Tested all the fields are required fields and cannot be left blank
- Tested that minimum and maximum length
- Tested that on clicking edit category it's redirected to categories form with the changed details.
- Tested that on delete button deletes a selected category and a warning message is shown before deleting.
![Categories page](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/screenshots/categorieslist.png?raw=true)

## Tested Add Ingredient form validation and feature
[Add Ingredient]()
- Tested all the fields are required fields and cannot be left blank
- Tested that minimum and maximum length
- Tested that on adding ingredient it's redirected to ingredients form and at the same time the added ingredient is listed.
![Add ingredient form](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/screenshots/newingredient.png?raw=true)
![Required field](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/screenshots/ingredientfieldisrequiried.png?raw=true)
![Minimum length](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/screenshots/minimum_ingredientlength.png?raw=true) 

## Tested Edit/Delete Ingredient form validation
[Ingredients]()
- Tested that ingredient name field is prefilled with the data needs to be edited.
- Tested all the fields are required fields and cannot be left blank
- Tested that minimum and maximum length
- Tested that on clicking edit ingredient it's redirected to ingredients form with the changed details.
- Tested that on delete button deletes a selected ingredient and a warning message is shown before deleting.
![Ingredients page](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/screenshots/ingredientlist.png?raw=true) 

### Tested add recipe form validation
[Add recipe](https://foodrecipe-798974a40ee6.herokuapp.com/)
- Tested all the fields are required fields and cannot be left blank: 
- Tested the character length on the name input field must be a minimum of 5 and maximum of 50 characters.
- Tested the character length on the recipe description and recipe method input fields must be a minimum of 5 characters.
- Tested the drop down category menu contains all categories in the database, that a category can be selected and the field not left blank.
- Tested the drop down ingredient menu contains all ingredients in the database, that a ingredient can be selected and the field not left blank.
- Tested the submit button added the record to the database and can be seen listed in PostgreSQL.
- Tested that the user is redirected to the home page with added recipe to tell the user that the recipe has been successfully added.  
![Add recipe page](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/screenshots/newerecipe.png?raw=true)
![Required field](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/screenshots/recipefieldisrequiried.png?raw=true)

### Tested homepage with edit and delete recipe form validation
- Tested that all the fields are prefilled with the data needs to be edited. 
- Tested all the fields are required fields and cannot be left blank: 
- Tested the character length on the name input field must be a minimum of 5 and maximum of 50 characters.
- Tested the character length on the recipe description and recipe method input fields must be a minimum of 5 characters.
- Tested the drop down category menu contains all categories in the database, that a category can be selected and the field not left blank.
- Tested the drop down ingredient menu contains all ingredients in the database, that a ingredient can be selected and the field not left blank.
- Tested that once the user clicks the edit button after making changes, the user is redirected to home page with the edited details.
- Tested that once the user clicks the delete button, the user receives a confirmaition message that says their recipe will be deleted, and that the recipe record is deleted from the layout and the database on pressing delete button and also tested that the cancel button redirects back to the home page
- Checked the edit and delete buttons on the home page functioned correctly, and that only the selected recipe was permitted to edit or delete the recipe record. 
- Tested the collapsable is expandable for each recipe and details are correctly displayed for that particular recipe
[Homepage](https://foodrecipe-798974a40ee6.herokuapp.com/)  
![Homepage](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/screenshots/homepage.png?raw=true)


### Tested navigation links.
All navigation links on desktop and mobile were tested to make sure they linked to the relevant pages.


## Browser testing
- The desktop App was tested on Google Chrome, Microsoft Edge and Safari browsers, to check for responsive layouts and functionality on all pages. I tested all page layouts on a number of screensizes, which all proved responsive to the screen size. I tested website functionality on all browsers to cheeck that users were able to navigate through all pages, add, edit and delete recipe, ingredients and categories. The homepage view is illustrated below:  
![Desktop browser views](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/screenshots/browserdesktop.png?raw=true)
## Responsive layouts testing
- The App was tested on a series of devices to check the layouts automatically adapt to different devices with different screen sizes. I took a mobile first approach to responsive design; for example on the home page, the layout changes from a one column layout on mobile screens. This meant the user experience was as good, whether the site was viewed on a small mobile device or large desktop screen.
- Mobile screen - Iphone 12 pro:  
![iphone13 layouts](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/screenshots/iphone13.png?raw=true). 
- Tablet layout - iPad 10th edition   
![iPad mini layouts](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/screenshots/ipad10thedition.png?raw=true) 

## Device testing CRUD functionality
- I tested adding a recipe record on iPhone 13 device, then edited it and deleted it without any issues.
- I tested adding a recipe record on iPad10th Edition device, then edited it and deleted it without any issues.
- I tested adding a recipe record on MacBook device, then edited it and deleted it without any issues.

# Validation
### HTML validation:
I tested the app with the [W3C HTML checker](https://validator.w3.org/) and it indicated the following warnings:
- Warning: Section lacks heading. Consider using h2-h6 elements to add identifying headings to all sections, or else use a div element instead for any cases where no heading is needed. The reason for this is that the html (div and h4 headings) were hidden from the validator due to the jinga templating language.  
![HTML validation](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/screenshots/htmlresult.png?raw=true). 
### CSS validation
I tested style.css file with the [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) and no error was found.  
![CSS validation](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/screenshots/cssresult.png?raw=true)
### Javascript validation
The script.js was tested by [Jshint online checker](https://jshint.com/) Two warnings were issued about the let variable keyword being available in ES6 version since 2015. 
![Javascript warning](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/screenshots/javascriptresult.png?raw=true)
### Python validation
I tested routes.py file with [PEP8 Online Check](http://pep8online.com/) and the file is PEP8 compliant.  
![PEP8 compliant](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/screenshots/pythonresults.png?raw=true)

## Confirmation message examples
while deleting a record a confirmation message is displayed to the user before deleting. Some of these are illustrated below:
![Confirmation message examples](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/screenshots/deleterecipemodal.png?raw=true)

## Performance testing
I tested the app with Lighthouse in Chrome Dev Tools. Whilst the scores were good especially for best practices, the app would be improved primarily by reducing the size of the images used, in order to improve page load speed.
![Lighthouse performance summary](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/screenshots/performance.png?raw=true)

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

# Known Bugs
* When I add a recipe I see some space on description and preparation method input fields
  * I tried fixing, Since there is not much impact on the UX,I left it unfixed
  ![Lighthouse performance summary](https://github.com/fatimagama20/food-receipe/blob/main/foodrecipe/screenshots/knownbug.png?raw=true)
  