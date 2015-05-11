# -*- coding: utf-8 -*-
from django.db import models


class CurriculumVitae(models.Model):
    first_name = models.CharField('ime', max_length=30)
    last_name = models.CharField('prezime', max_length=30)
    address_1 = models.CharField('adresa prebivališta', max_length=100, blank=True, null=True)
    address_2 = models.CharField('adresa boravišta', max_length=100, blank=True, null=True)
    email = models.EmailField('e-mail')
    web = models.URLField('web (pref. LinkedIn)', blank=True, null=True)
    born = models.PositiveIntegerField('godina rođenja')
    phone = models.CharField('broj mobitela', max_length=20, blank=True, null=True)
    college = models.CharField('fakultet', max_length=100)
    course = models.CharField('Smjer/Godina', max_length=100)
    discipline = models.CharField('natjecateljska disciplina na Elektrijadi', max_length=100, blank=True, null=True)

    activities = models.TextField('aktivnosti na fakultetu', max_length=1000, blank=True, null=True)
    education = models.TextField('dodatno školovanje', max_length=1000, blank=True, null=True)

    languages = models.CharField('jezici', max_length=100, blank=True, null=True, help_text='Odvojite ih s razmakom.')

    skills = models.TextField('Znanja/Vještine', max_length=1000, blank=True, null=True)
    experience = models.TextField('radno iskustvo', max_length=1000, blank=True, null=True)
    about = models.TextField('ukratko o sebi', max_length=1000, blank=True, null=True)

    graduation = models.PositiveIntegerField('planirana godina diplomiranja', blank=True, null=True)

    preferences = models.TextField('preferirani posao', max_length=1000, blank=True, null=True)
    expectations = models.TextField('očekivanja', max_length=1000, blank=True, null=True)

    created = models.DateTimeField('vrijeme kreiranja', auto_now_add=True)
    visible = models.BooleanField('vidljivost', default=True)

    @property
    def full_name(self):
        "Returns the person's full name."
        return u'%s %s' % (self.first_name, self.last_name)

    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = 'životopis'
        verbose_name_plural = 'životopisi'

    def __unicode__(self):
        return self.full_name
