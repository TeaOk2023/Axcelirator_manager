from .models import User
import datetime

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, AuthenticationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input'}), label='Логин')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input'}), label='Пароль')

    class Meta:
        model = get_user_model()
        fields = ('username', 'password')


class RegisterUserForm(UserCreationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input'}), label='Nickaname')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input'}), label='Пароль')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input'}), label='Повтор пароля')

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')
        labels = {
            'email': 'E-mail',
        }
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-input'}),
        }

    def clean_email(self) -> forms.EmailField:
        #Метод-валидатор проверяет уникальность электронной почты.
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError('Такой E-mail уже существует')

        return email


class ProfileUserForm(forms.ModelForm):

    username = forms.CharField(disabled=True, widget=forms.TextInput(attrs={'class': 'form-input'}), label='Nickaname')
    # id = forms.CharField(disabled=True, widget=forms.TextInput(attrs={'class': 'form-input'}), label='ID')
    email = forms.CharField(disabled=True, required=False, widget=forms.TextInput(attrs={'class': 'form-input'}), label='E-mail')
    this_year = datetime.date.today().year
    date_birth = forms.DateTimeField(widget=forms.SelectDateWidget(years=tuple(range(this_year-5, this_year-100, -1))),
                                     label='Дата рождения')

    class Meta:
        """
        Вложенный класс предназначен для корректной обработки данных.

        Атрибуты:\n
        fields - tuple - поля, которые требуется отображать;\n
        labels - dict - метки для полей;\n
        widgets - dict - CSS-виджеты полей.
        """
        model = get_user_model()
        fields = ('username', 'email',  'date_birth', 'first_name', 'last_name')
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
        }


class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input'}), label='Старый пароль')
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input'}), label='Новый пароль')
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input'}), label='Подтверждение пароля')