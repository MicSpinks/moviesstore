from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.petition_list, name='petition_list'),
    path("", views.petition_list, name="petition_list"),
    path("<int:pk>/vote/", views.vote_petition, name="vote_petition"),
    path("create/", views.petition_create, name="petition_create"),
]