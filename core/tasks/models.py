from django.db import models
from authentication.models import CustomUser
# Create your models here.

class Priority(models.Model):
  name= models.CharField(max_length=40)

  def __str__(self):
    return self.name



class task(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title=models.CharField(max_length=20, null=False)
    description=models.TextField(max_length=100, null=True, blank=True)
    date_limited=models.DateField()
    asignado_a=models.CharField(max_length=20, null=False)
    prioridad=models.ForeignKey(Priority, on_delete= models.DO_NOTHING)

    def __str__(self):
      return f"{self.title} - {self.user}"