from django.contrib import admin
from .models import Task
from .models import Tasklist

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass


@admin.register(Tasklist)
class TasklistAdmin(admin.ModelAdmin):
    pass
# Register your models here.
