from django.shortcuts import render

def index(request):
    context = {'guest': 'student'}
    return render(request, 'index.html', context)
