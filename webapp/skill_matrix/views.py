from re import L
from django.shortcuts import redirect, render, get_object_or_404, redirect
from django.forms import modelform_factory
from .models import Skill, Subject
from .forms import SkillModelForm, SubjectModelForm
from django.contrib.admin.views.decorators import staff_member_required

def list_skills_view(request):

    if request.user.is_authenticated:

        skill_list = []
        name = request.user.username

        for skill in Skill.objects.all():
            if skill.user == request.user:
                skill_list.append(skill)

        return render(request, "skill_matrix/list_skills.html", {"name": name, "skills": skill_list, "user": request.user})

    request.session['error'] ="You must be logged in to perform this action"
    return redirect('login')
    

def list_subjects_view(request):

    if request.user.is_authenticated:

        subject_list = Subject.objects.all()
        name = request.user.username

        return render(request, "skill_matrix/list_subjects.html", {"name": name, "subjects": subject_list, "user": request.user})

    request.session['error'] ="You must be logged in to perform this action"
    return redirect('login')

def skill_create_view(request, *args, **kwargs):
    
    if request.user.is_authenticated:

        form = SkillModelForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            obj = form.save(commit=False)            
            obj.user = request.user
            obj.save()
            form = SkillModelForm()
        return render(request, "skill_matrix/skill_form.html", {"form": form, "user": request.user})

    request.session['error'] ="You must be logged in to perform this action"
    return redirect('login')

def subject_create_view(request, *args, **kwargs):
    if request.user.is_authenticated:

        form = SubjectModelForm(request.POST or None, request.FILES or None) 
        if form.is_valid():      
            obj = form.save(commit=False)
            obj.save()
            form = SubjectModelForm()
        return render(request, "skill_matrix/subject_form.html", {"form": form, "user": request.user})

    request.session['error'] ="You must be logged in to perform this action"
    return redirect('login')

def skill_update_view(request, id):

    if request.user.is_authenticated:

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

    request.session['error'] ="You must be logged in to perform this action"
    return redirect('login')

def skill_delete_view(request, id):

    if request.user.is_authenticated:

        skill = Skill.objects.get(id=id)
        return render(request, "skill_matrix/delete_skill_form.html", {"skill": skill}) 

    request.session['error'] ="You must be logged in to perform this action"
    return redirect('login')

@staff_member_required
def delete_view(request, id):

    if request.user.is_authenticated:

        skill = Skill.objects.get(id=id)
        skill.delete()
        return redirect('skill')

    request.session['error'] ="You must be logged in to perform this action"
    return redirect('login')

def subject_update_view(request, id):

    if request.user.is_authenticated:

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

    request.session['error'] ="You must be logged in to perform this action"
    return redirect('login')

def subject_delete_view(request, id):
   
    if request.user.is_authenticated:

        subject = Subject.objects.get(id=id)
        return render(request, "skill_matrix/delete_subject_form.html", {"subject": subject})

    request.session['error'] ="You must be logged in to perform this action"
    return redirect('login')

@staff_member_required
def s_delete_view(request, id):

    if request.user.is_authenticated:

        subject = Subject.objects.get(id=id)
        subject.delete()
        return redirect('subject')

    request.session['error'] ="You must be logged in to perform this action"
    return redirect('login')

@staff_member_required
def master_view(request):

    if request.user.is_authenticated:

        skill_list = Skill.objects.all()
        subject_list = Subject.objects.all()
        name = request.user.username

        return render(request, "skill_matrix/master_list.html", {"name": name, "subjects": subject_list, "skills": skill_list, "user": request.user})

    request.session['error'] ="You must be logged in to perform this action"
    return redirect('login')

def invalid_user_view(request):
    return render(request, "skill_matrix/invalid_user.html", {"user": request.user})