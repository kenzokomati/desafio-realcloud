from django.db import models

class Pessoa(models.Model):
  name = models.CharField(max_length=100)  
  id = models.AutoField(primary_key=True)  
  birthdate = models.DateField()  
  quantity = models.DecimalField(max_digits=10, decimal_places=2)  

  def __str__(self):
    return self.name
