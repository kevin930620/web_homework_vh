from django.db import models

# Create your models here.
class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)
  age = models.IntegerField(default=50)

  

  def __str__(self):
    return f"{self.firstname} {self.lastname} {self.phone} {self.joined_date} {self.age} "

Type=(
  ("Grass","Grass"),
  ("Hard","Hard"),
  ("Mud","Mud"),
  ("Redsand","Redsand"),
)
class Field(models.Model):
  
  name = models.CharField(max_length=255)
  type = models.CharField(max_length=20,choices=Type,null=True)
  locate = models.CharField(max_length=255)

  def __str__(self):
    return f"{self.name} {self.type} {self.locate}"