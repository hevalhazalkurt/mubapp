# { MUB : Multi User Blog }

**MUB** is a multi-user blog web app using the Python - Django infrastructure. It's works right now, however, I'm planning to add more features in the future. So, if you want to be informed, you can follow and/or give the star to the project.

Don't you like reading codes? You can also test [**MUBapp**](https://mubapp.herokuapp.com/) on Heroku.


<br>

<sub>P.S. The post images, titles and summaries is taken from various Medium content for creating dummy data. If you want to read any post just search on Medium with the title.</sub>

<br>

----

## Features

<br>

![](media/mubapp.gif)

<br>

* Multi user blogging system
* User profile card
* Auto-slug url by post title
* Post listing by user
* Post listing by category
* Related posts by category
* Image uploading
* Pagination
* Email backend
* User register
* User login / logout
* User password reset
* User post form on frontend
* Updatable user profile
* Rich text editor for new and update post
* Post create, update and delete on frontend
* Clean and responsive design with TailwindCSS
* SEO friendly meta tags system


<br>

----

### Requirements

```
asgiref==3.2.7
Django==3.0.5
django-ckeditor==5.9.0
django-crispy-forms==1.9.0
django-js-asset==1.2.2
gunicorn==20.0.4
Pillow==7.1.2
psycopg2-binary==2.8.5
python-dotenv==0.13.0
pytz==2020.1
sqlparse==0.3.1
whitenoise==5.0.1
```


<br>

----

### Project Tree

```
├── mubapp
    ├── Procfile
    ├── README.md
    ├── blog
    │   ├── __init__.py
    │   ├── __pycache__
    │   ├── admin.py
    │   ├── apps.py
    │   ├── migrations
    │   ├── models.py
    │   ├── static
    │   │   └── blog
    │   ├── templates
    │   │   └── blog
    │   │       ├── about.html
    │   │       ├── base.html
    │   │       ├── category_posts.html
    │   │       ├── home.html
    │   │       ├── post_confirm_delete.html
    │   │       ├── post_detail.html
    │   │       ├── post_form.html
    │   │       └── user_posts.html
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── db.sqlite3
    ├── manage.py
    ├── media
    │   ├── cover_pics
    │   ├── images
    │   ├── profile_pics
    │   └── uploads
    ├── mubapp
    │   ├── __init__.py
    │   ├── __pycache__
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── requirements.txt
    ├── staticfiles
    │   ├── admin
    │   │   ├── css
    │   │   ├── fonts
    │   │   ├── img
    │   │   └── js
    │   └── ckeditor
    └── users
      ├── __init__.py
      ├── __pycache__
      ├── admin.py
      ├── apps.py
      ├── forms.py
      ├── migrations
      ├── models.py
      ├── signals.py
      ├── templates
      │   └── users
      │       ├── login.html
      │       ├── logout.html
      │       ├── password_reset.html
      │       ├── password_reset_complete.html
      │       ├── password_reset_confirm.html
      │       ├── password_reset_done.html
      │       ├── profile.html
      │       └── register.html
      ├── tests.py
      └── views.py
```
