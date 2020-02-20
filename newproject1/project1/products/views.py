"""# from django.http import Http404
# from django.shortcuts import render, get_object_or_404, redirect
# from django.http import HttpResponse
# from .models import Product
# from .forms import ProductForm, RawProductForm
# # Create your views here.
#
#
# # from lecture 29
# def dynamic_lookup_view(request,my_id):
#     # obj = Product.objects.get(id=my_id)
#     # obj = get_object_or_404(Product,id =my_id)
#     try:
#         obj = Product.objects.get(id=my_id)
#     except Product.DoesNotExist:
#         raise Http404
#         return redirect('../../')
#     context = {
#         "object":obj
#     }
#     return render(request, 'products/product_detail.html',context)
#
#
#
#
# # def product_create_view(request):
# #     my_form = RawProductForm()
# #     if request.method == "POST":
# #         my_form = RawProductForm(request.POST)
# #         if my_form.is_valid():
# #             #now the data is good
# #             print(my_form.cleaned_data)
# #             Product.objects.create(**my_form.cleaned_data)
# #         else:
# #             print(my_form.errors)
# #     context={
# #         "form" : my_form
# #     }
# #     return render(request,'products/product_create.html',context)
#
# # def product_create_view(request):
# #     # print(request.GET)
# #     # print(request.POST)
# #     if request.method == "POST":
# #         my_new_title = request.POST.get('title')
# #         print(my_new_title)
# #     context={}
# #     return render(request,'products/product_create.html',context)
#
#
# def product_create_view(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ProductForm()
#     context = {
#         'form': form
#     }
#     return render(request,'products/product_create.html',context)
#
# def product_update_view(request,id=id):
#     obj = get_object_or_404(Product,id=id)
#     form = ProductForm(request.POST or None, instance=obj)
#     if form.is_valid():
#         form.save()
#         context={
#             'form':form
#         }
#     return render(request,"product/product_create.html",context)
#
#
# # from lecture 32
# def product_list_view(request):
#     queryset = Product.objects.all() ## list all objects
#     context = {
#         "object_list":queryset
#     }
#     return render(request,"products/product_list.html",context)
#
# # def product_detail_view(request):
# #     obj = Product.objects.get(id=1)
# #     # context = {
# #     #     'title': obj.title,
# #     #     'description': obj.description
# #     # }
# #     context = {
# #         'object' : obj
# #     }
# #     return render(request,"products/product_detail.html",context)
#
# def product_detail_view(request,id=id):
#     obj = get_object_or_404(Product,id=id)
#     context = {
#         'object':obj
#     }
#     return render(request,"products/product_detail.html",context)
#
# # # from lecture 31
# def product_delete_view(request,id):
#     obj = get_object_or_404(Product,id=id)
#     # POST request
#     if request.method == "POST":
#         # confirming delete
#         obj.delete()
#         context = {
#             "object": obj
#         }
#     return render(request,"products/product_delete.html",context)"""

from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProductForm
from .models import Product


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)


def product_update_view(request, id=id):
    obj = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)


def product_list_view(request):
    queryset = Product.objects.all()  # list of objects
    context = {
        "object_list": queryset
    }
    return render(request, "products/product_list.html", context)


def product_detail_view(request, id):
    obj = get_object_or_404(Product, id=id)
    context = {
        "object": obj
    }
    return render(request, "products/product_detail.html", context)


def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "products/product_delete.html", context)
