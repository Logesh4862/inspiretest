from email.policy import default
from pyexpat import model
from statistics import mode
from unicodedata import category, name
from unittest.util import _MAX_LENGTH
from django.db import models



class Category(models.Model):
    name        =   models.CharField(max_length=250)
    is_active   =   models.BooleanField(default=True)
    record_data =   models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name


class CleanedData(models.Model):
    title       =   models.CharField(max_length=500)
    snippet     =   models.TextField()
    category    =   models.ForeignKey(Category, on_delete = models.SET_NULL, null=True)
    record_date =   models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title
