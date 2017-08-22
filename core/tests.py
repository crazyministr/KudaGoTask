import os
from core.models import Event, Place, Schedule
from django.test import TestCase
from django.conf import settings
from django.core.management import call_command


class LoadXMLCommandTest(TestCase):
    def setUp(self):
        source = os.path.join(settings.BASE_DIR, 'feed', 'test.xml')
        call_command('loadxml', source)

    def test_all_data_loaded(self):
        self.assertEqual(16, Event.objects.count())
        self.assertEqual(11, Place.objects.count())
        self.assertEqual(435, Schedule.objects.count())

    def test_some_event_tags(self):
        event = Event.objects.get(eid=94114)
        tags = {tag.name for tag in event.tags.all()}
        self.assertEqual({'16+', 'концерт', 'метал'}, tags)
