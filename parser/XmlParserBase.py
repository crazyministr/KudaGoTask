from datetime import datetime


class XmlParserBase(object):
    def __init__(self):
        self.xml_data = {
            'events': None,
            'places': None,
            'schedule': None
        }

        self._events = []
        self._places = []
        self._schedule = []

    def parse(self):
        self.parse_events(self.xml_data['events'])
        self.parse_places(self.xml_data['places'])
        self.parse_schedule(self.xml_data['schedule'])

    def parse_events(self, events):
        raise NotImplementedError

    def parse_places(self, places):
        raise NotImplementedError

    def parse_schedule(self, schedule):
        raise NotImplementedError

    def get_events(self):
        return self._events

    def get_places(self):
        return self._places

    def get_schedule(self):
        return self._schedule

    @staticmethod
    def get_text(x):
        try:
            return x.text
        except AttributeError:
            return x

    @staticmethod
    def convert_to_int(x):
        x = XmlParserBase.get_text(x)
        try:
            return int(x)
        except (ValueError, TypeError):
            return None

    @staticmethod
    def convert_to_float(x):
        x = XmlParserBase.get_text(x)
        try:
            return float(x)
        except (ValueError, TypeError):
            return None

    @staticmethod
    def convert_to_str(x):
        x = XmlParserBase.get_text(x)
        return str(x) if x is not None else x

    @staticmethod
    def convert_to_bool(x):
        x = str(XmlParserBase.get_text(x)).lower()
        if x in ('true', 'false'):
            return (False, True)[x == 'true']
        return None

    @staticmethod
    def convert_to_date(x):
        try:
            return datetime.strptime(x, '%Y-%m-%d')
        except (ValueError, TypeError):
            return None

    @staticmethod
    def convert_to_list(data, attr=None):
        if data is None:
            return []

        res = []
        for tag in data:
            res.append(tag.attrib.get(attr, None) if attr else tag.text)

        return res

    @staticmethod
    def convert_to_dict_in_list(data):
        if data is None:
            return []

        res = []
        for tag in data:
            res.append({t.tag: t.text for t in tag})

        return res
