__author__ = 'nhaines'

from neo4django.db import models


class Person(models.NodeModel):
    first = models.StringProperty()
    last = models.StringProperty()


class User(Person):
    username = models.StringProperty(null=False)
    email = models.EmailProperty()


class Asset(models.NodeModel):
    sha1 = models.StringProperty(min_length=20, max_length=20, unique=True)
    paths = models.StringArrayProperty()
    title = models.StringProperty()


