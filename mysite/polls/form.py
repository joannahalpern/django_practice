from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime  # for checking renewal date range.


class RenewBookForm(forms.Form):
    sort_choice = forms.ChoiceField(label='helloooo', help_text="yo ;)")