from django.shortcuts import render

def profiles(request):
    context = {}
    return render(request, 'users/profiles.html', context)

