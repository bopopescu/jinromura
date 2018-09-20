from django import forms

class SearchForm(forms.Form):
    people = forms.IntegerField(
        label='人数',
        min_value=5,
        max_value=15,
    )
