from django.urls import path
from . import views

app_name = 'profile'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('signin/', views.signin, name='signin'),
    path('drafts/', views.drafts, name='drafts'),
    path('logout/', views.log_out, name='log_out'),
]
