from django.urls import path

from . import views

app_name = 'twitter'
urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('log_in', views.log_in, name='log_in'),
    path('home', views.home, name='home'),
]
