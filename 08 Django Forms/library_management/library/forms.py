from django import forms
from .models import Book, Author, Publisher

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, help_text="Your full name")
    email = forms.EmailField(help_text="Your email address")
    message = forms.CharField(widget=forms.Textarea, help_text="Enter your message here")

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if len(name) < 3:
            raise forms.ValidationError("Name must be at least 3 characters long.")
        return name


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter author name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter author email'}),
        }
        error_messages = {
            'name': {
                'required': "Author name is required.",
                'max_length': "Author name is too long.",
            },
            'email': {
                'invalid': "Please enter a valid email address.",
            },
        }
        help_texts = {
            'name': 'The name should be full and unique.',
            'email': 'This email will be unique to each author.',
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if "example.com" in email:
            raise forms.ValidationError("Emails from 'example.com' are not allowed.")
        return email

from .models import Book
from django.utils.text import slugify


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publisher', 'publication_date', 'slug']
        widgets = {
            'publication_date': forms.SelectDateWidget(years=range(1900, 2100)),
            'slug': forms.TextInput(attrs={'placeholder': 'Leave blank to auto-generate'}),
        }
        error_messages = {
            'title': {
                'required': "Title is required.",
                'max_length': "Title is too long.",
            },
            'publication_date': {
                'invalid': "Enter a valid date.",
            },
        }

    def clean_slug(self):
        slug = self.cleaned_data.get('slug')
        if not slug:
            slug = slugify(self.cleaned_data.get('title'))
        return slug
    

class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name', 'address', 'slug']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': "Publisher's Name"}),
            'address': forms.Textarea(attrs={'placeholder': "Publisher's Address"}),
            'slug': forms.TextInput(attrs={'placeholder': "Slug (auto-generated if blank)"}),
        }
        help_texts = {
            'name': 'Enter the full name of the publisher.',
            'address': 'Optional: Enter the publisher’s address if available.',
        }
        error_messages = {
            'name': {
                'required': "Publisher name is required.",
                'max_length': "Name is too long.",
            },
            'slug': {
                'unique': "This slug is already in use. Please choose a different one.",
            },
        }

    def clean_slug(self):
        # Auto-generate slug if not provided
        slug = self.cleaned_data.get('slug')
        if not slug:
            slug = slugify(self.cleaned_data.get('name'))
        return slug
