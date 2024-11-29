from datetime import datetime, timezone, time
from django.urls import reverse
from django.conf import settings
from django.db import models


class SportClass(models.Model):
    name = models.CharField(max_length=150, unique=True, null=False, default='')

    def __str__(self):
        return self.name


class Competition(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    registration_deadline = models.DateTimeField(null=True)
    location = models.CharField(max_length=200) # Можно подробнее, но не сейчас
    sport_name = models.ForeignKey(SportClass, on_delete=models.CASCADE)

    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


    class Meta:
        ordering = ['start_time']


        # permissions = [
        #     ("can_manage_competitions", "Can manage competitions"),
        # ]

    #Поменяю на choose
    @property
    def event_status(self):
        status = None

        present = datetime.now().timestamp()
        deadline = self.registration_deadline.timestamp()
        past_deadline = (present > deadline)

        if past_deadline:
            status = 'Finished'
        else:
            status = 'Ongoing'

        return status


class Team(models.Model):
    name = models.CharField(max_length=200, null=False)
    leader_id = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, on_delete=models.CASCADE, related_name='leader')
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='members')
    # One to One наверное нужно (команда только на 1 мероприятие)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE, related_name='competition')
    is_search_members = models.BooleanField(default=False)
    is_draft = models.BooleanField(default=True)  # Черновик или уже нет

    #created_at = models.DateTimeField(auto_now_add=True)
    #2updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('team_detail', args=[str(self.id)])

    @property
    def get_member_count(self):
        return self.members.count()  # Возвращает количество участников


class TeamRegistration(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='submissions')
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE, related_name='submissions')
    is_registered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return str(self.competition) + '----' + str(self.team)


