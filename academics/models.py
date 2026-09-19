from django.db import models
from django.db import models
# Create your models here.



class SchoolClass(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Section(models.Model):
    name = models.CharField(max_length=10)
    
    school_class = models.ForeignKey(
        SchoolClass,
        on_delete=models.CASCADE,
        related_name="sections"
    )
    
    def __str__(self):
        return f"{self.school_class} - {self.name}"