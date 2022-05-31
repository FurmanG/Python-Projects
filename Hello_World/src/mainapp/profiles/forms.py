from cProfile import Profile
from django.forms import ModelForm
from .models import profiles


class ProfileForm(ModelForm):
  class Meta:
    model = profiles
    fields = '__all__'

