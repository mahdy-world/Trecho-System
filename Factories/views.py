from django.shortcuts import render

import Factories
from .models import *

# Create your views here
def list(request):
    factory = Factory.objects.all()
    print(factory)
    
    context = {
        'factory' : factory
    }
    return render(request,'factory/list.html' , context)