from django.contrib import admin

from .models import Agenda, Animal, Post, Reservation, Vet, WorkingTime


class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "created_date"]


class WorkingTimeAdmin(admin.ModelAdmin):
    list_display = ["vet", "start_datetime"]


admin.site.register(Post, PostAdmin)
admin.site.register(Reservation)
admin.site.register(Animal)
admin.site.register(Vet)
admin.site.register(WorkingTime, WorkingTimeAdmin)
admin.site.register(Agenda)
