from django.db import models

# Create your models here.

class Tasklist(models.Model):
  title = models.CharField(max_length=200)

  def __str__(self):
    return self.title







# Create your models here.

class Task(models.Model):
  title = models.CharField(max_length=200)
  completed = models.BooleanField(default=False, blank=True, null=True)
 # tasklist = models.ForeignKey(Tasklist, on_delete=models.CASCADE, default=None)
      
  def __str__(self):
    return self.title





  