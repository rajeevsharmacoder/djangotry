from django import forms

from .models import Article

class ArticleModelForm(forms.ModelForm):
	class Meta:
		model = Article
		fields = [
			'title',
			'content',
			'active'
		]



# FOR FUNCTION BASED VIEWS

# class ArticleForm(forms.ModelForm):
# 	title = forms.CharField(
# 				label='',
# 				widget=forms.TextInput(
# 					attrs={
# 						"placeholder": "Title"
# 					}
# 				)
# 			)
# 	content = forms.CharField(
# 				required=False,
# 				label='',
# 				widget=forms.Textarea(
# 					attrs={
# 						"class": "my-article-form-class",
# 						"id": "my-article-form-id",
# 						"placeholder": "Content",
# 						"rows": 40,
# 						"cols": 200
# 					}
# 				)
# 			)
# 	active = forms.BooleanField(required=False)
# 	class Meta:
# 		model = Article
# 		fields = [
# 			'title',
# 			'content',
# 			'active'
# 		]

# 	def clean_title(self, *args, **kwargs):
# 		title = self.cleaned_data.get("title")
# 		return title
