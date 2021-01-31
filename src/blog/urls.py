from django.urls import path

# from blog.views import (
# 	article_detail_view, 
# 	article_create_view, 
# 	article_update_view, 
# 	article_delete_view,
# 	article_list_view
# )

from .views import (
	ArticleCreateView,
	ArticleDeleteView,
	ArticleDetailView,
	ArticleListView,
	ArticleUpdateView
)

app_name = "blog"

urlpatterns = [

	# CLASS BASED URLS

	path('', ArticleListView.as_view(), name='article-list'),
	path('create/', ArticleCreateView.as_view(), name='article-create'),
	path('<int:id>/', ArticleDetailView.as_view(), name='article-detail'),
	path('<int:id>/update/', ArticleUpdateView.as_view(), name='article-update'),
	path('<int:id>/delete/', ArticleDeleteView.as_view(), name='article-delete'),


	# FUNCTION BASED URLS

	# path('', article_list_view, name='article-list'),
	# path('create/', article_create_view, name='article-create'),
	# path('<int:id>/', article_detail_view, name='article-detail'),
	# path('<int:id>/update/', article_update_view, name='article-update'),
	# path('<int:id>/delete/', article_delete_view, name='article-delete'),

]
