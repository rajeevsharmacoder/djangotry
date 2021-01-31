from django import forms

from .models import Course

class CourseModelForm(forms.ModelForm):
	class Meta:
		model = Course
		fields = [
			'title'
		]

	# Only at form level validation
	def clean_title(self):
		title = self.cleaned_data.get('title')
		if title.lower() == 'abc':
			raise forms.ValidationError("This is not a valid title.")
		return title
