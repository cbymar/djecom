from django import forms

class ContactForm(forms.Form):
    fullname = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control", "id": "form_full_name"
    }))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            "class": "form-control",
            "placeholder": "Enter email @",
        }))
    content = forms.CharField(
        widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "your message here",
        }))
