from django.urls import path 
from .views import *


app_name = 'Factories'

urlpatterns = [
    path('all_factories' ,FactoryList.as_view(), name="factory_list" )
]

