from django import forms

from .models import Questions, Background, Gender

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime  # for checking renewal date range.

# This gives value then name
SortOptions = (
    ('LAB', 'labor'),
    ('CAR', 'cars'),
    ('TRU', 'trucks'),
    ('WRI', 'writing'),
)

class SortForm(forms.Form):
    sort_choice = forms.ChoiceField(widget=forms.Select(attrs={'onchange': 'this.form.submit();'}), choices=SortOptions)

class BasicForm(forms.Form):
    name = forms.CharField(max_length=20, label='First Name')
    sort_choice = forms.MultipleChoiceField(choices=SortOptions)


class QuestionsForm(forms.ModelForm):
    gender = forms.ModelChoiceField(queryset=Gender.objects, empty_label=None, widget=forms.RadioSelect)

    class Meta:
        model = Questions
        exclude = ['']
        widgets = {
            'gender': forms.RadioSelect(),
            'background': forms.CheckboxSelectMultiple(),
        }

class BackgroundForm(forms.ModelForm):
    class Meta:
        model = Background
        exclude = ['']
