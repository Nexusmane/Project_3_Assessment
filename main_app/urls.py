from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add_wiget/', views.WidgetCreate.as_view(), name='add_widget'),
]