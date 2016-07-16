from django.conf.urls import url
from . import views
from views import upload

app_name = 'bgextr'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^upload$',upload, name='upload')
    ]