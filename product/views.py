from django.shortcuts import render, reverse, redirect
from django.views.generic import UpdateView,DetailView,DeleteView,ListView,CreateView
from django.views import View
from django.urls import reverse_lazy
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *
from category.models import *

myproductslist = [

    {'id': 1, 'name': 'product1', 'image': 'images/card5.png'},
    {'id': 2, 'name': 'product2', 'image': 'images/card2.png'},
    {'id': 3, 'name': 'product3', 'image': 'images/card3.png'},
    {'id': 4, 'name': 'product4', 'image': 'images/card4.png'},
]


def myproduct(request):
    return HttpResponse("welcome")


def productlist(request):
    # return HttpResponse(myproductslist)
    context = {'myproductslist': Product.objects.all()}  # from db
    # context = {'myproductslist': myproductslist}
    
    return render(request, 'productdir/index.html', context)


# def productdetailes(request,proid):
   # prod=filter(lambda t:t['id']==proid,myproductslist)
    # prod=list(prod)
    # if prod:
    # return HttpResponse(prod)
    # return HttpResponse("not found")

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
    product = Product.objects.get(id=proid)
    context = {'product': product}
    return render(request, 'productdir/prodetaileshtml.html', context)


def addpro(request):
    if (request.method == 'POST'):
        Product.objects.create(
            name=request.POST['pname'], image=request.FILES['pimage'],
            category=Category.objects.get(id=request.POST['category']))
        # return HttpResponseRedirect('/products/list')
        r = reverse("product_list")
        return HttpResponseRedirect(r)
    #context={"cate":Category.objects.all()}
    return render(request, 'productdir/proaddhtml.html',{'getcategory': Category.getcategory()})


def deletepro(request, proid):
    Product.objects.filter(id=proid).delete()
    r = reverse("product_list")
    return HttpResponseRedirect(r)

'''
def updatepro(request, proid):
    pro = Product.objects.get(id=proid)
    #pro=Product.product_detailes(proid)
    context = {'pro': pro}

    if (request.method == 'POST'):
        if (request.POST['pname'] != ''):
            Product.objects.filter(id=proid).update(
                name=request.POST['pname'], image=request.FILES['pimage'])
            # return HttpResponseRedirect('/products/list')
            r = reverse("product_list")
            return HttpResponseRedirect(r)
        else:
            context['msg'] = 'fill all fields'
    return render(request, 'productdir/proupdate.html', context)
'''


def updatepro(request, proid):
    pro = Product.objects.get(id=proid)
    context = {'pro': pro}

    if request.method == 'POST':
        pname = request.POST['pname']

        # Check if 'pimage' key exists in request.FILES
        if 'pimage' in request.FILES:
            pimage = request.FILES['pimage']
            # Update the product with the new name and image
            pro.name = pname
            pro.image = pimage
            pro.save()

            # Redirect to the product list after successful update
            return HttpResponseRedirect(reverse("product_list"))
        else:
            context['msg'] = 'Image not provided'

    return render(request, 'productdir/proupdate.html', context)

'''
def addFormpro(request):
    form = ProductForm()
    context = {"form": form}
    if (request.method == 'POST'):
        form = ProductForm(request.POST, request.FILES)  
        if form.is_valid():
            Product.objects.create(
                name=request.POST['pname'], image=request.FILES['pimage'])
        # return HttpResponseRedirect('/products/list')
            r = reverse("product_list")
            return HttpResponseRedirect(r)
        else:
            context['msg'] = "data not complete"

    return render(request, 'productdir/proaddForm.html', context)
'''

'''
def addFormpro(request):
    form = ProductForm()
    context = {"form": form}

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            Product.objects.create(
                name=form.cleaned_data['name'],
                image=form.cleaned_data['image'],
                category=form.cleaned_data['category']
            )
            r = reverse("product_list")
            return HttpResponseRedirect(r)
        else:
            context['msg'] = "name must be unique"

    return render(request, 'productdir/proaddForm.html',context,{'getcategory': Category.getcategory()})
'''

def addFormproo(request):
    context = {}

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            r = reverse("product_list")
            return HttpResponseRedirect(r)
        else:
            context['form'] = form
            context['msg'] = "Name must be unique"
    else:
        form = ProductForm()
        context['form'] = form

    context['getcategory'] = Category.getcategory()
    return render(request, 'productdir/proaddForm.html', context)


def addFormpro(request):
    context = {}

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            Product.objects.create(
                name=form.cleaned_data['name'],
                image=form.cleaned_data['image'],
                category_id=form.cleaned_data['category']
            )
            r = reverse("product_list")
            return HttpResponseRedirect(r)
        else:
            context['form'] = form
            context['msg'] = "Name must be unique"
    else:
        form = ProductForm()
        context['form'] = form

    context['getcategory'] = Category.getcategory()
    return render(request, 'productdir/proaddForm.html', context)


def addMetaFormPro(request):
    metaform = ProductMetaForm()
    context = {'metaform': metaform}
    if (request.method == 'POST'):
        metaform = ProductMetaForm(request.POST, request.FILES)
        if (metaform.is_valid()):
            metaform.save()
            return redirect(reverse("product_list"))
    return render(request, 'productdir/proddMetaForm.html', context)


#implement the same using generic method

class ProductGenericUpdate(UpdateView):
    model=Product
    template_name='productdir/proMetaUpdate.html'
    context_object_name='form'
    form_class=ProductMetaForm
    success_url=reverse_lazy('product_list')


class ProductGenericDetails(DetailView):
    model=Product
    template_name='productdir/prodetaileshtml.html'
    context_object_name='product'


class ProductGenericDelete(DeleteView):
    model=Product
    template_name='productdir/proDelete.html'
    context_object_name='product'
    success_url=reverse_lazy('product_list')


class ProductGenericlist(ListView):
    model=Product
    template_name='productdir/index.html'
    context_object_name='product'


class ProductGenericCreate(CreateView):
    model=Product
    template_name='productdir/proCreate.html'
    form_class=ProductMetaForm
    success_url=reverse_lazy('product_list')