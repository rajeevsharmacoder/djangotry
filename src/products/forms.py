from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
	title = forms.CharField(
				label='',
				widget=forms.TextInput(
					attrs={
						"placeholder": "Title"
					}
				)
			)
	# email = forms.EmailField()
	# description = forms.CharField(
	# 				required=False, 
	# 				label='',
	# 				widget=forms.Textarea(
	# 					attrs={
	# 						"class": "new-class-name-two",
	# 						"id": "my-id-for-text-area",
	# 						"rows": 15,
	# 						"cols": 100,
	# 						"placeholder": "Description"
	# 					}
	# 				)
	# 			)
	price = forms.DecimalField(initial=199.99)
	summary = forms.CharField(required=False)
	featured = forms.BooleanField(required=False)
	class Meta:
		model = Product
		fields = [
			'title',
			'description',
			'price',
			'summary',
			'featured'
		]

	def clean_title(self, *args, **kwargs):
		title = self.cleaned_data.get("title")
		# if not "RSC" in title:
		# 	raise forms.ValidationError("This is not a valid title")
		# if not "NEWS" in title:
		# 	raise forms.ValidationError("This is not a valid title")
		return title

	# def clean_email(self, *args, **kwargs):
	# 	email = self.cleaned_data.get("email")
	# 	if not email.endswith('edu'):
	# 		raise forms.ValidationError("This is not a .edu email")
	# 	return email

class RawProductForm(forms.Form):
	title = forms.CharField(
				label='',
				widget=forms.TextInput(
					attrs={
						"placeholder": "Title"
					}
				)
			)
	description = forms.CharField(
					required=False, 
					label='',
					widget=forms.Textarea(
						attrs={
							"class": "new-class-name-two",
							"id": "my-id-for-text-area",
							"rows": 15,
							"cols": 100,
							"placeholder": "Description"
						}
					)
				)
	price = forms.DecimalField(initial=199.99)
	summary = forms.CharField(required=False)
	featured = forms.BooleanField(required=False)
