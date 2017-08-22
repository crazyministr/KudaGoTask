from django.db import models


class Image(models.Model):
    url = models.URLField()  # max_length = 200 by default

    def __str__(self):
        return '%s' % self.url


class Person(models.Model):
    name = models.CharField(max_length=128)
    role = models.CharField(max_length=128)

    def __str__(self):
        return '%s %s' % (self.role, self.name)


class Tag(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return '%s' % self.name


class Phone(models.Model):
    phone = models.CharField(max_length=64)

    def __str__(self):
        return '%s' % self.phone


class Metro(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return '%s' % self.name


class WorkTime(models.Model):
    time = models.CharField(max_length=64)

    def __str__(self):
        return '%s' % self.time


class Event(models.Model):
    eid = models.PositiveIntegerField()

    price = models.NullBooleanField()
    kids = models.NullBooleanField()

    runtime = models.PositiveSmallIntegerField(blank=True, null=True)

    age_restricted = models.CharField(max_length=3, blank=True, null=True)
    etype = models.CharField(max_length=64, blank=True, null=True)
    title = models.CharField(max_length=128, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    description = models.CharField(max_length=1024, blank=True, null=True)
    stage_theatre = models.CharField(max_length=128, blank=True, null=True)

    gallery = models.ManyToManyField(Image)
    persons = models.ManyToManyField(Person)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return '%s | %s' % (self.eid, self.title)


class Place(models.Model):
    pid = models.PositiveIntegerField()

    ptype = models.CharField(max_length=64, blank=True, null=True)
    title = models.CharField(max_length=128, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=64, blank=True, null=True)
    address = models.CharField(max_length=128, blank=True, null=True)

    url = models.URLField(blank=True, null=True)

    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    gallery = models.ManyToManyField(Image)
    phones = models.ManyToManyField(Phone)
    metros = models.ManyToManyField(Metro)
    tags = models.ManyToManyField(Tag)
    work_times = models.ManyToManyField(WorkTime)

    def __str__(self):
        return '%s | %s' % (self.pid, self.title)


class Schedule(models.Model):
    date = models.DateTimeField()

    event = models.ForeignKey(Event)
    place = models.ForeignKey(Place)

    time = models.CharField(max_length=5)
    timetill = models.CharField(max_length=5, blank=True, null=True)

    def __str__(self):
        return 'e %s, p %s | %s' % (self.event, self.place, self.time)
