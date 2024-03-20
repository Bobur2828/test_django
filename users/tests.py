from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import get_user
from django.core.exceptions import ValidationError
class RegisterTestCase(TestCase):
    # def test_success_register(self):
    #     self.client.post(
    #         reverse("users:register"),
    #         data={
    #             'username':'boburjon',
    #             'first_name':'Boburjon',
    #             'last_name':'Gulomov',
    #             'email':'gulomof@gmail.com',
    #             'password':'2828',
    #         }
    #     )

    #     user_count=User.objects.count()
    #     self.assertEqual(user_count,1)

    #     user=User.objects.get(username='boburjon')
    #     self.assertEqual(user.username,'boburjon')
    #     self.assertEqual(user.first_name,'Boburjon')
    #     self.assertEqual(user.last_name,'Gulomov')
    #     self.assertEqual(user.email,'gulomof@gmail.com')
    #     self.assertNotEqual(user.password,'2828')
    #     self.assertTrue(user.check_password('2828'))

    # def test_required_fields(self):
    #     response=self.client.post(
    #         reverse("users:register"),
    #         data={
    #             'first_name':'Boburjon',
    #             'last_name':'Gulomov',
    #             'email':'gulomof@gmail.com',
    #         }
    #     )
    #     form=response.context['form']

    #     self.assertTrue([form.errors])
    #     self.assertEqual(form.errors['username'],['This field is required.'])

   
    # def test_already_exists(self):
    #     create=User.objects.create(username='boburjon', password='2828')
        
    #     response = self.client.post(
    #         reverse("users:register"),
    #         data={
    #             'username': 'boburjon',
    #             'first_name': 'Boburjon',
    #             'last_name': 'Gulomov',
    #             'email': 'gulomof@gmail.com',
    #             'password': '2828',
    #         }
    #     )
    #     user_count = User.objects.filter(username='boburjon').count()
    #     self.assertTrue(user_count,1)
        
    #     form = response.context['form']
    #     self.assertEqual(form.errors['username'], ['A user with that username already exists.'])

    # #         # tekshirish uchun pasdagini ochib koring
    # #     # self.assertEqual(form.errors['username'], ['A user with that exists.'])  

    # def test_email_valid(self):# email ni notogri berilsa hatolik berilyatganini tekshiradi 
    #     response=self.client.post(
    #         reverse("users:register"),
    #         data={
    #             'username': 'boburjon',
    #             'first_name':'Boburjon',
    #             'last_name':'Gulomov',
    #             'email':'gulomof@',
    #             'password': '2828',

    #         }                   
    #     )
    #     form=response.context['form']
    #     self.assertTrue(form.errors)

    #     self.assertIn('email', form.errors)
    #     self.assertEqual(form.errors['email'], ['Enter a valid email address.'])

    # def test_username_valid(self):
    #     user = User.objects.create(username='boburjon', password='5852828')
    #     user.set_password('5852828')
    #     user.save()
    #     response = self.client.post(
    #         reverse('users:login'),
    #         data={
    #             'username': 'boburjon',
    #             'password': '585282',
    #         }
    #     )

    #     user = get_user(self.client)
    #     self.assertFalse(user.is_authenticated)
       
    def test_login_notogri_malumot(self):
        user = User.objects.create(username='boburjon')
        user.set_password('5852828')
        user.save()
        response = self.client.post(
            reverse('users:login'),  
            data={
                'username': 'boburjon',
                'password': '585282',  
            }
        )    

        user = User.objects.get(username='boburjon')

        self.assertTrue(user.check_password('5852828'))  
        self.assertEqual(user.password, '5852828')  

        form = response.context['form']

        self.assertTrue(form.errors)

        self.assertIn('username', form.errors)
        self.assertEqual(form.errors['username'], ['This field is required.'])


    def test_profile(self):
        user = User.objects.create_user(
            username='boburjon',
            first_name='Boburjon',
            last_name='Gulomov',
            email='farmusic@inbox.ru',
            password='5852828'
        )

        self.client.login(username='boburjon', password='5852828')

        response = self.client.get(reverse('users:profile'))

        self.assertContains(response, 'Boburjon')
        self.assertContains(response, 'Gulomov')
        self.assertContains(response, 'farmusic@inbox.ru')







