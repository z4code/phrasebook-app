# main/urls.py

from django.urls import path
# from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('view/category/<slug:slug>/', views.view_category, name='view_category'),
]