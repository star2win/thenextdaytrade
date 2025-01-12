from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('db/', views.db, name='db'),
    path('login/', views.login_view, name='login'),
] 