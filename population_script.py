import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myCard_project.settings')
import django
django.setup()
from myCard.models import Card
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
# Populate the database creating Users and Cards
def populate():
    # José's cards definition
    jose_picture = 'user_avatars/user1.png'
    jose_cards = [
    {'name':'Business Card',
    'phone_no':712456789,
    'location':'Mexico',
    'occupation':'Math tutor',
    'website':'www.math-with-josé.com',
    'picture': jose_picture,
    'visibility': True},
    {'name':'Personal Card',
    'phone_no':9876543210,
    'location':'Brazil',
    'occupation':'Student',
    'website':'www.instagram.com/jose_carter',
    'picture': jose_picture,
    'visibility': False},
    {'name':'School Card',
    'phone_no':101019991,
    'location':'California',
    'occupation':'Student',
    'website':'www.instagram.com/jose_carter',
    'picture': jose_picture,
    'visibility': True}
    ]

    # Olivia's cards definition
    olivia_picture = 'user_avatars/user2.png'
    olivia_cards = [
    {'name':'Business Card',
    'phone_no':785451201,
    'location':'Middleton',
    'occupation':'Lawyer',
    'website':'www.olia-brown.com',
    'picture': olivia_picture,
    'visibility': True},
    {'name':'Company Card',
    'phone_no':111222101,
    'location':'Chicago',
    'occupation':'CEO of C&G',
    'website':'www.c&g/oliabrown.com',
    'picture': olivia_picture,
    'visibility': True},
    {'name':'Personl Card',
    'phone_no':235467890,
    'location':'Canada',
    'occupation':'Law Tutor',
    'website':'www.study-with-o.com',
    'picture': olivia_picture,
    'visibility': False}
    ]

    # Tegan's cards definition
    tegan_picture = 'user_avatars/user3.png'
    tegan_cards = [
    {'name':'University Card',
    'phone_no':5321457890,
    'location':'Toronto',
    'occupation':'Lecturer',
    'website':'www.uoft/tegan_price.com',
    'picture': tegan_picture,
    'visibility': True},
    {'name':'Personal Card',
    'phone_no':111222101,
    'location':'Ottawa',
    'occupation':'Lecturer',
    'website':'www.facebook.com/tegan-price',
    'picture': tegan_picture,
    'visibility': False},
    {'name':'Company Card',
    'phone_no':111119991,
    'location':'Toronto',
    'occupation':'Human Resources director',
    'website':'www.hr4u.com',
    'picture': tegan_picture,
    'visibility': False}
    ]

    # Micheala's cards definition
    micheala_picture = 'user_avatars/user4.png'
    micheala_cards = [
    {'name':'Student Card',
    'phone_no':3465586794,
    'location':'Italy',
    'occupation':'CS Student',
    'website':'www.uniroma/micheala_pratt.com',
    'picture': micheala_picture,
    'visibility': True},
    {'name':'Personal Card',
    'phone_no':3756420157,
    'location':'Germany',
    'occupation':'Tutor',
    'website':'www.instagram.com/m_pratt.com',
    'picture': micheala_picture,
    'visibility': True},
    {'name':'Fun Card',
    'phone_no':1111111111,
    'location':'Wonderland',
    'occupation':'Unemployed',
    'website':'',
    'picture': micheala_picture,
    'visibility': False}
    ]

    # Laurel's cards definition
    laurel_picture = 'user_avatars/user5.png'
    laurel_cards = [
    {'name':'Family Card',
    'phone_no':754315270,
    'location':'Miami',
    'occupation':'Full-time mom',
    'website':'www.laurel-mom-tips.com',
    'picture': laurel_picture,
    'visibility': True},
    {'name':"Friend's Card",
    'phone_no':9784321506,
    'location':'Florida',
    'occupation':'Assistant',
    'website':'www.facebook.com/my-friend.com',
    'picture': laurel_picture,
    'visibility': False},
    {'name':'Personal Card',
    'phone_no':2583691470,
    'location':'Glasgow',
    'occupation':'Unemployed',
    'website':'',
    'picture': laurel_picture,
    'visibility': False}
    ]

    # Create users dictionary and link their cards
    users = {
    'jose_carter': {'cards': jose_cards,'firstname':'José','lastname':'Carter','email':'josé.carter@domain.com','password':'Joseito98.'},
    'olivia_brown': {'cards': olivia_cards,'firstname':'Olivia','lastname':'Brown','email':'olivia_brown@domain.com','password':'Olivia00.'},
    'tegan_price': {'cards': tegan_cards,'firstname':'Tegan','lastname':'Price','email':'tegan_price@domain.com','password':'Tegan99.'},
    'micheala_pratt': {'cards': micheala_cards,'firstname':'Micheala','lastname':'Pratt','email':'micheala_pratt@domain.com','password':'Michaela03.'},
    'laurel_castillo': {'cards': laurel_cards,'firstname':'Laurel','lastname':'Castillo','email':'laurel_castillo@domain.com','password':'Tegan99.'},
    }

    # Create User and Cards objects iterating over the dictionary
    for user, user_data in users.items():
         u = add_user(user, user_data['firstname'], user_data['lastname'], user_data['email'], user_data['password'])
         for c in user_data['cards']:
            add_card(u,c['name'], user_data['firstname'], user_data['lastname'], user_data['email'], c['phone_no'], c['location'], c['occupation'], c['website'], c['picture'], c['visibility'])

# Add a Card and set its fields
def add_card(user, name, firstname, lastname, email, phone_no, location, occupation, website, picture, visibility):
    c = Card.objects.get_or_create(user = user, name = name, visibility = visibility)[0]
    c.first_name = firstname
    c.last_name = lastname
    c.email = email
    c.phone_no = phone_no
    c.location = location
    c.occupation = occupation
    c.website = website
    c.picture =  picture
    c.save()
    return c

# Add a User and set their fields
def add_user(name,firstname,lastname,email,password):
    u = User.objects.get_or_create(username = name)[0]
    u.firstname = firstname
    u.lastname = lastname
    u.email = email
    u.password =  make_password(password)
    u.save()
    return u

# Start the execution
if __name__ == '__main__':
    print('Starting to populate myCard...')
    populate()
    print('myCard population was successfull!')
