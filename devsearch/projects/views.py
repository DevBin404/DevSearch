from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import ProjectForm, ReviewForm
from .models import Project
from .uttils import searchProjects, paginateProjects


def projects(request):
    projects, search_query = searchProjects(request)

    projects, custom_range = paginateProjects(request, projects, 3)

    context = {
        'projects': projects,
        'search_query': search_query, 
        'custom_range': custom_range,
    }
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    project = Project.objects.get(pk=pk)
    
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.owner = request.user.profile
        review.project = project
        review.save()

        project.getVoteCount

        messages.info(request, 'Your review submitted for this project!')
        return redirect('project', pk=project.id)  
    context = {
        'project': project,
        'form': form,
    }        
    return render(request, 'projects/single-project.html', context)


@login_required(login_url='login')
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            messages.success(request, 'Project was created successfully!')
            return redirect('account')
    context = {
        'form': form,
    }
    return render(request, 'projects/project-form.html', context)


@login_required(login_url='login')
def updateProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES,instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project was updated successfully')
            return redirect('account')
    context = {
        'form': form,
    }
    return render(request, 'projects/project-form.html', context)   


@login_required(login_url='login')
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)

    if request.method == 'POST':
        project.delete()
        messages.success(request, 'Project was deleted successfully!')
        return redirect('account')
    context = {
        'object': project
    }
    return render(request, 'delete-template.html', context)     
    