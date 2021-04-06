# myCard

myCard is a web application built with Django where users can create their own Personal Cards, share and download them. This project runs on Python 3, the source code is available at [myCard_GitHub_repository](https://github.com/myCard-9c/myCard) and is deployed at [myCard.pythonanywhere.com](https://mycard.pythonanywhere.com/myCard/).

## Lab group 9 - Team C
The students who worked on the project are:
- Manuel Simonetta:  2472780S
- Donald Mackenzie:  2426230M
- Alex Kilkenny:     2464370K
- Alexander McAteer: 2461479M


## To deploy locally:
Clone the repository by running

`git clone https://github.com/myCard-9c/myCard`

Once the repository is locally cloned, enter the installation directory:

`cd myCard/myCard`

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

#### To log in the auto-created accounts, use the following credentials:
###### 1) username: *jose_carter* | password: *Joseito98.*
###### 2) username: *olivia_brown* | password: *Olivia00..*
###### 3) username: *tegan_price* | password: *Tegan99.*
###### 4) username: *micheala_pratt* | password: *Micheala03.*
###### 5) username: *laurel_castillo* | password: *Laurel55.*

#### Important notice:
The following functionalities will not be funcional on the *pythonanywhere* server.
###### 1) Google's OAuth-based authentication, due to issues with domain ownership. The set-up process on the marker's local machine can be explained upon the request.
###### 2) The "Download" function, due to issues with loading external JavaScript. This will work if the project is deployed locally.


## External Resources:
### CSS styling:
##### [Bootstrap 5](https://getbootstrap.com/)
Bootstrap CSS framework which allows a responsive and intuitive interface.
### Illustration:
##### [Storyset](https://storyset.com/)
### Technical:
##### [html2canvas](https://html2canvas.hertzen.com/) and [jspdf](https://github.com/MrRio/jsPDF)
Used to convert HTML into PDF
##### [DOMPurify](https://github.com/cure53/DOMPurify)
Used to clean up HTML files

### Libraries and Dependencies:
##### [django-allauth](https://github.com/pennersr/django-allauth)
Used to implement OAuth authentication.
##### [django-crispy-forms](https://github.com/django-crispy-forms/django-crispy-forms)
Used to customize the django-allauth forms.
##### [coverage](https://coverage.readthedocs.io/en/coverage-5.5/)
Used to generate a coverage report of areas that require testing
##### [live-server](https://github.com/tapio/live-server)
Used to view testing coverage with Python's inbuilt 'Coverage' module. (Not required to run tests)
