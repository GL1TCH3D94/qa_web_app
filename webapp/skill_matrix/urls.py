from django.urls import path

from .import views

urlpatterns = [
    path('skill', views.list_skills_view, name="skill"),
    path('add_skill', views.skill_create_view, name="add_skill"),
    path('add_subject', views.subject_create_view, name="add_subject"),
]