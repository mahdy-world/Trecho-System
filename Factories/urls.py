from django.urls import path 
from .views import *


app_name = 'Factories'

urlpatterns = [
    path('all_factories' ,FactoryList.as_view(), name="factory_list" ),
    path('factory/<int:pk>/', FactoryDetail.as_view(), name='FactoryDetail'),

]

