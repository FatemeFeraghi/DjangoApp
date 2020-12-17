from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name="posts-index"),
    path('<int:received_id>/details/', views.details, name="posts-details"),
]