from django.db import models

# Create your models here.
#ORM = object relational mapping

class Book(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)

# Creating Company model
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type=models.CharField(max_length=100,choices=(("IT","IT"),
                                                  ("Non IT","Non IT")
                                                  ))
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name+" "+self.location




class Employee(models.Model):
    name = models.CharField(max_length=50)
    email_id = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=10)
    about = models.TextField()
    position = models.CharField(max_length=50,choices=(("manager","manager"),
                                                      ("software devloper","SD"),
                                                      ("Project Leader",'PL')
                                                      ))
    Company = models.ForeignKey(Company,on_delete = models.CASCADE)


