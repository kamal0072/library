from .models import Book
from django import forms

class BookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__" 
        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'picture' : forms.FileInput(attrs={'class' : 'form-control'}),
            'author' : forms.TextInput(attrs={'class' : 'form-control'}),
            'email' : forms.EmailInput(attrs={'class' : 'form-control'}),
            'describe' : forms.TextInput(attrs={'class' : 'form-control'}),
            'book_soft_copy' : forms.FileInput(attrs={'class' : 'form-control'}),
        }