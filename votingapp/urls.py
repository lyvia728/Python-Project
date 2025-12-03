
from django.urls import path
from . import views 

urlpatterns = [
path('', views.home, name='index'),
path('register/', views.register, name='register'),
path("parties/", views.parties, name="parties"),
path("submit_vote/", views.submit_vote, name="submit_vote"),# This makes it your homepage
]
