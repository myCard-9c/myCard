from django.test import TestCase
from django.urls import reverse
from myCard.models import UserProfile
from django.contrib import auth


class BaseTest(TestCase):
    def setUp(self):
        self.register_page = reverse('myCard:signup')
        self.login_page = reverse('myCard:login')
        self.logout_page = reverse('myCard:logout')
        self.dashboard_page = reverse('myCard:dashboard')
        self.public_cards_page = reverse('myCard:public_cards')
        self.resume_tips_page = reverse('myCard:resume_tips')
        self.create_card_page = reverse('myCard:create_card')
        self.edit_card_page = reverse('myCard:edit_card')
        self.your_card_page = reverse('myCard:your_card')

        self.user = {
            'username' : 'testeraccount1',
            'email' : 'testaccount77@gmail.com',
            'first_name' : 'tester',
            'last_name' : 'testertwo',
            'password1' : 'Testpass1',
            'password2' : 'Testpass1',
        }

        return super().setUp()

class AccessTest(BaseTest):

    # Tests whether the register page can be accessed when logged out
    def test_can_view_register_page(self):
        response = self.client.get(self.register_page)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'myCard/register.html')

    # Tests whether the login page can be accessed when logged out
    def test_can_view_login_page(self):
        response = self.client.get(self.login_page)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'myCard/login.html')

    # Tests whether the resume tips page can be accessed when logged out
    def test_can_view_resume_page(self):
        response = self.client.get(self.resume_tips_page)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'myCard/resume_tips.html')

    # Tests whether the public cards page can be accessed when logged out
    def test_can_view_public_cards_page(self):
        response = self.client.get(self.public_cards_page)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'myCard/public_cards.html')

    # Tests whether the logout page redirects when not logged in
    def test_can_view_logout_page(self):
        response = self.client.get(self.logout_page, follow=True)
        self.assertRedirects(response, '/myCard/login/?next=/myCard/logout/')


    # Tests whether the dashboard page redirects when not logged in
    def test_can_view_dashboard_page(self):
        response = self.client.get(self.dashboard_page, follow=True)
        self.assertRedirects(response, '/myCard/login/?next=/myCard/dashboard/')

    # Tests whether you can access create card page while not logged in
    def test_can_view_create_card_page(self):
        response = self.client.get(self.create_card_page, follow=True)
        self.assertRedirects(response, '/myCard/login/?next=/myCard/create_card/')

    # Tests whether you can access edit card page while not logged in
    def test_can_view_edit_card_page(self):
        response = self.client.get(self.edit_card_page, follow=True)
        self.assertRedirects(response, '/myCard/login/?next=/myCard/edit_card/')

    # Tests whether you are redirected when accessing your card page while not logged in
    def test_can_view_your_card_page(self):
        response = self.client.get(self.your_card_page, follow=True)
        self.assertRedirects(response, '/myCard/login/?next=/myCard/your_card/')

class AuthenticationTests(BaseTest):

    # Test whether user can register for an account successfully
    def test_user_can_register(self):
        response = self.client.post(self.register_page, self.user, format = 'text/html')
        self.assertEqual(response.status_code, 302)

    # Test whether valid account can log in
    def test_user_login_success(self):
        response = self.client.post('/myCard/login', {'username' : 'testeraccount1', 'password' : 'Testpass1'})
        self.assertEqual(response.status_code, 301)
