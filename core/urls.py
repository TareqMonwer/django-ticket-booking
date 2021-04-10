from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('seats/', views.seat_planner, name='seat_planner'),
    path('pay/', views.pay, name='pay'),
]