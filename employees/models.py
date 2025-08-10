from django.db import models

# Create your models here.
class Employee(models.Model):
    eid = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Employees"
        ordering = ['name']