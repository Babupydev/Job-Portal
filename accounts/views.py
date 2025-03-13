from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid email or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

# logout view

from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse

def logout_view(request):
    logout(request)  # Logs out the user
    return render(request, 'accounts/logout.html')  # Redirect to the logout page


def home_view(request):
    return render(request,'index.html')
# 
from django.shortcuts import render
from django.http import HttpResponse

def signup_select(request):
    # This will render the signup selection page
    return render(request, 'accounts/signup_select.html')


# Logic for recruiter signup will go here
    
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RecruiterSignupForm


from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views import View
from .forms import RecruiterSignupForm, CandidateSignupForm

def recruiter_signup(request):
    if request.method == 'POST':
        form = RecruiterSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login or another page after successful signup
    else:
        form = RecruiterSignupForm()

    return render(request, 'accounts/recruiter_signup.html', {'form': form})

class candidate_signup(View):
    def get(self, request):
        form = CandidateSignupForm()
        return render(request, 'accounts/candidate_signup.html', {'form': form})

    def post(self, request):
        form = CandidateSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to a page after successful signup
        return render(request, 'accounts/candidate_signup.html', {'form': form})


#Edit profile

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user.profile)
    return render(request, 'accounts/edit_profile.html', {'form': form})
