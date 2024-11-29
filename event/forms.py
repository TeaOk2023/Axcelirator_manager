from django import forms

from account.models import User
from .models import Team

class TeamCreationForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'members'] # Добавьте сюда все необходимые поля
        widgets = {
          'members': forms.CheckboxSelectMultiple()  #Или другой виджет, который вам подходит.
        }

