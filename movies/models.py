from django.db import models

class Movie(models.Model):

    title = models.CharField("Movie Title", max_length=100, null=True, blank=False)
    synopsys = models.CharField("Synopsys", max_length=100, null=True, blank=True)
    release_year = models.CharField("Release Year", max_length=100, null=True, blank=True)
    duration = models.IntegerField("Duration", default=10, null=True, blank=True)