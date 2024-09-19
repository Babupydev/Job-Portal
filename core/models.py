from django.db import models

# Create your models here.
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.user.email

# Post a Job
from django.db import models
from django.contrib.auth import get_user_model

class Job(models.Model):
    JOB_TYPES = (
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('contract', 'Contract'),
        ('internship', 'Internship'),
    )

    title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    job_type = models.CharField(max_length=10, choices=JOB_TYPES)
    description = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    requirements = models.TextField()
    posted_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    last_date_to_apply = models.DateField()

    def __str__(self):
        return self.title

class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    applicant_name = models.CharField(max_length=255)
    date_applied = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50)  # e.g., "Pending", "Accepted", "Rejected"

    def __str__(self):
        return f"Application by {self.applicant_name} for {self.job.title}"