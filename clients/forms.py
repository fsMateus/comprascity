from django import forms
from .models import Company
from django.core.exceptions import ValidationError
from validate_docbr import CNPJ, validate_docs


class FormCompany(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        forms.ModelForm.__init__(self, *args, **kwargs)

        self.fields['cnpj'] = forms.CharField()

    class Meta:
        model = Company
        fields = (
            'cnpj',
        )

    def clean_cnpj(self):
        data = self.cleaned_data['cnpj']

        docs = [(CNPJ, data), ]
        if True not in validate_docs(docs):
            raise ValidationError("O valor informado não corresponde há um CNPJ válido!")

        return data