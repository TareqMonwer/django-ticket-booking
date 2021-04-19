# django-ticket-booking : Open source project for awesome Django devs, Learners.
Goal: Build A minimal functional ticket booking system with Django, JavaScript and Bootstrap/Sass/CSS.

### We Have a [Contribution Guideline Here, Please Check.](contribute.md)


### Installation
+ clone & go to the repo folder
+ create a virtual environment `virtualenv env` or use any equivalant tool.
+ activate virtualenv `source env/bin/activate` in linux. For windows, use `.\env\bin\activate.bat` (probably).
+ Install dependencies by running `pip install -r requirements.txt` command.
+ Load fixtures for the seats, you may need to create a Car object from admin dashboard to be able to import fixtures.
+ Command for loading fixtures: `python manage.py loaddata core/fixtures/carseats.json`, windows users should use backslash instead of forward slashes.
+ run `python manage.py runserver`
