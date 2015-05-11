# -*- coding: utf-8 -*-
from django import forms
from django.utils.timezone import now
from zivotopis.models import CurriculumVitae


class CVForm(forms.ModelForm):
    born = forms.RegexField(label=u'Godina rođenja', regex=r'^\d{4}$',
                            error_messages={'invalid': u'Unesite ispravanu godinu od 4 znamenke (bez točke).'})
    graduation = forms.RegexField(label=u'Planirana godina diplomiranja', regex=r'^\d{4}$',
                                  error_messages={'invalid': u'Unesite ispravanu godinu od 4 znamenke (bez točke).'})
    phone = forms.RegexField(label=u'Broj mobitela', regex=r'^\d+$', required=False,
                             error_messages={'invalid': u'Unesite ispravan broj (samo znamenke).'})
    tos = forms.BooleanField(label=u'Slažem se da se moj životopis da na uvid srebrnim, zlatnim i platinastim '
                             'partnerima natjecatelja FER-a na Elektrijadi', required=True, widget=forms.CheckboxInput)

    def __init__(self, *args, **kwargs):
        super(CVForm, self).__init__(*args, **kwargs)
        self.fields['tos'].label += ' %d.' % now().year
        self.fields['email'].widget.attrs['type'] = 'email'
        self.fields['phone'].widget.attrs['type'] = 'phone'
        for name, field in self.fields.items():
            if field.required:
                field.widget.attrs['required'] = ''
                field.label += '*'

    class Meta:
        model = CurriculumVitae
        exclude = ('created', 'visible')
