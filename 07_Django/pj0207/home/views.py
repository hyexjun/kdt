from django.shortcuts import render

# Create your views here.
def index(req):
    context = {'user_id':'admin', 'u_count':100}
    return render(req, 'index.html', context)