from django.urls import path
from . import views

urlpatterns = [
    path("verify/", views.verify_identity, name="verify_identity"),
    path("login/", views.login_view, name="login"),
]
