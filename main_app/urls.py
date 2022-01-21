from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add___/', views.___Create.as_view(), name='add_____'),
]