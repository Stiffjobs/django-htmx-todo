from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("submit-todo", views.submit_todo, name="submit-todo"),
    path("toggle-completed/<int:pk>/", views.toggle_completed, name="toggle-completed"),
    path("delete-todo/<int:pk>/", views.delete_todo, name="delete-todo"),
]
