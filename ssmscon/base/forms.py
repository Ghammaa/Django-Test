from django.db.models import fields
from django.db.models.base import Model
from django.forms import ModelForm
from .models import Room, Student

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'

class EditProfile(ModelForm):
    class Meta:
        model = Student
        fields = [
            'name', 'age', 'speciality', 'profpic'
        ]