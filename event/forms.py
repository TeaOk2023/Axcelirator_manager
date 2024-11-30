from django import forms
from django.contrib.auth import get_user_model

from Axcelirator_manager import settings
from account.models import User
from .models import Team

class TeamCreationForm(forms.ModelForm):
    members = forms.ModelMultipleChoiceField(
        #print(User.objects.all().filter(id__exact=settings.AUTH_USER_MODEL)),
        queryset=get_user_model().objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'js-selectize'}),  # Для использования selectize.js
        required=False,  # Делаем поле необязательным
    )

    class Meta:
        model = Team
        fields = ['name', 'leader_id', 'members'] # Добавьте сюда все необходимые поля
