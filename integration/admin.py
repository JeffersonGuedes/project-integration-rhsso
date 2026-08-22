from django.contrib import admin
from .models import Nome

@admin.register(Nome)
class NomeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address')
    list_filter = ('name', 'email', 'phone', 'address')
