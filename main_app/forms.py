from django.forms import ModelForm
from .models import Widget

def WidgetForm(ModelForm):
    class Meta:
        model = Widget
        fields = ['description', 'quantity']

