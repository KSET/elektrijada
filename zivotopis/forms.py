# -*- coding: utf-8 -*-
from django import forms
from zivotopis.models import CurriculumVitae


class CVForm(forms.ModelForm):
    born = forms.RegexField(label=u'Godina rođenja', regex=r'^\d{4}$', error_messages={'invalid': u'Unesite ispravanu godinu od 4 znamenke (bez točke).'})
    graduation = forms.RegexField(label=u'Planirana godina diplomiranja', regex=r'^\d{4}$', error_messages={'invalid': u'Unesite ispravanu godinu od 4 znamenke (bez točke).'})
    phone = forms.RegexField(label=u'Broj mobitela', regex=r'^\d+$', required=False, error_messages={'invalid': u'Unesite ispravan broj (samo znamenke).'})

    class Meta:
        model = CurriculumVitae
        exclude = ('created', 'visible')
