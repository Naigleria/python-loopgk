from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
  user=serializers.SerializerMethodField('get_user')
  priority = serializers.SerializerMethodField('get_priority')
  class Meta:
    model = Task
    fields=['user', 'id', 'title', 'description', 'asignado_a', 'priority']

  def get_user(self, Task):
    return{
      "user_id": Task.user.pk,
      "user_full_name": Task.user.get_full_name(),
    }
  def get_priority(self, Task):
    return{
      "priority_id": Task.priority.pk,
      "priority_name": Task.priority.name
    }



'''class TaskSerializer(serializers.ModelSerializer):
  class Meta:
    model = Task
    fields='__all__'
    '''