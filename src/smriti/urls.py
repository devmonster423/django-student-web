from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.indexPage, name='index'),
    url(r'^home/', views.homePage, name='home'),
    url(r'^browse/', views.browsePage, name='browse'),
    url(r'^search/', views.searchPage, name='search'),
    url(r'^testimonial/(?P<id>[0-9]+)', views.testimonial, name='testimonial'),
    url(r'^write/', views.WritePage.as_view(), name='write'),
    ]
