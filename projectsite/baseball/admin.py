from django.contrib import admin
from django.contrib.admin import display
from .models import Position, Person, Club, Play


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ("description",)
    search_fields = ("description",)


@admin.register(Person)
class PositionAdmin(admin.ModelAdmin):
    list_display = ("lastname", "firstname", "height", "weight",)
    search_fields =("lastname", "firstname", "height", "weight",)

@admin.register(Club)
class PositionAdmin(admin.ModelAdmin):
    list_display = ("name", "coach", "dorm_latitude", "dorm_longitude",)
    search_fields = ("name", "coach", "dorm_latitude", "dorm_longitude",)

@admin.register(Play)
class PlayAdmin(admin.ModelAdmin):
    list_display = ("player","team","string_no","isActive",)

# Register your models here.
