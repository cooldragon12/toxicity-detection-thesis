from django import forms
from django.forms import inlineformset_factory

from .models import Entry, PlayerDemography

RANK_CHOICES = (
    ("Iron 1", "Iron 1"),
    ("Iron 2", "Iron 2"),
    ("Iron 3", "Iron 3"),
    ("Bronze 1", "Bronze 1"),
    ("Bronze 2", "Bronze 2"),
    ("Bronze 3", "Bronze 3"),
    ("Silver 1", "Silver 1"),
    ("Silver 2", "Silver 2"),
    ("Silver 3", "Silver 3"),
    ("Gold 1", "Gold 1"),
    ("Gold 2", "Gold 2"),
    ("Gold 3", "Gold 3"),
    ("Platinum 1", "Platinum 1"),
    ("Platinum 2", "Platinum 2"),
    ("Platinum 3", "Platinum 3"),
    ("Diamond 1", "Diamond 1"),
    ("Diamond 2", "Diamond 2"),
    ("Diamond 3", "Diamond 3"),
    ("Ascendant 1", "Ascendant 1"),
    ("Ascendant 2", "Ascendant 2"),
    ("Ascendant 3", "Ascendant 3"),
    ("Immortal 1", "Immortal 1"),
    ("Immortal 2", "Immortal 2"),
    ("Immortal 3", "Immortal 3"),
    ("Radiant", "Radiant"),
)
SERVER_CHOICES = (
    ("Singapore", "Singapore"),
    ("Tokyo", "Tokyo"),
    ("Hong Kong", "Hong Kong"),
)
GENDER_CHOICES = (
    ("Male", "male"),
    ("Female", "female"),
    ("Other", "other"),
)


class PlayerDemographyForm(forms.ModelForm):
    in_game_rank = forms.ChoiceField(choices=RANK_CHOICES, required=True, label="What is your in-game rank?")
    often_server = forms.ChoiceField(
        choices=SERVER_CHOICES, required=True, label="In which server do you play the most?"
    )
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=GENDER_CHOICES)

    class Meta:
        model = PlayerDemography
        fields = [
            "email",
            "name",
            "gender",
            "age",
            "country",
            "province",
            "username",
            "average_hours",
            "frequency",
            "in_game_rank",
            "often_server",
        ]


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ["text", "screenshot", "description"]
        widgets = {
            "id": forms.HiddenInput(),
        }


class EntryFormset(forms.BaseInlineFormSet):
    def clean(self):
        super().clean()
        any_field_filled = False
        for form in self.forms:
            screenshot = form.cleaned_data.get("screenshot")
            text = form.cleaned_data.get("text")
            print(screenshot)
            if screenshot or text:
                any_field_filled = True
                break

        if any_field_filled:
            raise forms.ValidationError("At least one field must be filled.")


EntryFormSet = inlineformset_factory(
    PlayerDemography, Entry, form=EntryForm, formset=EntryFormset, extra=1, can_delete=False, validate_min=1
)
