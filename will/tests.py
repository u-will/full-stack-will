from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Will


class WillTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='tester',
            email='tester@email.com',
            password='pass'
        )

        self.will = Will.objects.create(
            name='pickle',
            description='refreshing',
            purchaser=self.user,
        )

    def test_string_representation(self):
        will = Will(name='Snicker')
        self.assertEqual(str(will), will.name)

    def test_will_content(self):
        self.assertEqual(f'{self.will.name}', 'pickle')
        self.assertEqual(f'{self.will.purchaser}', 'tester')
        self.assertEqual(f'{self.will.description}', 'refreshing')

    def test_will_list_view(self):
        response = self.client.get(reverse('will_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'pickle')
        self.assertTemplateUsed(response, 'will-list.html')

    def test_will_detail_view(self):
        response = self.client.get(reverse('will_detail', args='1')) #'/will/1/')
        no_response = self.client.get('/will/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'refreshing')
        self.assertTemplateUsed(response, 'will-detail.html')


    def test_will_create_view(self):
        response = self.client.post(reverse('will_create'), {
            'name': 'Chicharrones',
            'description': 'Low carb',
            'purchaser': self.user,
        })

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Chicharrones')
        self.assertContains(response, 'Low carb')
        self.assertTemplateUsed(response, 'will-create.html')


    def test_will_update_view(self):
        response = self.client.post(reverse('will_update',args='1'), {
            'name': 'Updated name',
            'description': 'Updated description',
        })
        self.assertEqual(response.status_code, 302)

    def test_will_update_view_redirect(self):
        response = self.client.post(reverse('will_update',args='1'), {
            'name': 'Updated name',
            'description': 'Updated description',
        }, follow=True)

        self.assertEqual(response.status_code, 200)

        self.assertContains(response, 'Updated name')

        self.assertTemplateUsed('will-detail.html')


    def test_will_delete_view(self):
        response = self.client.get(reverse('will_delete',args='1'))
        self.assertEqual(response.status_code, 200)