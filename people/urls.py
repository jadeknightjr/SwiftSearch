from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
  # /people/
    url(r'^$', views.index, name='index'),

   # /people/71
   url(r'^teams/(?P<id>\d+)/$', views.teamview, name='teamview'),

   url(r'^employees/(?P<id>\d+)/$', views.employees, name='employees'),

   url(r'^search/(?P<search>.+?)/$', views.search, name='search'),

   url(r'^teams-list/$', views.teamlist, name='teamlist'),

   url(r'^employees-list/$', views.employeelist, name='employeelist'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

