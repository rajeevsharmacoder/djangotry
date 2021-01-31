from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

from .models import Product
from .forms import ProductForm, RawProductForm
# Create your views here.
def product_create_view(request): #version 1
	form = ProductForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ProductForm()
		return redirect("../")

	context = {
		'form': form
	}
	return render(request, "products/product_create.html", context)

def product_update_view(request, id):
	obj = get_object_or_404(Product, id=id)
	form = ProductForm(request.POST or None, instance=obj)
	if form.is_valid():
		form.save()
		return redirect("../")
	context = {
		"form": form
	}
	return render(request, "products/product_create.html", context)

def product_list_view(request):
	queryset = Product.objects.all()

	context = {
		"object_list": queryset
	}
	return render(request, "products/product_list.html", context)

def product_detail_view(request, id):
	obj = get_object_or_404(Product, id=id)
	context = {
		'object': obj
	}
	return render(request, "products/product_detail.html", context)

def product_delete_view(request, id):
	obj = get_object_or_404(Product, id=id)
	if request.method == "POST":
		obj.delete()
		return redirect("../../")
	context = {
		"object": obj
	}
	return render(request, "products/product_delete.html", context)

def dynamic_lookup_view(request, id):
	obj = get_object_or_404(Product, id=id)
	context = {
		"object": obj
	}
	return render(request, "products/product_detail.html", context)

def render_initial_data(request):
	initial_data = {
		"title": "Title to be entered here",
		"description": "Description to be entered here",
		"price": 00.00,
		"summary": "Summary to be entered here",
		"featured": False
	}
	obj = Product.objects.get(id=1)
	# form = RawProductForm(request.POST or None, initial=initial_data)
	form = ProductForm(request.POST or None, instance=obj)
	if form.is_valid():
		form.save()
	context = {
		"form": form
	}
	return render(request, "products/product_create.html", context)

# def product_create_view(request, *args, **kwargs): #version 3
# 	my_form = RawProductForm()
# 	if request.method == "POST":
# 		my_form = RawProductForm(request.POST)
# 		if my_form.is_valid(): # data in form validation check
# 			print(my_form.cleaned_data)
# 			Product.objects.create(**my_form.cleaned_data)
# 		else:
# 			print(my_form.errors)
# 	context = {
# 		"form": my_form
# 	}
# 	return render(request, "products/product_create.html", context)

# def product_create_view(request, *args, **kwargs): #version 2
# 	# print(request.GET)
# 	# print(request.POST)
# 	if request.method == "POST":
# 		my_new_title = request.POST.get('title')
# 		print(my_new_title)
# 		# Product.objects.create(title=my_new_title)
# 	context = {}
# 	return render(request, "products/product_create.html", context)
