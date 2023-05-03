#Author: antlampas
#Date: 2023-04-28
#This work is licensed under the Creative Commons Attribution 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

from django import forms

from django.apps import apps
if apps.is_installed("OpenSimBaseInterface"):
    from OpenSimBaseInterface.models import *

class SimulatorSelect(forms.Form):
    simulator = forms.ModelChoiceField(queryset=Simulator.objects)