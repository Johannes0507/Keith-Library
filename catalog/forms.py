# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 23:51:40 2023

@author: KeithLee
"""

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import datetime


class RenewBookForm(forms.Form):
    renew_date = forms.DateField(help_text="輸入續借日期，時間要小於四個禮拜(預設是三個禮拜)。")

    def clean_renew_date(self):
        data = self.cleaned_data['renew_date']
        
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))

        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))
            
        return data