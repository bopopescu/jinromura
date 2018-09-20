class SampleForm(forms.Form):
    age = forms.IntegerField(
        label='年齢',
        min_value=5,
        max_value=15,
    )
