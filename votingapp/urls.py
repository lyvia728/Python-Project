
from django.urls import path
from . import views 

urlpatterns = [
path("templates/home.thml", views.home, name = "home")
]
