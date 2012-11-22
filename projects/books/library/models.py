# -*- coding: utf-8 -*-

from datetime import datetime
from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField('Имя', max_length=32)
    last_name = models.CharField('Фамилия', max_length=32)
    email = models.EmailField('Email', null=True, blank=True)

    def __unicode__(self):
        return u"%s %s" % (self.first_name, self.last_name)


class Book(models.Model):
    title = models.CharField('Название', max_length=128)
    authors = models.ManyToManyField('Author')
    publisher = models.ForeignKey('Publisher')
    publication_date = models.DateField('Дата выпуска', default=datetime.now())
    version = models.IntegerField('Издание', default=1, blank=True)

    def __unicode__(self):
        return self.title


class Publisher(models.Model):
    title = models.CharField('Название', max_length=32)
    address = models.TextField('Адрес')
    city = models.CharField('Город', max_length=64)
    country = models.CharField('Город', max_length=64)
    website = models.URLField('Адрес сайта')

    def __unicode__(self):
        return self.title


class PublisherOffices(models.Model):
    publisher = models.ForeignKey('Publisher')
    phone = models.CharField('Телефон', max_length=16)
    email = models.EmailField('Email')

    def __unicode__(self):
        return self.phone
