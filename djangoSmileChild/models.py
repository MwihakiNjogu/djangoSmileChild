from django.db import models


class NGO(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    city = models.CharField(max_length=30, blank=False, null=False)
    country = models.CharField(max_length=30, blank=False, null=False)
    sdgs = models.CharField(max_length=30, blank=False, null=False)
    directors = models.IntegerField(blank=False, null=False)
    members = models.IntegerField(blank=False, null=False)
    funding = models.CharField(max_length=30, blank=False, null=False)

    def __str__(self):
        self.name