from django.contrib import admin
from .models import Actress
# Register your models here.

@admin.register(Actress)
class ActressAdmin(admin.ModelAdmin):
    list_display =("id","name","profile_path")