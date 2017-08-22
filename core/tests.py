import os
from core.models import Event, Place, Schedule
from django.test import TestCase
from django.conf import settings
from django.core.management import call_command


class LoadXMLCommandTest(TestCase):
    def setUp(self):
        self.source = os.path.join(settings.BASE_DIR, 'feed', 'test.xml')

    def test_all_data_loaded(self):
        call_command('loadxml', self.source)

        self.assertEqual(16, Event.objects.count())
        self.assertEqual(11, Place.objects.count())
        self.assertEqual(435, Schedule.objects.count())
