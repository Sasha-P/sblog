from django.core.urlresolvers import reverse
from django.db import models


class Student(models.Model):
    last_name = models.CharField(verbose_name=u'Last name', max_length=30)
    first_name = models.CharField(verbose_name=u'First name', max_length=30)
    patronymic = models.CharField(verbose_name=u'Patronymic', max_length=30)
    birthday = models.DateField(verbose_name=u'Birthday')
    group = models.ForeignKey('Group', verbose_name=u'Group')

    def __str__(self):
        return '%s %s %s' % (self.last_name, self.first_name, self.patronymic)

    def get_absolute_url(self):
        return reverse('studdb:student_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = u'Student'
        verbose_name_plural = u'Students'


class Group(models.Model):
    name = models.CharField(verbose_name=u'Group name', max_length=30)
    monitor = models.ForeignKey('Student', verbose_name=u'Monitor', related_name="groups", blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('studdb:group_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = u'Group'
        verbose_name_plural = u'Groups'
