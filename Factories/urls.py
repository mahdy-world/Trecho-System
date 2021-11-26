from django.urls import path 
from . import views


app_name = 'Factories'

urlpatterns = [
    path('all_factories' ,views.list, name="factory_list" )
]

