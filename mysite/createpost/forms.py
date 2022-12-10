from django import forms

class CreateUserPost(forms.Form):
    user = forms.CharField( max_length=50, widget=forms.TextInput(attrs={
            "placeholder": "Username",
            "class": "form-control",
        }))
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
            "placeholder": "Title",
            "class": "form-control",
        }))
    details = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
            "placeholder": "Details",
            "class": "form-control",
        }))