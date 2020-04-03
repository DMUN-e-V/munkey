from django.urls import path

from . import views

app_name = "user_management"
urlpatterns = [
    path("register", views.RegisterView.as_view(), name="register"),
    path("validate/<uidb64>/<token>", views.ValidateView.as_view(), name="validate"),
]
