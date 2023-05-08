from django import forms
from .models import JobSeeker

class JobSeekerForm(forms.ModelForm):
    class Meta:
        model = JobSeeker
        fields = ('first_name', 'last_name', 'email', 'phone', 'address', 'resume')
