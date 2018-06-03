from django.conf.urls import url

from core import views
from core.models import Upload


urlpatterns = [
    url(r'^clear/$', views.clear_database, name='clear_database'),
    url(r'^uploads/$', views.UploadView.as_view(), name='uploads_database'),
    # url('uploads/<int:year>/<int:month>/',UploadMonthArchiveView.as_view(month_format='%m'),
    #          name="post_archive_month"),
]