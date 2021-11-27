from django.shortcuts import render
from django.views.generic import *
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from .models import *

# Create your views here

class FactoryList(LoginRequiredMixin , ListView):
    login_url = '/auth/login/'
    model = Factory
    paginate_by = 6