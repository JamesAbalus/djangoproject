from django.db import models
from django.utils import timezone

class BaseModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
        
class Position(BaseModel):
    description = models.CharField(max_length=100)
    
    # It will display the description instead of Position object(n)
    def __str__(self):
        return f"{self.description}"
    
class Person(BaseModel):
    lastname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True, max_length=100)
    height = models.DecimalField(max_digits=10, decimal_places=5, null=True)
    weight = models.DecimalField(max_digits=10, decimal_places=5, null=True)
    
    # It will display the lastname, firstname instead of Person object(n)
    def __str__(self):
        return f"{self.lastname}, {self.firstname}"
    
class Club(BaseModel):
    name = models.CharField(max_length=100)
    coach = models.ForeignKey(Person, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    dorm_latitude = models.DecimalField(max_digits=22, decimal_places=16, null=True, blank=True)
    dorm_longitude = models.DecimalField(max_digits=22, decimal_places=16, null=True, blank=True)
    team_pic = models.ImageField(default="defaultimg.png", null=True, blank=True, verbose_name="Team Image")

    def __str__(self):
        return f"{self.name}"
