from django.urls import path

from . import views

app_name = 'paper_management'
urlpatterns = [
    path('', views.index, name='index'),
    path('paper/<int:paper_id>/', views.paper_detail, name='paper_detail')
]
