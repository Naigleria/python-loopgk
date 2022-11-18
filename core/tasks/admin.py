from django.contrib import admin
from .models import Priority, task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
  list_display=('id','user','title', 'prioridad')
  search_fields=('id','user','title','prioridad')

class PriorityAdmin(admin.ModelAdmin):
  list_display=('id','name')

admin.site.register(task, TaskAdmin)
admin.site.register(Priority, PriorityAdmin) 