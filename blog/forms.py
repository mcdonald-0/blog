from django import forms
from django.forms import ModelForm, Textarea

# from ckeditor.fields import RichTextField

from .models import *
from .dates import *

class DatePicker(forms.DateInput):
	input_type = 'date'
		

class EditProfileForm(ModelForm):
	first_name = forms.CharField(
        widget=forms.TextInput(attrs={
        	'placeholder': 'First name' , 
        	'class': 'form-control',
        	})
        )
	middle_name = forms.CharField(
		required=False,
        widget=forms.TextInput(attrs={
        	'placeholder': 'Middle name' , 
        	'class': 'form-control',
        	})
        )
	last_name = forms.CharField(
        widget=forms.TextInput(attrs={
        	'placeholder': 'Last name', 
        	'class': 'form-control',
        	})
        )
	email = forms.EmailField(
        widget=forms.EmailInput(attrs={
        	'placeholder': 'Email', 
        	'class': 'form-control',
        	})
        )

	birthdate = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEARS))

	bio = forms.CharField(
		widget=forms.Textarea(attrs={
			'class': 'form-control', 
			'rows': 3, 
			'placeholder': 'Write a little about your self!'
			})
		)

	GENDER_CHOICES = (
    		('M', 'Male'),
    		('F', 'Female'),
    	)
	gender = forms.ChoiceField(
		label="",
		choices=GENDER_CHOICES,
        widget=forms.RadioSelect(),
        )

	class Meta:
		model = UserProfile
		fields = '__all__'
		exclude = ['user']


class BlogPostForm(ModelForm):
	title = forms.CharField(
		label="",
        widget=forms.TextInput(attrs={
        	'placeholder': 'Blog Title', 
        	'class': 'form-control'})
        )
	short_description = forms.CharField(
		label="",
		widget=forms.Textarea(attrs={
			'class': 'form-control', 
			'rows': 2, 
			'placeholder': 'Write a short description about your post'
			})
		)
	content = forms.CharField(
		label="",
		widget=forms.Textarea(attrs={
			'class': 'form-control', 
			'rows': 8, 
			'placeholder': 'Your content goes here!'
			})
		)

	class Meta:
		model = BlogPost
		fields = '__all__'
		exclude = ['author', 'likes']


class CommentForm(ModelForm):
	body = forms.CharField(
		widget=forms.Textarea(attrs={
			'class': 'form-control', 
			'rows': 3, 
			'placeholder': 'Join the discussion and leave a comment!'
			})
		)
	class Meta:
		model = Comment
		fields = ['body']

	
class SearchForm(ModelForm):
	author = forms.ModelChoiceField(
		queryset=UserProfile.objects.all(),
		label='',
		required=False,
		)
	title = forms.CharField(
		label="",
		required=False,
        widget=forms.TextInput(attrs={
        	'placeholder': 'Title', 
        	'class': 'form-control'})
        )
	short_description = forms.CharField(
		label="",
		required=False,
        widget=forms.TextInput(attrs={
        	'placeholder': 'Short description', 
        	'class': 'form-control'})
        )
	category = forms.ModelChoiceField(
		queryset=Category.objects.all(),
		label='',
		required=False,
		)
	class Meta:
		model = BlogPost
		fields = '__all__'
		exclude = ['likes', 'related_image', 'date_added', 'content']
