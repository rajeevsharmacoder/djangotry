from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
	print(args, kwargs)
	print(request.user)
	# return HttpResponse("<h1 align='center'>Welcome to djangotry project</h1>")
	return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
	# return HttpResponse("<h1 align='center'>Contacts Page</h1>")
	return render(request, "contact.html", {})

def social_view(request, *args, **kwargs):
	# return HttpResponse("<h1 align='center'>Social Page</h1>")
	return render(request, "social.html", {})

def about_view(request, *args, **kwargs):

	my_context = {
		"title": "this is about me.",
		"this_is_true": True,
		"my_number": 123,
		"my_list": [123, 456, 789, "Abc"],
		"my_html": "<h4>I'm in about page.</h4>"
	}

	# return HttpResponse("<h1 align='center'>About Page</h1>")
	return render(request, "about.html", my_context)
