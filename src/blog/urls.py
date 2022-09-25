from django.urls import path
 
# Importing all required views
from .views import HomeView
 
urlpatterns = [
    path('', HomeView.as_view(), name="home"),
]
