from django.contrib import admin

from account.models import User
from .models import Competition, Team, SportClass
from django import forms

@admin.register(Competition)
class CompetitionAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'description',
        'start_time',
        'end_time',
    ]

    list_filter = ['start_time', 'end_time']


class TeamCreationForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'members', 'competition']
        widgets = {
          'members': forms.CheckboxSelectMultiple(),
          'competition': forms.Select()
        }



@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'leader_id', 'competition', 'get_member_count', 'is_draft')  # Add fields to display
    list_filter = ('competition', 'is_draft')  # Add fields to filter by

    def get_member_count(self, obj):
        return obj.members.count()

    get_member_count.short_description = 'Number of Members'

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "members":
            kwargs["queryset"] = User.objects.all()
            kwargs['widget'] = forms.CheckboxSelectMultiple()
            return forms.ModelMultipleChoiceField(**kwargs)
        return super().formfield_for_manytomany(db_field, request, **kwargs)


@admin.register(SportClass)
class SportClassAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]