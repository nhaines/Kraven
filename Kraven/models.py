__author__ = 'nhaines'

from django.db import models


class Asset(models.Model):
    sha1 = models.CharField(max_length=20, blank=False, null=False, unique=True)
    md5 = models.CharField(max_length=16, blank=False, null=False, unique=True)

    def __unicode__(self):
        return unicode(self.sha1)


class Path(models.Model):
    asset = models.ForeignKey(Asset)
    path = models.CharField(max_length=255, blank=False, null=False, unique=True)

    def __unicode__(self):
        return unicode(self.url)