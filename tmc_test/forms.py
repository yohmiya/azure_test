from django import forms

class SearchForm(forms.Form):
    search_text = forms.CharField(
        label = "検索テキスト",
        max_length='50',
        required = False,
        widget = forms.TextInput()
    )