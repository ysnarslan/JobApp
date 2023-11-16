from django import forms
from uploadpp.models import UploadPP, UploadFile


class UploadPPForm(forms.ModelForm):
    class Meta:
        model = UploadPP
        fields = '__all__'


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadFile
        fields = '__all__'
