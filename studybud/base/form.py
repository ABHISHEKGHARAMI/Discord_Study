from django.forms import ModelForm
from .models import Room


# creating the form class
class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'