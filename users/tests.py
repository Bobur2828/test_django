from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
class RegisterTestCase(TestCase):
    def test_success_register(self):
        self.client.post(
            reverse("users:register"),
            data={
                'username':'boburjon',
                'first_name':'Boburjon',
                'last_name':'Gulomov',
                'email':'gulomof@gmail.com',
                'password':'2828',
            }
        )

        user_count=User.objects.count()
        self.assertEqual(user_count,1)

        user=User.objects.get(username='boburjon')
        self.assertEqual(user.username,'boburjon')
        self.assertEqual(user.first_name,'Boburjon')
        self.assertEqual(user.last_name,'Gulomov')
        self.assertEqual(user.email,'gulomof@gmail.com')
        self.assertNotEqual(user.password,'2828')
        self.assertTrue(user.check_password('2828'))

    def test_required_fields(self):
        response=self.client.post(
            reverse("users:register"),
            data={
                'first_name':'Boburjon',
                'last_name':'Gulomov',
                'email':'gulomof@gmail.com',
            }
        )
        form=response.context['form']

        self.assertTrue([form.errors])
        self.assertEqual(form.errors['username'],['This field is required.'])

   
    def test_already_exists(self):
        create=User.objects.create(username='boburjon', password='2828')
        
        response = self.client.post(
            reverse("users:register"),
            data={
                'username': 'boburjon',
                'first_name': 'Boburjon',
                'last_name': 'Gulomov',
                'email': 'gulomof@gmail.com',
                'password': '2828',
            }
        )
        user_count = User.objects.filter(username='boburjon').count()
        self.assertTrue(user_count,1)
        
        form = response.context['form']
        self.assertEqual(form.errors['username'], ['A user with that username already exists.'])

    #         # tekshirish uchun pasdagini ochib koring
    #     # self.assertEqual(form.errors['username'], ['A user with that exists.'])  

    def test_email_valid(self):# email ni notogri berilsa hatolik berilyatganini tekshiradi 
        response=self.client.post(
            reverse("users:register"),
            data={
                'username': 'boburjon',
                'first_name':'Boburjon',
                'last_name':'Gulomov',
                'email':'gulomof@',
                'password': '2828',

            }                   
        )
        form=response.context['form']
        self.assertTrue(form.errors)

        self.assertIn('email', form.errors)
        self.assertEqual(form.errors['email'], ['Enter a valid email address.'])

        
   









