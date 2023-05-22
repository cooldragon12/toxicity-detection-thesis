from django.forms import inlineformset_factory
from django import forms
from .models import PlayerDemography, Entry

RANK_CHOICES = (
        ('Iron 1', 'Iron 1'),
        ('Iron 2', 'Iron 2'),
        ('Iron 3', 'Iron 3'),
        ('Bronze 1', 'Bronze 1'),
        ('Bronze 2', 'Bronze 2'),
        ('Bronze 3', 'Bronze 3'),
        ('Silver 1', 'Silver 1'),
        ('Silver 2', 'Silver 2'),
        ('Silver 3', 'Silver 3'),
        ('Gold 1', 'Gold 1'),
        ('Gold 2', 'Gold 2'),
        ('Gold 3', 'Gold 3'),
        ('Platinum 1', 'Platinum 1'),
        ('Platinum 2', 'Platinum 2'),
        ('Platinum 3', 'Platinum 3'),
        ('Diamond 1', 'Diamond 1'),
        ('Diamond 2', 'Diamond 2'),
        ('Diamond 3', 'Diamond 3'),
        ('Ascendant 1', 'Ascendant 1'),
        ('Ascendant 2', 'Ascendant 2'),
        ('Ascendant 3', 'Ascendant 3'),
        ('Immortal 1', 'Immortal 1'),
        ('Immortal 2', 'Immortal 2'),
        ('Immortal 3', 'Immortal 3'),
        ('Radiant', 'Radiant'),
    )
SERVER_CHOICES = (
        ('Singapore', 'Singapore'),
        ('Tokyo', 'Tokyo'),
        ('Hong Kong', 'Hong Kong'),
)
GENDER_CHOICES = (
    ('Male', 'male'),
    ('Female','female'),
    ('Other','other'),
)
class PlayerDemographyForm(forms.ModelForm):
    in_game_rank = forms.ChoiceField(choices=RANK_CHOICES,required=True,label='What is your in-game rank?')
    often_server = forms.ChoiceField(choices=SERVER_CHOICES,required=True, label='In which server do you play the most?')
    gender = forms.ChoiceField(widget=forms.RadioSelect,choices=GENDER_CHOICES)
    class Meta:
        model = PlayerDemography
        fields = ['email','first_name','last_name','gender','age', 'country','province','ethnicity','username','average_hours','frequency','in_game_rank','often_server']
        
        
class EntryForm(forms.BaseInlineFormSet):
    class Meta:
        model = Entry
        fields = ['text','screenshot','description','emotion','toxicity','sentiment']
        widgets = {
            'id': forms.HiddenInput(),
        }
EntryFormSet = inlineformset_factory(PlayerDemography, Entry, exclude=['id'],extra=1, can_delete=False)