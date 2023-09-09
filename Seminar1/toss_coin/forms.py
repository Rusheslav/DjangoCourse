from django import forms


class ChooseGameForm(forms.Form):
    game_choices = (
        ('HeadTails', 'HeadTails'),
        ('Dice', 'Dice'),
        ('Randomizer', 'Randomizer')
    )
    game = forms.ChoiceField(choices=game_choices, widget=forms.Select(attrs={'class': 'form-select'}))
    count = forms.IntegerField(min_value=1, max_value=64, widget=forms.NumberInput(attrs={'class': 'form-select'}))
