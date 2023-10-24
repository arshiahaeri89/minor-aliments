from django.urls import path
from .views import cold

app_name = 'kids'
urlpatterns = [
    path('cold/', cold, name='cold')
]
