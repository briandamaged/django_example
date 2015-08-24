# A. Q. A. #

Assessment. Question. Answer.

## Purpose ##

This is just a toy application that I'm writing to learn the basics of Django.

## Installation ##

First, you will need to install Python 2.7.x .  The code will probably work w/ Python 3.x as well, but I have not confirmed this yet.

Next, install the dependencies via pip:

```shell
pip install -r requirements.txt
```

Now, create the database:

```shell
python manage.py migrate
```

And finally, launch the server:

```shell
python manage.py runserver
```


## Usage ##

### Adding Users ###

First, you will need to add an adminstrative user through the command line:

```shell
python manage.py createsuperuser
```

Currently, all additional users must be added through Django's admin control panel.  Assuming that your server is running on port 8000, you can access this via:

http://localhost:8000/admin


### Defining Articles / Questions ###

Once again: currently, all data entry is performed via Django's admin control panel at:

http://localhost:8000/admin


## TODO ##

### Add "Sign Up" Functionality ###

Currently, all users must be added through Django's admin control panel.  It would be nice to add first-class support for user registration directly into the application itself.

### Add data entry pages for Articles / Questions ###

Right now, the models compute a number of virtual properties, such as the maximum possible score for an assessment.  Each time the models are accessed, this value needs to be recomputed.  From an efficiency standpoint, it would be better to simply compute these values whenever the articles are persisted.  That way, the cached values could be retrieved without any need to perform database joins.

But, it would be safe to do this until after we replace Django's admin control panel.  Otherwise, end-users will be able to tamper w/ the derived properties, which could have unanticipated consequences.
