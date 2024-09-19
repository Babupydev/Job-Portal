from django.urls import path
from . import views 
from .views import candidate_signup



urlpatterns = [
    path('home/', views.home_view, name='home'),
    path('signup/', views.signup_select, name='signup_select'),
    path('signup/candidate/', candidate_signup.as_view(), name='candidate_signup'),
    path('signup/recruiter/', views.recruiter_signup, name='recruiter_signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile_edit', views.edit_profile, name='edit_profile'),
    
    
]
