from django.forms import ModelForm
from .models import Room

# generate a form with metadata that is already modeled in the room model
class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__' # give all fields from the room