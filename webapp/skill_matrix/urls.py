from django.urls import path

from .import views

urlpatterns = [
    path('<int:id>', views.skill, name="skill"),
    path('add_skill', views.skill_create_view, name="add_skill"),
]