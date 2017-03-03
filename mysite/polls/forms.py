from django import forms

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