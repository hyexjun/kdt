from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'guest':'student'}
    return render(request, 'index.html', context)