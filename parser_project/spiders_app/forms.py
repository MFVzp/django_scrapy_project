from django import forms


class URLForm(forms.Form):
    spider_name = forms.CharField()
    url = forms.URLField()
