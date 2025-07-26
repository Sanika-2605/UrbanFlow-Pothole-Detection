from django import forms
from .models import PotholeReport
from .models import Pothole


class PotholeReportForm(forms.ModelForm):
    latitude = forms.FloatField(widget=forms.HiddenInput())
    longitude = forms.FloatField(widget=forms.HiddenInput())

    class Meta:
        model = PotholeReport
        fields = ['image', 'video', 'latitude', 'longitude']

    def clean(self):
        cleaned_data = super().clean()
        image = cleaned_data.get("image")
        video = cleaned_data.get("video")
        if not image and not video:
            raise forms.ValidationError("Please upload an image or a video.")

class PotholeForm(forms.ModelForm):
    class Meta:
        model = Pothole
        fields = ['depth', 'height', 'width', 'latitude', 'longitude']