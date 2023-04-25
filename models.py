from django.db import models

# Create your models here.

class Grids(models.Model):
    name = models.CharField(max_length=26)
    models.UniqueContraint(fields=['name'],name='unique_grid_name')

class Simulators(models.Model):
    name = models.CharField(max_length=26)
    models.UniqueContraint(fields=['name'],name='unique_simulator_name')

class Regions(models.Model):
    regionName = models.CharField(max_length=26)
    simulator  = models.CharField(max_length=26)
    grid       = models.CharField(max_length=26)
    models.UniqueConstraint(fields=['regionName','simulator'],name='unique_region_in_grid_simulator')

class Avatars(models.Model):
    firstName = models.CharField(max_length=26)
    lastName  = models.CharField(max_length=26)
    username  = models.CharField(max_length=26)
    models.UniqueConstraint(fields=['firstName','lastName','username'],name='unique_user')

class OwnerRegionAssociations(models.Model):
    username = models.CharField(max_length=26)
    region   = models.CharField(max_length=26)
    grid     = models.CharField(max_length=26)
    models.UniqueConstraint(fields=['username','region','grid'],name='unique_user_region_association')

class RESTConsoles(models.Model):
    simulator = models.CharField(max_length=26)
    ip        = models.CharField(max_length=26)
    port      = models.CharField(max_length=26)
    models.UniqueConstraint(fields=['simulator','ip','port','username'],name='unique_RESTConsole')

class RESTCredentials(models.Model):
    simulator = models.CharField(max_length=26)
    username  = models.CharField(max_length=26)
    password  = models.CharField(max_length=26)