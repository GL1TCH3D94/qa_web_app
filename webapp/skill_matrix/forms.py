from django import forms
from .models import Skills

class SkillModelForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = [
            'subject',
            'current_level',
            'required_level',
            'last_updated',
            'user',
        ]

    
    def clean_content(self):
        data = self.cleaned_data.get('content')
        if len(data) < 4:
            raise forms.ValidationError("This is not long enough")
        return data