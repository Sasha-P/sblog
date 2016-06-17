from django.contrib import admin
from .models import Group, Student


class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'monitor')
    list_filter = ('name', 'monitor')
    search_fields = ('name',)
    ordering = ['name', 'monitor']

admin.site.register(Group, GroupAdmin)
admin.site.register(Student)
