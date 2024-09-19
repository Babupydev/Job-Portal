from django import forms
from accounts.models import RecruiterProfile,CandidateProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = RecruiterProfile
        fields = ['company_name', 'company_website']
class CandidateProfileForm(forms.ModelForm):
    class Meta:
        model = CandidateProfile
        fields = ['resume', 'phone_number', 'address', 'skills', 'education', 'experience',
                  'linkedin_profile', 'portfolio', 'date_of_birth', 'preferred_locations', 
                  'expected_salary', 'availability', 'professional_summary', 'certifications', 
                  'languages']
        
# Post a Job

from django import forms
from .models import Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'company_name', 'location', 'job_type', 'description', 'salary', 'requirements', 'last_date_to_apply']
        widgets = {
            'last_date_to_apply': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 4}),
            'requirements': forms.Textarea(attrs={'rows': 4}),
        }


from django import forms
from .models import Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'company_name', 'location', 'job_type', 'description', 'salary', 'requirements', 'last_date_to_apply']
