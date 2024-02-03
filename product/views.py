from django.shortcuts import render,reverse

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from .models import *


myproductslist=[

{'id':1,'name':'product1', 'image':'images/card5.png' },
{'id':2,'name':'product2', 'image':'images/card2.png'},
{'id':3,'name':'product3', 'image':'images/card3.png'},
{'id':4,'name':'product4', 'image':'images/card4.png'},
]



def myproduct(request):
    return HttpResponse("welcome")

def productlist(request):
    #return HttpResponse(myproductslist)
    context = {'myproductslist': Product.objects.all()} #from db 
    #context = {'myproductslist': myproductslist}
    return render(request,'productdir/index.html', context)



#def productdetailes(request,proid):
   # prod=filter(lambda t:t['id']==proid,myproductslist)
    #prod=list(prod)
    #if prod:
        #return HttpResponse(prod)
    #return HttpResponse("not found")


"""
def productdetailes(request, proid):
    # Use filter to find the product with the specified ID
    filtered_products = filter(lambda product: product['id'] == proid, myproductslist)
    
    # Convert the filtered_products to a list
    filtered_products = list(filtered_products)

    # Check if any product was found
    if filtered_products:
        # Take the first product (there should be only one with the given ID)
        product = filtered_products[0]

        # Render the product details template with the product data
        return render(request, 'productdir/prodetaileshtml.html', {'product': product})
    else:
        return HttpResponse("Product not found")
        """

def productdetailes(request, proid):
    product=Product.objects.get(id=proid)
    context={'product': product}
    return render(request, 'productdir/prodetaileshtml.html', context)


def addpro(request):
    if(request.method=='POST'):
        Product.objects.create(name=request.POST['pname'],image= request.POST['pimage'])
        #return HttpResponseRedirect('/products/list')
        r=reverse("product_list")
        return HttpResponseRedirect(r)
    return render(request, 'productdir/proaddhtml.html')

def deletepro(request,proid):
  Product.objects.filter(id=proid).delete()
  r=reverse("product_list")
  return HttpResponseRedirect(r)
  