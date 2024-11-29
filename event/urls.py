from django.urls import path
from .views import *

urlpatterns = [
    path('landing/', index, name='landing'),
    path('posts/', CompetitionPosts.as_view(), name='posts'),
    path('my_teams/', MyTeams.as_view(), name='my_teams'),
    path('team_search/', SearchTeam.as_view(), name='team_search'),
    path('team_detail/<int:team_id>', TeamDetail.as_view(), name='team_detail'),
    path('posts/<int:competition_id>/create-team/', CreateTeamView.as_view(), name='create_team'),
    #path('teams/<int:pk>/submit/', SubmitTeamView.as_view(), name='submit_team'),

    path('posts/<int:post_id>/', index, name='detail'),
    path('register_or_create_team/<int:competition_id>/', index2, name="reg_or_create")#
]
