from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from account.forms import LoginForm, RegisterUserForm, ProfileUserForm, UserPasswordChangeForm


class LoginUser(LoginView):
    form_class = LoginForm
    template_name = 'account/login.html'
    extra_context = {"title": "Login"}

    #def get_success_url(self):
        # перенаправление после авторизации сильнее чем в settings
        #return reverse_lazy('home')


class RegisterUser(CreateView):

    form_class = RegisterUserForm
    template_name = 'account/register.html'
    extra_context = {'title': 'Регистрация'}
    success_url = reverse_lazy('account:login') #redirect after логина


class ProfileUser(LoginRequiredMixin, UpdateView):

    model = get_user_model()
    form_class = ProfileUserForm
    template_name = 'account/profile.html'
    extra_context = {
        'title': 'Профиль пользователя',
        #'default_image': settings.DEFAULT_USER_IMAGE,
    }

    def get_success_url(self):
        return reverse_lazy('account:profile')

    def get_object(self, queryset=None):
        return self.request.user # текущий пользователь


class UserPasswordChange(PasswordChangeView):
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy('account:password_change_done')
    template_name = 'account/password_change_form.html'
    extra_context = {'title': 'Смена пароля'}