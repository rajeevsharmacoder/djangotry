from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from .forms import CourseModelForm
from .models import Course

# BASE VIEW CLASS = View

# Object Mixin
# class CourseObjectMixin(object):
# 	model = Course

# 	def get_bject(self):
# 		id = self.kwargs.get('id')
# 		obj = None
# 		if id is not None:
# 			obj = get_object_or_404(self.model, id=id)
# 		return obj


class CourseCreateView(View):
	template_name = 'courses/course_create.html'

	def get(self, request, *args, **kwargs):
		form = CourseModelForm()
		context = {
			"form": form
		}
		return render(request, self.template_name, context)

	def post(self, request, *args, **kwargs):
		form = CourseModelForm(request.POST)
		if form.is_valid():
			form.save()
			form = CourseModelForm()
			return redirect("/courses/")
		context = {
			"form": form
		}
		return render(request, self.template_name, context)

# delete with Mixin
# class CourseDeleteView(CourseObjectMixin, View):
# 	template_name = 'courses/course_delete.html'

# 	def get(self, request, id=None, *args, **kwargs):
# 		context = {}
# 		obj = self.get_object()
# 		if obj is not None:
# 			context['object'] = obj
# 		return render(request, self.template_name, context)

# 	def post(self, request, id=None, *args, **kwargs):
# 		context = {}
# 		obj = self.get_object()
# 		if obj is not None:
# 			obj.delete()
# 			context['object'] = None
# 			return redirect('/courses/')
# 		return render(request, self.template_name, context)

# delete without Mixin
class CourseDeleteView(View):
	template_name = 'courses/course_delete.html'

	def get_object(self):
		id = self.kwargs.get("id")
		obj = None
		if id is not None:
			obj = get_object_or_404(Course, id=id)
		return obj

	def get(self, request, id=None, *args, **kwargs):
		context = {}
		obj = self.get_object()
		if obj is not None:
			context['object'] = obj
		return render(request, self.template_name, context)

	def post(self, request, id=None, *args, **kwargs):
		context = {}
		obj = self.get_object()
		if obj is not None:
			obj.delete()
			context['object'] = None
			return redirect('../../')
		return render(request, self.template_name, context)

class CourseUpdateView(View):
	template_name = 'courses/course_update.html'

	def get_object(self):
		id = self.kwargs.get("id")
		obj = None
		if id is not None:
			obj = get_object_or_404(Course, id=id)
		return obj

	def get(self, request, id=None, *args, **kwargs):
		context = {}
		obj = self.get_object()
		if obj is not None:
			form = CourseModelForm(instance=obj)
			context['object'] = obj
			context['form'] = form
		return render(request, self.template_name, context)

	def post(self, request, id=None, *args, **kwargs):
		context = {}
		obj = self.get_object()
		if obj is not None:
			form = CourseModelForm(request.POST, instance=obj)
			if form.is_valid():
				form.save()
				print(obj)
				return redirect('../')
			context['object'] = obj
			context['form'] = form
		return render(request, self.template_name, context)

class CourseListView(View):
	template_name = 'courses/course_list.html'
	queryset = Course.objects.all()
	
	def get_queryset(self):
		return self.queryset

	def get(self, request, *args, **kwargs):
		context = {
			"object_list": self.get_queryset()
		}
		return render(request, self.template_name, context)

# class MyListView(CourseListView): # inheritance property using class based views
	# queryset = Course.objects.filter(id=1)

# with object Mixin
# class CourseView(CourseObjectMixin, View):
# 	template_name = 'courses/course_detail.html'

# 	def get(self, request, id=None, *args, **kwargs):
# 		context = {
# 			"object": self.get_object()
# 		}
# 		return render(request, self.template_name, context)

# without object Mixin
class CourseView(View):
	template_name = 'courses/course_detail.html'

	def get(self, request, id=None, *args, **kwargs):
		context = {}
		if id is not None:
			obj = get_object_or_404(Course, id=id)
			context['object'] = obj
		return render(request, self.template_name, context)

	def post(request, *args, **kwargs):
		return render(request, 'about.html', {})


# HTTP METHOD
def my_fbv(request, *args, **kwargs):
	return render(request, 'about.html', {})
