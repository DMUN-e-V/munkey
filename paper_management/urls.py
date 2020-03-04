from django.urls import path

from . import views

app_name = "paper_management"
urlpatterns = [
    path("", views.ListView.as_view(), name="paper_list"),
    path("<int:pk>/edit", views.UpdateView.as_view(), name="paper_change"),
    path("<int:pk>/delete", views.DeleteView.as_view(), name="paper_delete"),
    path("<int:pk>/", views.DetailView.as_view(), name="paper_detail"),
    path("add/", views.CreateView.as_view(), name="paper_add"),
]
