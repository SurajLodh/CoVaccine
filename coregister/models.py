from django.db import models

# Create your models here.

class User_data(models.Model):
    fname = models.TextField()
    lname = models.TextField()
    phone = models.TextField()
    email =models.TextField()
    age = models.TextField()
    blod = models.TextField()
    addres =models.TextField()
    state = models.TextField()
    city = models.TextField()
    zipcode = models.TextField()
    op_date = models.TextField()
    status = models.TextField()

class Contact(models.Model):
    unique_id = models.TextField()
    name = models.TextField()
    phone = models.TextField()
    email = models.TextField()
    query = models.TextField()




