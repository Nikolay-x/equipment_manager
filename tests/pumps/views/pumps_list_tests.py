from django.urls import reverse

from em_asd.pumps.models import Pump
from tests.base.base_test_case import BaseTestCase


class PumpsListTests(BaseTestCase):
    def test_pumps_list__when_no_pumps__expect_empty_list_and_count_in_context(self):
        credentials = {
            'username': 'nb',
            'password': 'QwertAsdf',
        }

        self.create_and_login_user(**credentials)

        response = self.client.get(reverse('pumps list'))

        self.assertCollectionEmpty(response.context['pumps'])
        self.assertEqual(0, response.context['pumps_count'])
        self.assertTemplateUsed(response, 'pumps/pumps.html')

    def test_pumps_list__when_pumps__expect_list_of_pumps_and_count(self):
        credentials = {
            'username': 'nb',
            'password': 'QwertAsdf',
        }

        self.create_and_login_user(**credentials)

        pumps_count = 9
        pumps = [
            Pump(
                tag=f'P{i}',
                name=f'Name1',
                type=f'Dosing',
                model=f'Model{i}',
                fluid=f'Sea Water',
                flow_rate=f'9{i}',
                head=f'8{i}',
                power=f'3{i}',
            )
            for i in range(1, pumps_count + 1)
        ]

        Pump.objects.bulk_create(pumps)

        response = self.client.get(reverse('pumps list'))

        self.assertListEqual(pumps, list(response.context['pumps']))
        self.assertEqual(pumps_count, response.context['pumps_count'])
        self.assertTemplateUsed(response, 'pumps/pumps.html')

    def test_pumps_list__when_anonymous_user__expect_to_redirect_to_login_page(self):
        response = self.client.get(reverse('pumps list'))

        self.assertEqual('/accounts/login/?next=/pumps/pumps_list/', response.url)
        self.assertEqual(302, response.status_code)

    def test_pumps_list__when_logged_in_user__expect_username_to_be_correct(self):
        username = 'nb'
        credentials = {
            'username': username,
            'password': 'QwertAsdf',
        }

        self.create_and_login_user(**credentials)

        response = self.client.get(reverse('pumps list'))

        self.assertEqual(username, response.context['user'].username)

    def test_pumps_list__when_context_is_provided__expect_context_to_be_in_context(self):
        response = self.client.get(
            reverse('pumps list'),
            context={
                'query': 'the-query',
            })

        self.assertEqual('the-query', response.request['context']['query'])
