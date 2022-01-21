from django.shortcuts import render
from .models import
from django.views.generic import CreateView

# Create your views here.

def index(request):
     = .object.all()
     return render(request, 'index.html', {'': })


class Create(CreateView):
    model = 
    fields = '__all__'
    success_url = '/'