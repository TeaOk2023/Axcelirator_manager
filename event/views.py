from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Competition, Team
from .forms import *
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth import get_user

def index(request):
    return render(request, 'event/landing.html')

class CompetitionPosts(ListView):
    model = Competition
    template_name = "event/posts.html"
    context_object_name = "competitions"

    def get_queryset(self):
        set = Competition.objects.all()
        current_user = self.request.user
        if (current_user.id):
            teams = Team.objects.all().filter(members=current_user)

            for comp in set:
                t = False
                for team in teams:
                    if team.competition == comp:
                        t=True
                comp.registered = t

        return set


class MyTeams(LoginRequiredMixin, ListView):
    model = Team
    template_name = "event/my_teams.html"
    context_object_name = "teams"

    def get_queryset(self):
        return Team.objects.all().filter(members=self.request.user) # пока так


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CreateTeamView(LoginRequiredMixin, CreateView):
    model = Team
    form_class = TeamCreationForm
    template_name = 'event/team_create.html'

    def form_valid(self, form):
        team = form.save(commit=False)
        team.leader_id = self.request.user
        team.competition_id = Competition.objects.get(pk=self.kwargs['competition_id']).id # Получаем competition_id из URL
        team.save()
        team.members.add(self.request.user)
        team.members.add(*form.cleaned_data['members'])

        return redirect(team.get_absolute_url())


class TeamDetail(LoginRequiredMixin, UpdateView):
    model = Team
    form_class = TeamCreationForm
    template_name = "event/team_detail.html"
    context_object_name = "team"
    pk_url_kwarg = "team_id"

    def get_success_url(self):
        return self.object.get_absolute_url()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['participation_form'] = ParticipationRequestForm()  # Добавьте форму заявки
        return context

    def form_valid(self, form):
        if not self.object.is_draft:
            messages.warning(self.request, 'Изменить команду после отправки заявки нельзя!')
            return redirect(self.object.get_absolute_url())
        return super().form_valid(form)


class SearchTeam(LoginRequiredMixin, ListView):
    model = Team
    template_name = "event/search_team.html"
    context_object_name = "teams"

    def get_queryset(self):
        return Team.objects.all().filter(is_search_members = True) # пока так


class CompetitionDetail(LoginRequiredMixin, DetailView):
    model = Competition
    #form_class = TeamCreationForm
    template_name = "event/competition_detail.html"
    context_object_name = "competition"
    pk_url_kwarg = "competition_id"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teams'] = Team.objects.all().filter(competition=context['object'].id)

        return context

