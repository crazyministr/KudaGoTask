from django.db import models


class Event(models.Model):
    uid = models.PositiveIntegerField(),

    price = models.NullBooleanField(),
    kids = models.NullBooleanField(),

    runtime = models.PositiveSmallIntegerField(),

    age_restricted = models.CharField(max_length=3, blank=True, null=True),
    etype = models.CharField(max_length=64, blank=True, null=True),
    title = models.CharField(max_length=128, blank=True, null=True),
    text = models.CharField(max_length=1024, blank=True, null=True),
    description = models.CharField(max_length=1024, blank=True, null=True),
    stage_theatre = models.CharField(max_length=128, blank=True, null=True),

    # gallery ManyToMany
    # persons ManyToMany
    # tags ManyToMany

    def __str__(self):
        return '%s | %s' % (self.uid, self.title)


class Place(models.Model):
    uid = models.PositiveIntegerField(),

    ptype = models.CharField(max_length=64, blank=True, null=True),
    title = models.CharField(max_length=128, blank=True, null=True),
    text = models.CharField(max_length=1024, blank=True, null=True),
    city = models.CharField(max_length=64, blank=True, null=True),
    address = models.CharField(max_length=128, blank=True, null=True),

    url = models.URLField(blank=True, null=True),  # max_length = 200

    latitude = models.FloatField()
    longitude = models.FloatField()

    # gallery ManyToMany
    # phones ManyToMany
    # metros ManyToMany
    # tags ManyToMany
    # work_times ManyToMany


class Schedule(models.Model):
    date = models.DateTimeField()

    event = models.ForeignKey(Event)
    place = models.ForeignKey(Place)

    time = models.CharField(max_length=5),
    timetill = models.CharField(max_length=5, blank=True, null=True),

    def __str__(self):
        return 'e %s, p %s | %s' % (self.event, self.place, self.time)