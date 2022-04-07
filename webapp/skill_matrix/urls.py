from django.urls import path

from .import views

urlpatterns = [
    path('master', views.master_view, name="master"),
    path('skill', views.list_skills_view, name="skill"),
    path('subject', views.list_subjects_view, name="subject"),
    path('update_subject/<int:id>', views.subject_update_view, name="update_subject"),
    path('delete_subject/<int:id>', views.subject_delete_view, name="delete_subject"),
    path('update_skill/<int:id>', views.skill_update_view, name="update_skill"),
    path('delete_skill/<int:id>', views.skill_delete_view, name="delete_skill"),
    path('deleted/<int:id>', views.delete_view, name="deleted"),
    path('s_deleted/<int:id>', views.s_delete_view, name="s_deleted"),
    path('add_skill', views.skill_create_view, name="add_skill"),
    path('add_subject', views.subject_create_view, name="add_subject"),
]