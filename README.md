# myCard

myCard is a web application built with Django where users can create their own Personal Cards, share and download them.

## Lab group 9 - Team C
- Manuel Simonetta: 2472780S
- Donald MacKenzie: 2426230M
- Alex Kilkenny: 2464370K
- Alexander McAteer: 2461479M

The source code is available at [https://github.com/myCard-9c/myCard](https://github.com/myCard-9c/myCard) and is deployed at *pythonanywhere_link*.

## To deploy locally:
This project runs on Python 3.

To clone the repository, run

`git clone https://github.com/myCard-9c/myCard`

Once the repository is locally cloned, enter the installation directory:

`cd myCard/myCard_project`

Next, install the dependencies with

`pip install -r requirements.txt`

If the database is empty, some errors will appear. To fix this, run database migrations, and run the population script:

```
python manage.py makemigrations
python manage.py migrate
python population_script.py
```

Start a test server by running

`python manage.py runserver`

#### Important notice:
Some features will not be functional when running the application on localhost, i.e.:
###### 1) Google's OAuth based authentication
###### 2)
###### 3)

## External Resources:
### Styling:
##### [Bootstrap 5]()
Bootstrap CSS framework which allows a responsive and intuitive interface.
##### Add others, if used

### Libraries and Dependencies:
##### [django-allauth](https://github.com/pennersr/django-allauth)
Used to implement OAuth authentication.
##### [django-crispy-forms](https://github.com/django-crispy-forms/django-crispy-forms)
Used to customize the django-allauth forms.
##### [coverage](https://coverage.readthedocs.io/en/coverage-5.5/)
Used to generate a coverage report of areas that require testing
##### [live-server](https://github.com/tapio/live-server)
Used to view testing coverage with Python's inbuilt 'Coverage' module. (Not required to run tests)
