from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, RecruiterProfile,CandidateProfile

class RecruiterSignupForm(UserCreationForm):
    company_name = forms.CharField(max_length=255, required=True)
    company_website = forms.URLField(required=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'gender', 'company_name', 'company_website', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        recruiter_profile = RecruiterProfile(
            user=user,
            company_name=self.cleaned_data['company_name'],
            company_website=self.cleaned_data['company_website']
        )
        if commit:
            recruiter_profile.save()
        return user

class CandidateSignupForm(forms.ModelForm):
    fullname = forms.CharField(max_length=255, required=True)
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = CustomUser
        fields = ('fullname','email', 'first_name', 'last_name', 'gender')
        
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        
        if password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

# edit profile

from django import forms
from .models import RecruiterProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = RecruiterProfile
        fields = ['company_name', 'company_website']

# Candidate Profile Edit Form
class CandidateProfileForm(forms.ModelForm):
    class Meta:
        model = CandidateProfile
        fields = ['resume', 'phone_number', 'address', 'skills', 'education', 'experience',
                  'linkedin_profile', 'portfolio', 'date_of_birth', 'preferred_locations', 
                  'expected_salary', 'availability', 'professional_summary', 'certifications', 
                  'languages']