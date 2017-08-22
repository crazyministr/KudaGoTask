from django.core.exceptions import ObjectDoesNotExist
from django.core.management import BaseCommand
from parser.XmlFeed import XmlFeed
from core.models import *


class Command(BaseCommand):
    EVENT_FIELDS = ('eid', 'etype', 'price', 'kids', 'title',
                    'age_restricted', 'text', 'description',
                    'runtime', 'stage_theatre')

    PLACE_FIELDS = ('pid', 'ptype', 'title', 'city', 'address',
                    'latitude', 'longitude', 'url', 'text')

    def add_arguments(self, parser):
        parser.add_argument('source', help='source file')

    def handle(self, *args, **options):
        source = options.get('source', None)
        parser = XmlFeed(source)
        parser.parse()

        self.load_events(parser.get_events())
        self.load_places(parser.get_places())
        self.load_schedule(parser.get_schedule())

    def load_events(self, events):
        for event in events:
            kwargs = {field: event.get(field) for field in self.EVENT_FIELDS}
            db_event = Event.objects.create(**kwargs)

            db_event.gallery.clear()
            db_event.persons.clear()
            db_event.tags.clear()

            for image in event.get('gallery', []):
                db_image, _ = Image.objects.get_or_create(url=image)
                db_event.gallery.add(db_image)

            for person in event.get('persons', []):
                db_person, _ = Person.objects.get_or_create(name=person.get('name'),
                                                            role=person.get('role'))
                db_event.persons.add(db_person)

            for tag in event.get('tags', []):
                db_tag, _ = Tag.objects.get_or_create(name=tag)
                db_event.tags.add(db_tag)

    def load_places(self, places):
        for place in places:
            kwargs = {field: place.get(field) for field in self.PLACE_FIELDS}
            db_place = Place.objects.create(**kwargs)

            db_place.gallery.clear()
            db_place.phones.clear()
            db_place.metros.clear()
            db_place.tags.clear()
            db_place.work_times.clear()

            for image in place.get('gallery', []):
                db_image, _ = Image.objects.get_or_create(url=image)
                db_place.gallery.add(db_image)

            for phone in place.get('phones', []):
                db_phone, _ = Phone.objects.get_or_create(phone=phone)
                db_place.phones.add(db_phone)

            for metro in place.get('metros', []):
                db_metro, _ = Metro.objects.get_or_create(name=metro)
                db_place.metros.add(db_metro)

            for tag in place.get('tags', []):
                db_tag, _ = Tag.objects.get_or_create(name=tag)
                db_place.tags.add(db_tag)

            for work_time in place.get('work_times', []):
                db_work_time, _ = WorkTime.objects.get_or_create(time=work_time)
                db_place.work_times.add(db_work_time)

    def load_schedule(self, schedule):
        for session in schedule:
            try:
                event = Event.objects.get(eid=session.get('event'))
                place = Place.objects.get(pid=session.get('place'))
            except ObjectDoesNotExist:
                continue

            Schedule.objects.create(date=session.get('date'),
                                    time=session.get('time'),
                                    timetill=session.get('timetill'),
                                    event=event,
                                    place=place)
