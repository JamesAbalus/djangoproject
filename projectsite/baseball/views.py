from django.shortcuts import render, redirect

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView

from baseball.models import Position, Person, Club, Play, Match

class HomePageView(ListView):
    model = Play
    context_object_name = 'play'
    template_name = "landingpage/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ClubView(ListView):
    model = Club
    context_object_name = 'club'
    template_name = "club.html"

    # This method is used to populate a dictionary to use as the template context.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header_text'] = 'List of Teams'
        return context

    # Used by ListViews - it determines the list of objects that you want to display. 
    # By default, it will just give you all for the model you specify.
    def get_queryset(self, *args, **kwargs):
        qs = super(ClubView, self).get_queryset(*args, **kwargs)
        return qs

class PlayerView(ListView):
    model = Play
    context_object_name = 'play'
    template_name = "player.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header_text'] = 'List of Players'
        return context

    def get_queryset(self, *args, **kwargs):
        qs = super(PlayerView, self).get_queryset(*args, **kwargs)
        return qs

class MatchView(ListView):
    model = Match
    context_object_name = 'match'
    template_name = "match.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header_text'] = 'List of Matches'
        return context

    def get_queryset(self, *args, **kwargs):
        qs = super(MatchView, self).get_queryset(*args, **kwargs)
        return qs

