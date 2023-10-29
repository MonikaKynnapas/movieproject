from django.db import models
import datetime

from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import (MinLengthValidator, MinValueValidator, MaxValueValidator)


# Create your models here.


class Country(models.Model):
    common = models.CharField(max_length=100)
    official = models.CharField(max_length=100)
    capital = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    subregion = models.CharField(max_length=100, null=True, blank=True)
    flag = models.CharField(max_length=100)
    map = models.CharField(max_length=100)


    class Meta:
        """ Default result ordering """
        ordering = ['common']
        verbose_name_plural = 'countries'

    def country_info(self):
        """Show simple book info """
        return f'{self.common}, {self.official}'

    def __str__(self):
        """ Admin page show info """
        return self.common

class Movie(models.Model):
    title = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    imdb = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    poster = models.CharField(max_length=100)

    class Meta:
        """ Default result ordering """
        ordering = ['title']
        verbose_name_plural = 'movies'

    def country_info(self):
        """Show simple book info """
        return f'{self.title}, {self.year}'

    def __str__(self):
        """ Admin page show info """
        return self.title