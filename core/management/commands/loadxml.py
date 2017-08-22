from django.core.management import BaseCommand
from parser.XmlFeed import XmlFeed
from core.models import *


class Command(BaseCommand):
    EVENT_FIELDS = ('eid', 'etype', 'price', 'kids', 'title',
                    'age_restricted', 'text', 'description',
                    'runtime', 'stage_theatre')

    def add_arguments(self, parser):
        parser.add_argument('source', help='source file')

    def handle(self, *args, **options):
        source = options.get('source', None)
        parser = XmlFeed(source)
        parser.parse()

        events = parser.get_events()
        # places = parser.get_places()
        # schedule = parser.get_schedule()

        self.load_events(events)

    def load_events(self, events):
        for event in events:
            kwargs = {}
            for field in self.EVENT_FIELDS:
                kwargs[field] = event[field]

            db_event = Event.objects.create(**kwargs)
            # db_event.save()

            db_event.gallery.clear()
            db_event.persons.clear()
            db_event.tags.clear()

            for image in event['gallery']:
                db_image, _ = Image.objects.get_or_create(url=image)
                db_event.gallery.add(db_image)

            for person in event['persons']:
                db_person, _ = Person.objects.get_or_create(name=person.get('name'),
                                                            role=person.get('role'))
                db_event.persons.add(db_person)

            for tag in event['tags']:
                db_tag, _ = Tag.objects.get_or_create(name=tag)
                db_event.tags.add(db_tag)
