from django.forms import ModelForm
from django.shortcuts import render, redirect
from .models import Widget
from django.views.generic import CreateView
from .forms import WidgetForm

# Create your views here.

def index(request):
     widgets = Widget.objects.all()
     widget_form = WidgetForm()
     return render(request, 'index.html', { 'widgets': widgets, 'widget_form': widget_form})

def add_widget(request):
    widget_form = WidgetForm(request.POST)
    widget_form.save()
    return redirect('/')

def delete_widget(request, widget_id):
    Widget.objects.get(id=widget_id).delete()
    return redirect('/')