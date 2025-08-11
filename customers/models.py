from django.db import models

# Create your models here.

class Customer(models.Model):
    cid = models.CharField(max_length=4)
    cname = models.CharField(max_length=50)
    address = models.name = models.CharField(max_length=50)

    def __str__(self):
        return self.cname
    
class Blog(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField(max_length=200)

    def __str__(self):
        return self.title 
    
class Comment(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)    
    comment = models.CharField(max_length=100)

    def __str__(self):
        return self.comment
    
