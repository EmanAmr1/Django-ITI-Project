from django.shortcuts import render,reverse

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from .models import *


mycategorylist = [

    {'id': 1, 'name': 'Chair', 'image': 'images/chair.png'},
    {'id': 2, 'name': 'Sofa', 'image': 'images/sofa.png'},
    {'id': 3, 'name': 'Table', 'image': 'images/table.png'},
    {'id': 4, 'name': 'Office', 'image': 'images/office.png'},
]


def mycategory(request):
    return HttpResponse("welcome")


def categorylist(request):
    # return HttpResponse(mycategorylist)
    #context = {'mycategorylist': mycategorylist}
    context = {'mycategorylist': Category.objects.all()} 
    return render(request, 'categorydir/index.html', context)


#def categorydetailes(request, catid):
    #cat = filter(lambda t: t['id'] == catid, mycategorylist)
    #cat = list(cat)
    #if cat:
        #return HttpResponse(cat)
    #return HttpResponse("not found")

'''
def categorydetailes(request, catid):
    # Use filter to find the product with the specified ID
    cat = filter(lambda t: t['id'] == catid,  mycategorylist)

    # Convert the filtered_products to a list
    cat = list(cat)

    # Check if any product was found
    if cat:
        # Take the first product (there should be only one with the given ID)
        catego = cat[0]

        # Render the product details template with the product data
        return render(request, 'categorydir/categorydetaileshtml.html', {'catgo': catego})
    else:
        return HttpResponse("Product not found")
'''


def categorydetailes(request, catid):
    catgo=Category.objects.get(id=catid)
    context={'catgo': catgo}
    return render(request, 'categorydir/categorydetaileshtml.html', context)


def addcat(request):
    if(request.method=='POST'):
        Category.objects.create(name=request.POST['cname'],image= request.POST['cimage'])
        #return HttpResponseRedirect('/products/list')
        r=reverse("category_list")
        return HttpResponseRedirect(r)
    return render(request, 'categorydir/cataddhtml.html')

def deletecat(request,catid):
  Category.objects.filter(id=catid).delete()
  r=reverse("category_list")
  return HttpResponseRedirect(r)