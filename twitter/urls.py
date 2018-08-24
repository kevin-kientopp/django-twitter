from django.urls import path

from . import views

app_name = 'twitter'
urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:username>/', views.usertweets, name='usertweets'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('home', views.home, name='home'),
]
