from django import forms

class SearchForm(forms.Form):
    search_text = forms.CharField(
        label = "検索ワード",
        max_length='50',
        required = True,
        widget = forms.TextInput()
    )