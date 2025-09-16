from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    # Index
    path('', views.index, name='index'),

    # Movie detail and reviews
    path('<int:id>/', views.show, name='show'),
    path('<int:id>/review/create/', views.create_review, name='create_review'),
    path('<int:id>/review/<int:review_id>/edit/', views.edit_review, name='edit_review'),
    path('<int:id>/review/<int:review_id>/delete/', views.delete_review, name='delete_review'),

    # Hidden movies and toggle
    path('hidden/', views.hidden_movies, name='hidden_movies'),
    path('<int:pk>/toggle_hide/', views.toggle_hide, name='toggle_hide'),
]