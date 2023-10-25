from django.urls import path
from .views import *

app_name = 'kids'
urlpatterns = [
    path('cold/', cold, name='cold'),
    path('cold/advices', cold_advices, name='cold_advices')
]
