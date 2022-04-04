from re import L
from django.shortcuts import redirect, render, get_object_or_404, redirect
from django.forms import modelform_factory
from .models import Skill
from .forms import SkillModelForm

def list_skills_view(request):

    skill_list = []
    name = request.user.username

    for skill in Skill.objects.all():
        if skill.user == request.user:
            skill_list.append(skill)


    return render(request, "skill_matrix/list_skills.html", {"name": name, "skills": skill_list})

#def user_list(request):
#    return render(request, "skill_check/user_list.html", {"users": User.objects.all()})

def skill_create_view(request, *args, **kwargs):
    form = SkillModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = SkillModelForm()
    return render(request, "skill_matrix/skill_form.html", {"form": form}) # 200