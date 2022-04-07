from re import L
from django.shortcuts import redirect, render, get_object_or_404, redirect
from django.forms import modelform_factory
from .models import Skill, Subject
from .forms import SkillModelForm, SubjectModelForm
from django.contrib.admin.views.decorators import staff_member_required

def list_skills_view(request):

    skill_list = []
    name = request.user.username

    for skill in Skill.objects.all():
        if skill.user == request.user:
            skill_list.append(skill)


    return render(request, "skill_matrix/list_skills.html", {"name": name, "skills": skill_list, "user": request.user})

def list_subjects_view(request):

    subject_list = Subject.objects.all()
    name = request.user.username

    return render(request, "skill_matrix/list_subjects.html", {"name": name, "subjects": subject_list, "user": request.user})

def skill_create_view(request, *args, **kwargs):
    form = SkillModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = SkillModelForm()
    return render(request, "skill_matrix/skill_form.html", {"form": form, "user": request.user}) # 200

def subject_create_view(request, *args, **kwargs):
    form = SubjectModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():      
        obj = form.save(commit=False)
        obj.save()
        form = SubjectModelForm()
    return render(request, "skill_matrix/subject_form.html", {"form": form, "user": request.user}) 

def skill_update_view(request, id):

    item = Skill.objects.get(id=id)
    form = SkillModelForm(request.POST or None, instance=item)
    if form.is_valid():      
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return redirect('skill')
    else:
        form = SkillModelForm(instance=item)
    return render(request, "skill_matrix/update_skill_form.html", {"form": form}) 


def skill_delete_view(request, id):

    skill = Skill.objects.get(id=id)
    return render(request, "skill_matrix/delete_skill_form.html", {"skill": skill}) 

@staff_member_required
def delete_view(request, id):

    skill = Skill.objects.get(id=id)
    skill.delete()
    return redirect('skill')


def subject_update_view(request, id):

    item = Subject.objects.get(id=id)
    form = SubjectModelForm(request.POST or None, instance=item)
    if form.is_valid():      
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return redirect('subject')
    else:
        form = SubjectModelForm(instance=item)
    return render(request, "skill_matrix/update_subject_form.html", {"form": form}) 


def subject_delete_view(request, id):

    subject = Subject.objects.get(id=id)
    return render(request, "skill_matrix/delete_subject_form.html", {"subject": subject}) 

@staff_member_required
def s_delete_view(request, id):

    subject = Subject.objects.get(id=id)
    subject.delete()
    return redirect('subject')

@staff_member_required
def master_view(request):

    skill_list = Skill.objects.all()
    subject_list = Subject.objects.all()
    name = request.user.username

    return render(request, "skill_matrix/master_list.html", {"name": name, "subjects": subject_list, "skills": skill_list, "user": request.user})