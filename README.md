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

Same as above.

### Allow users to take assessments ###

Currently, I'm fighting w/ Django's form API.  It seems simple enough to use for basic forms; however, the dynamic nature of the assessments it proving to be problematic.  In short:

* If I take the obvious approach, then I end up w/ bloated form objects that are vulnerable to mass assignment.
* If I create custom forms, then I end up having to do a lot of data integrity checks inside of the view.  This feels like I'm fighting Django.

I think I can actually solve the problem via a little bit of meta-programming.  But, I'll handle that later.

