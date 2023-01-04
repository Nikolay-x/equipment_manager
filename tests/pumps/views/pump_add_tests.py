from django.contrib.auth.models import Group
from django.urls import reverse
from mixer.backend.django import mixer

from em_asd.pumps.models import Pump
from tests.base.base_test_case import BaseTestCase


class PumpAddTests(BaseTestCase):
    PUMP_VALID_DATA = {
        'tag': 'P0001',
        'name': 'Name1',
        'type': 'Dosing',
        'model': f'Model1',
        'fluid': f'Sea Water',
        'flow_rate': 25,
        'head': 15,
        'power': 12,
    }

    def test_pump_add__engineer_user__expect_pump_to_be_added(self):
        credentials = {
            'username': 'nb',
            'password': 'QwertAsdf',
        }

        user = self.create_and_login_user(**credentials)
        group = mixer.blend(Group, name='Engineer')
        user.groups.add(group)

        self.client.post(reverse('pump add'), self.PUMP_VALID_DATA, )

        pump = Pump.objects.all()

        self.assertEqual(True, user.is_authenticated)
        self.assertEqual(1, len(pump))

    def test_pump_add__not_engineer_user__expect_pump_not_to_be_added(self):
        credentials = {
            'username': 'nb',
            'password': 'QwertAsdf',
        }

        user = self.create_and_login_user(**credentials)
        group = mixer.blend(Group, name='Engineer1')
        user.groups.add(group)

        self.client.post(reverse('pump add'), self.PUMP_VALID_DATA, )

        pump = Pump.objects.all()

        self.assertEqual(True, user.is_authenticated)
        self.assertEqual(0, len(pump))
