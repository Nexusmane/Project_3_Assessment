from django.shortcuts import render
from .models import Widget
from django.views.generic import CreateView

# Create your views here.

def index(request):
     widgets = Widget.objects.all()
     return render(request, 'index.html', { 'widgets': widgets })


class WidgetCreate(CreateView):
    model = Widget
    fields = '__all__'
    success_url = '/'