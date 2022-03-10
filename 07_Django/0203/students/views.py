from django.shortcuts import render

# Create your views here.
def regStudent(request):
    return render(request, 'reg.html')