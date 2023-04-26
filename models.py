#Author: antlampas
#Date: 2023-04-23
#This work is licensed under the Creative Commons Attribution 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

from django.db import models

# Create your models here.

class RESTConsoles(models.Model):
    simulator = models.CharField(max_length=26)
    ip        = models.CharField(max_length=26)
    port      = models.CharField(max_length=26)
    models.UniqueConstraint(fields=['simulator','ip','port','username'],name='unique_RESTConsole')

class RESTCredentials(models.Model):
    simulator = models.CharField(max_length=26)
    username  = models.CharField(max_length=26)
    password  = models.CharField(max_length=26)