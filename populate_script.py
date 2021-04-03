import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myCard_project.settings')
import django
django.setup()
from myCard.models import Card
from django.contrib.auth.models import User

def populate():
    #Add a new array for the cards
    filepath = 'user1.png'
    jose_cards = [
    {'name':'Business',
    'phone_no':101010101,
    'location':'Mexico',
    'occupation':'Astronaut',
    'website':'www.jose.com',
    'media_links':'www.jose.com',
    'picture': filepath,
    'about':'Lorem Ipsum',
    'visibility': True},
    {'name':'Personal',
    'phone_no':111110101,
    'location':'Brazil',
    'occupation':'Computer',
    'website':'www.hose.com',
    'media_links':'www.kose.com',
    'picture': filepath,
    'about':'Lorem Ipsum Lorem Ipsum',
    'visibility': False},
    {'name':'Company',
    'phone_no':101019991,
    'location':'America',
    'occupation':'Javalin Thrower',
    'website':'www.jezzy.com',
    'media_links':'www.jerry.com',
    'picture': filepath,
    'about':'Lorem Ips',
    'visibility': True}
    ]
    
    maria_cards = [
    {'name':'Business',
    'phone_no':102323231,
    'location':'Japan',
    'occupation':'Microphone',
    'website':'www.maria.com',
    'media_links':'www.mse.com',
    'picture': filepath,
    'about':'Lo Ipsum',
    'visibility': True},
    {'name':'Personal',
    'phone_no':111222101,
    'location':'France',
    'occupation':'Garbage man',
    'website':'www.ggle.com',
    'media_links':'www.avemaria.com',
    'picture': filepath,
    'about':'Lorem Ipsu Loem Ipsum',
    'visibility': False},
    {'name':'Company',
    'phone_no':111119991,
    'location':'Canada',
    'occupation':'Bear Fighter',
    'website':'www.bfight.com',
    'media_links':'www.chickfila.com',
    'picture': filepath,
    'about':'Lor Ips',
    'visibility': True}
    ]
    jerry_cards = [
    {'name':'Business',
    'phone_no':105323231,
    'location':'Jaan',
    'occupation':'Mphone',
    'website':'www.xxJerry.com',
    'media_links':'www.mse.com',
    'picture': filepath,
    'about':'Lo Ipsum',
    'visibility': True},
    {'name':'Personal',
    'phone_no':111222101,
    'location':'France',
    'occupation':'Garbage man',
    'website':'www.ggle.com',
    'media_links':'www.avemaria.com',
    'picture': filepath,
    'about':'Lorem Ipsu Loem Ipsum',
    'visibility': False},
    {'name':'Company',
    'phone_no':111119991,
    'location':'Canada',
    'occupation':'Bear Fighter',
    'website':'www.bfight.com',
    'media_links':'www.chickfila.com',
    'picture': filepath,
    'about':'Lor Ips',
    'visibility': True}
    ]
    
    #Put in a new user and link it to cards array
    users = {'Jose1': {'cards': jose_cards,'firstname':'Jose','lastname':'Jones','email':'josa@domain.com','password':'hoseyman'},
    'maria1': {'cards': maria_cards,'firstname':'Maria','lastname':'Karia','email':'maria@domain.com','password':'avemaria'},
    'jerry1': {'cards': jerry_cards,'firstname':'Jerrry','lastname':'James','email':'JJ@domain.com','password':'tom'},
    }
   
    for user, user_data in users.items():
         u = add_user(user,user_data['firstname'],user_data['lastname'],user_data['email'],user_data['password'])
         for c in user_data['cards']:
                add_card(u,c['name'], user_data['firstname'],user_data['lastname'],user_data['email'], c['phone_no'],c['location'],c['occupation'],c['website'],c['picture'],c['media_links'],c['about'],c['visibility'])
               
def add_card(user, name, firstname, lastname, email, phone_no, location, occupation, website, picture, media_links, about, visibility):
    c = Card.objects.get_or_create(user = user, name = name, visibility = visibility)[0]
    c.first_name = firstname
    c.last_name = lastname
    c.email = email
    c.phone_no = phone_no
    c.location = location
    c.occupation = occupation
    c.website = website
    c.picture =  picture
    c.media_links = media_links
    c.about = about
    c.save()
    return c
    
def add_user(name,firstname,lastname,email,password):
    u = User.objects.get_or_create(username = name)[0]
    u.firstname = firstname
    u.lastname = lastname
    u.email = email
    u.password =  password
    u.save()
    return u

# Start execution here!
if __name__ == '__main__':
    print('Starting m population script...')
    populate()