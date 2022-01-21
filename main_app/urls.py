from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('add_wiget/', views.WidgetCreate.as_view(), name='add_widget'),
]