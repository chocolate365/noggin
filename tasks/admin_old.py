from django.contrib import admin
from .models import Task, List

admin.site.register(List)
admin.site.register(Task)
