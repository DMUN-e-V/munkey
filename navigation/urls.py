from django.urls import path

from navigation import views

urlpatterns = [
    path("choose-munkey-link", views.choose_munkey_link, name='choose-munkey-link'),
]
