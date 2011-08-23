from django import forms

class MdForm(forms.Form):
    markdown = forms.CharField(widget=forms.Textarea)
