#Author: antlampas
#Date: 2023-04-23
#This work is licensed under the Creative Commons Attribution 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

from django.contrib import admin

from .models import *

@admin.register(Setting)
class settingAdmin(admin.ModelAdmin):
    option = "option"
    value  = "value"
    list_display = ["option","value"]

@admin.register(RESTConsole)
class RESTConsoleAdmin(admin.ModelAdmin):
    simulator = "simulator"
    ip        = "ip"
    port      = "port"
    list_display = ["simulator","ip","port"]

@admin.register(RESTCredential)
class RESTCredentialAdmin(admin.ModelAdmin):
    simulator = "simulator"
    username  = "username"
    password  = "password"
    list_display = ["simulator","username","password"]