from django.urls import path,re_path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    path('home/', views.index, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('blog/', views.blog, name = 'blogs'),
    path('contact/', views.contact, name = 'contact'),

]
