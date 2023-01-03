from django.shortcuts import render
from django.http import HttpResponse

projectList = [
    {
        'id': '1',
        'title': "Econnerce Website",
        'description': "Nice and very good shop"
    },
    {
        'id': '2',
        'title': "Portfolio Website",
        'description': "This was very good project and so on"
    },
    {
        'id': '3',
        'title': "Social Network",
        'description': "Awsome open source project still working on it"
    }
    ]


def projects(request):
    page = 'Projects'
    number = 10
    context = {
        'page': page,
        'number': number,
        'projects': projectList
    }
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = None
    for i in projectList:
        if i['id'] == pk:
            projectObj = i
    context = {'project': projectObj}        
    return render(request, 'projects/single-project.html', context)

