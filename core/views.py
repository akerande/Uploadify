# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import time
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import View
from .forms import UploadForm
from core.models import Upload
from django.views.generic.dates import MonthArchiveView

class UploadView(View):
    def get(self, request):
        upload_list = Upload.objects.all()
        return render(self.request, 'core/index.html', {'uploads': upload_list})

    def post(self, request):
        time.sleep(1)  # to delay the process so you can see the progress bar testing locally.
        form = UploadForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            upload_form = form.save()
            data = {'is_valid': True, 'name': upload_form.file.name, 'url': upload_form.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)


class UploadMonthArchiveView(MonthArchiveView):
    queryset = Upload.objects.all()
    date_field = "posted"
    allow_future = True


def clear_database(request):
    for upload in Upload.objects.all():
        upload.file.delete()
        upload.delete()
    return redirect(request.POST.get('next'))