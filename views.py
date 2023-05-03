#Author: antlampas
#Date: 2023-04-23
#This work is licensed under the Creative Commons Attribution 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

from django.shortcuts import render

from django.apps import apps
if apps.is_installed("OpenSimBaseInterface"):
    from OpenSimBaseInterface.models import *

from .models import *
from .forms  import *

def index(request):
    form = SimulatorSelect()
    context = {"form" : form}
    return render(request,'RESTConsole/index.html',context)

def console(request):
    if request.method == "POST":
        simulator = request.POST.get("Simulator")
        
    context = {}
    return render(request,'RESTConsole/index.html',context)

def input(request):
    context = {}
    return render(request,'RESTConsole/input.html',context)

def output(request):
    context = {}
    return render(request,'RESTConsole/output.html',context)