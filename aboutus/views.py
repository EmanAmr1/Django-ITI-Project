from django.shortcuts import render

# Create your views here.



def aboutlist(request):
    return render(request,'aboutusdir/index.html')