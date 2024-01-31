from django.shortcuts import render

# Create your views here.


def homelist(request):
    return render(request,'homedir/index.html')
