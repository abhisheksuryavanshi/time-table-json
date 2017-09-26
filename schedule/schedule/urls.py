from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url
from django.contrib import admin
from tt import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^days/', views.daylist.as_view()),
    url(r'^days/(?P<day_id>[1-5])/', views.getmsg, name='getmsg'),
    #url(r'^(?P<day_id>[0-9]+)/$', views.daylist.as_view(), name ='detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
