from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView


urlpatterns = [
  url(r'admin/', admin.site.urls),
  url(r'people/', include('people.urls')),
  url(r'^$', include('people.urls')),



]
