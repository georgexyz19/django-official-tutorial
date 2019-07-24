## Django Official Tutorial Code

The link of Django Official Tutorial is:

<https://docs.djangoproject.com/en/2.2/intro/>

Each part is stored in a separate directory.


### Part 1  Project Setup

    $django-admin startproject myproject .
    $python manage.py runserver
    $python manage.py startapp polls

Create a project
Write the first hello world view



### Part 2  Django Models and Django Admin

Database setup

    $python manage.py migrate
    $sqlite3 db.sqlite3  # cli for sqlite

    $python manage.py makemigrations polls  # to 0001_initial.py
    $python manage.py sqlmigrate polls 0001  # SQL

    $python manage.py check

django\_migrations special table in the database to track

add django-extensions app, see requirements.txt
    $pip install -r requirements.txt

    $python manage.py shell_plus --ipython   # same as 
    $python manage.py shell_plus
    
It auto loads all the models. 

Introducing the Django Admin



### Part 3  Django Views and Templates

Write templates and views for index and detail two pages. 

Add `app_name = 'polls'` to the polls/urls.py to set url namespace. 

    {% url 'polls:detail' question.id %}



### Part 4  Django Form

This part has an example of manually writing a form
The code is smart. 

This part also introduces generic class based views

    detail ---|
              |
              | vote (can go back to detail or results depending on selection)
    results---|



### Part 5  Testing

Command to run django tests:

    $python manage.py test polls

Test class is derived from TestCase 

    class QuestionModelTests(TestCase)



### Part 6 Static Files

static file is saved in this directory

polls/static/polls/style.css

In the style.css file, cannot use `static` tag. CSS file does not go thru 
template system. 

    background: white url("images/background.gif") no-repeat;
    
    

### Part 7  Customize Admin Form

The code below is interesting.

```
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3
   
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = ...
    inlines = [ChoiceInline]
    
admin.site.register(Question, QuestionAdmin)
```


Last Update: 2019/07/24 08:46:43

