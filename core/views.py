from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import RecruiterProfile, CandidateProfile

@login_required
def index_view(request):
    if hasattr(request.user, 'recruiterprofile'):
        return redirect('recruiter_dashboard')
    elif hasattr(request.user, 'candidateprofile'):
        return redirect('candidate_dashboard')
    else:
        # Render a page or a template with the message
        return render(request, 'index.html', {
            'error_message': 'Your profile type is not defined. Please contact support.'
        })

@login_required
def profile_view(request):
    return render(request, 'core/profile.html',{'user': request.user})

@login_required
def candidate_dashboard(request):
    return render(request, 'core/candidate_dashboard.html')

# @login_required
# def recruiter_dashboard(request):
#     return render(request, 'core/recruiter_dashboard.html')

# Recruiter Dashboard

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Job, Application

@login_required
def recruiter_dashboard(request):
    user = request.user

    if not hasattr(user, 'recruiterprofile'):
        return redirect('create_recruiter_profile')

    job_count = Job.objects.filter(posted_by=user).count()
    active_jobs = Job.objects.filter(posted_by=user).count()  # Adjust if necessary
    application_count = Application.objects.filter(job__posted_by=user).count()
    recent_jobs = Job.objects.filter(posted_by=user).order_by('-date_posted')[:5]
    recent_applications = Application.objects.filter(job__posted_by=user).order_by('-date_applied')[:5]

    context = {
        'job_count': job_count,
        'active_jobs': active_jobs,
        'application_count': application_count,
        'recent_jobs': recent_jobs,
        'recent_applications': recent_applications,
    }
    
    return render(request, 'core/recruiter_dashboard.html', context)


# Post a Job

from django.shortcuts import render, redirect
from .forms import JobForm
from django.contrib.auth.decorators import login_required

@login_required
def create_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.posted_by = request.user
            job.save()
            return redirect('recruiter_dashboard')  # Redirect to the recruiter dashboard after job post
    else:
        form = JobForm()
    
    return render(request, 'core/create_job.html', {'form': form})

from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Job
from .forms import JobForm  # Ensure you have a form for editing jobs

@login_required
def edit_job(request, job_id):
    job = get_object_or_404(Job, id=job_id, posted_by=request.user)

    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('recruiter_dashboard')
    else:
        form = JobForm(instance=job)

    return render(request, 'core/edit_job.html', {'form': form})

@login_required
def delete_job(request, job_id):
    job = get_object_or_404(Job, id=job_id, posted_by=request.user)
    if request.method == 'POST':
        job.delete()
        return redirect('recruiter_dashboard')

    return render(request, 'core/confirm_delete.html', {'job': job})


