from django import forms

class SearchForm(forms.Form):
    people = forms.IntegerField(
        label='人数',
        min_value=5,
        max_value=15,
        required=False,
    )

    level = forms.IntegerField(
        label='難易度',
        min_value=1,
        max_value=5,
        required=False,
    )

    CHARA_CHOICES= (
    ('fox', '妖狐'),
    ('nekomata', '猫又'),
    ('black_cat', '黒猫'),
)

    chara = forms.ChoiceField(
            label='キャラ',
            widget=forms.Select,
            choices=CHARA_CHOICES,
            required=True,
        )
