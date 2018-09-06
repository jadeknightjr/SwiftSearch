from django.db import models

# Create your models here.
class Team(models.Model):
  teamName = models.CharField(max_length=250)
  department = models.CharField(max_length=50)

  def __str__(self):
    return self.teamName + ' - ' + self.department

class Employee(models.Model):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  alma_mater = models.CharField(max_length=100, default="James Madison University")
  position = models.CharField(max_length=100)
  location = models.CharField(max_length=100)
  teamID = models.ForeignKey(Team, on_delete=models.CASCADE)
  COE = models.CharField(max_length=250)
  skills = models.CharField(max_length=250)
  employeeID = models.CharField(max_length=10)
  parentID = models.CharField(max_length=10)

  def __str__(self):
    return self.first_name + ' ' + self.last_name 


