try:
    from parser.XmlParserBase import XmlParserBase
except ImportError:
    from XmlParserBase import XmlParserBase

import xml.etree.ElementTree as ET


class XmlFeed(XmlParserBase):
    def __init__(self, source_file):
        super().__init__()

        tree = ET.parse(source_file, parser=ET.XMLParser(encoding='utf-8'))
        root = tree.getroot()

        for child in root:
            self.xml_data[child.tag] = child

    def parse_events(self, events):
        for event in events:
            self._events.append({
                'uid': self.convert_to_int(event.attrib.get('id', None)),
                'etype': self.convert_to_str(event.attrib.get('type', None)),
                'price': self.convert_to_bool(event.attrib.get('price', None)),
                'kids': self.convert_to_bool(event.attrib.get('kids', None)),
                'title': self.convert_to_str(event.find('title')),
                'age_restricted': self.convert_to_str(event.find('age_restricted')),
                'text': self.convert_to_str(event.find('text')),
                'description': self.convert_to_str(event.find('description')),
                'gallery': self.convert_to_list(event.find('gallery'), attr='href'),
                'runtime': self.convert_to_int(event.find('runtime')),
                'stage_theatre': self.convert_to_str(event.find('stage_theatre')),
                'persons': self.convert_to_dict_in_list(event.find('persons')),
                'tags': self.convert_to_list(event.find('tags')),
            })

    def parse_places(self, places):
        for place in places:
            self._places.append({
                'uid': self.convert_to_int(place.attrib.get('id', None)),
                'ptype': self.convert_to_str(place.attrib.get('type', None)),
                'title': self.convert_to_str(place.find('title')),
                'city': self.convert_to_str(place.find('city')),
                'address': self.convert_to_str(place.find('address')),
                # 'latitude': self.convert_to_float(place.find('coordinates').attrib['latitude']),
                # 'longitude': self.convert_to_float(place.find('coordinates').attrib['longitude']),
                'phones': self.convert_to_list(place.find('phones')),
                'metros': self.convert_to_list(place.find('metros')),
                'url': self.convert_to_str(place.find('url')),
                'gallery': self.convert_to_list(place.find('gallery'), attr='href'),
                'tags': self.convert_to_list(place.find('tags')),
                'text': self.convert_to_str(place.find('text')),
                'work_times': self.convert_to_list(place.find('work_times')),
            })
            coordinates = place.find('coordinates')
            if coordinates:
                self._places[-1]['latitude'] = self.convert_to_float(coordinates.attrib['latitude'])
                self._places[-1]['longitude'] = self.convert_to_float(coordinates.attrib['longitude'])

    def parse_schedule(self, schedule):
        for session in schedule:
            self._schedule.append({
                'date': self.convert_to_date(session.attrib.get('date', None)),
                'event': self.convert_to_int(session.attrib.get('event', None)),
                'place': self.convert_to_int(session.attrib.get('place', None)),
                'time': self.convert_to_str(session.attrib.get('time', None)),
                'timetill': self.convert_to_str(session.attrib.get('timetill', None)),
            })


if __name__ == '__main__':
    parser = XmlFeed('/home/anton/Projects/KudaGoTask/feed/test.xml')
    parser.parse()
    e = parser.get_events()
    p = parser.get_places()
    s = parser.get_schedule()
    print('Events =', len(e))
    print('Places =', len(p))
    print('Sessions =', len(s))

    for ee in e:
        print(ee['uid'], end=' ')

    print()
    for pp in p:
        print(pp['uid'], end='\n\n')
    # for ss in s:
    #     print(ss, end='\n\n')
