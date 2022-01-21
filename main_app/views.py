from django.shortcuts import render
from .models import Widget
from django.views.generic import CreateView
from .forms import WidgetForm

# Create your views here.

def index(request):
     widgets = Widget.objects.all()
     return render(request, 'index.html', {'widgets': widgets})

class WidgetCreate(CreateView):
    model = Widget
    fields = '__all__'
    success_url = '/'

def widget_form(request):
    widget_form = WidgetForm()
    return render(request, 'index.html', {'widget_form': widget_form})