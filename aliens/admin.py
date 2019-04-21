from django.contrib import admin
from .models        import Alien, State



class AlienAdmin(admin.ModelAdmin):
    list_display  = ['city', 'state', 'date']
    search_fields = ['city']

class StateAdmin(admin.ModelAdmin):
    list_display  = ['initials', 'name', 'count']
    search_fields = ['initials']

admin.site.register(Alien, AlienAdmin)
admin.site.register(State, StateAdmin)
