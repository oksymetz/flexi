from django.urls import path
from . import views

app_name = 'profile'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('signin/', views.signin, name='signin'),
]
