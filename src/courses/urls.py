from django.urls import path
from .views import (
	CourseCreateView,
	CourseDeleteView,
	CourseListView,
	CourseUpdateView,
	CourseView
	# my_fbv
)

app_name = 'courses'

urlpatterns = [
	# path('', my_fbv, name='courses-list'),
	path('', CourseListView.as_view(), name='courses-list'),
	path('create/', CourseCreateView.as_view(), name='courses-create'),
	path('<int:id>/delete/', CourseDeleteView.as_view(), name='courses-delete'),
	path('<int:id>/', CourseView.as_view(), name='courses-detail'),
	path('<int:id>/update/', CourseUpdateView.as_view(), name='courses-update'),
]
