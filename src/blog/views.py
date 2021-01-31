from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import(
	CreateView,
	UpdateView,
	ListView,
	DetailView,
	DeleteView
)

from .forms import ArticleModelForm
from .models import Article

class ArticleCreateView(CreateView):
	template_name = 'articles/article_create.html'
	form_class = ArticleModelForm
	queryset = Article.objects.all()
	# success_url = '/'

	def form_valid(self, form):
		print(form.cleaned_data)
		return super().form_valid(form)

	# def get_success_url(self):
	# 	return '/'

class ArticleListView(ListView):
	template_name = 'articles/article_list.html'
	queryset = Article.objects.all()

class ArticleDetailView(DetailView):
	template_name = 'articles/article_detail.html'
	# queryset = Article.objects.all()

	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Article, id=id_)

class ArticleUpdateView(UpdateView):
	template_name = 'articles/article_create.html'
	form_class = ArticleModelForm
	# queryset = Article.objects.all()

	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Article, id=id_)

	def form_valid(self, form):
		print(form.cleaned_data)
		return super().form_valid(form)

class ArticleDeleteView(DeleteView):
	template_name = 'articles/article_delete.html'
	# queryset = Article.objects.all()

	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Article, id=id_)

	def get_success_url(self):
		return reverse('blog:article-list')


# BELOW IS DIRECT FUNCTION RELATED VIEWS ACTIONS

# from django.http import Http404
# from django.shortcuts import render, get_object_or_404, redirect

# from .models import Article
# from .forms import ArticleForm

# def article_list_view(request):
# 	queryset = Article.objects.all()
# 	context = {
# 		"object_list": queryset
# 	}
# 	return render(request, "articles/article_list.html", context)

# def article_detail_view(request, id):
# 	obj = get_object_or_404(Article, id=id)
# 	context = {
# 		"object": obj
# 	}
# 	return render(request, "articles/article_detail.html", context)


# def article_create_view(request):
# 	form = ArticleForm(request.POST or None)
# 	if form.is_valid():
# 		form.save()
# 		form = ArticleForm()
# 	context = {
# 		"form": form
# 	}
# 	return render(request, "articles/article_create.html", context)

# def article_update_view(request, id):
# 	obj = get_object_or_404(Article, id=id)
# 	form = ArticleForm(request.POST or None, instance=obj)
# 	if form.is_valid():
# 		form.save()
# 		return redirect("../")
# 	context = {
# 		"form": form
# 	}
# 	return render(request, "articles/article_create.html", context)

# def article_delete_view(request, id):
# 	obj = get_object_or_404(Article, id=id)
# 	if request.method == "POST":
# 		obj.delete()
# 		return redirect("../../")
# 	context = {
# 		"object": obj
# 	}
# 	return render(request, "articles/article_delete.html", context)
