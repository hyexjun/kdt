from django.shortcuts import render

# Create your views here.
def sview(req):
    return render(req, 'sview.html')