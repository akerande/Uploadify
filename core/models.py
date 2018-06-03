# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import date
from django.core.urlresolvers import reverse


def content_file_name(instance,filename):
    today = date.today()
    today_path = today.strftime("%Y/%m/%d")
    if instance.file.name.split('.')[1] == 'mp4':
        return 'uploads/{1}/videos/{0}'.format(filename,today_path)
    elif instance.file.name.split('.')[1] == 'jpg':
        return 'uploads/{1}/photos/{0}'.format(filename,today_path)


class Upload(models.Model):
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to=content_file_name)
    uploaded_at = models.DateField(auto_now_add=True)

    class Meta:
        get_latest_by = 'uploaded_at'

    def get_absolute_url(self):
        return reverse('upload-detail', kwargs={'pk': self.pk})