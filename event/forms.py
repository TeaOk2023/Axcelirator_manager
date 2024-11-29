from django import forms

from account.models import User
from .models import Team

class TeamCreationForm(forms.ModelForm):
    members = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'js-selectize'}),  # Для использования selectize.js
        required=False,  # Делаем поле необязательным
    )

    class Meta:
        model = Team
        fields = ['name', 'members'] # Добавьте сюда все необходимые поля



