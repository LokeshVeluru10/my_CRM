from django.shortcuts import render

# Create your views here.

def base(request):
    return render(request,'base.html')

def activities(request):
    return render(request,'activities.html')

def Opportunities(request):
    return render(request,'Opportunities.html')

def job_opportunities(request):
    return render(request,'job_opportunities.html')

def internship_opportunities(request):
    return render(request,'internship_opportunities.html')

def hackathon(request):
    return render(request, 'hackathon.html')

def team_building(request):
    return render(request, 'team_building.html')

def tech_talks(request):
    return render(request, 'tech_talks.html')

def workshops(request):
    return render(request, 'workshops.html')

def training_sessions(request):
    return render(request, 'training_sessions.html')

def networking_events(request):
    return render(request, 'networking_events.html')

def signup(request):
    return render(request, 'signup.html')

def signin(request):
    return render(request, 'signin.html')

def About_us(request):
    return render(request, 'About_us.html')

def admin_home(request):
    return render(request, 'admin_home.html')

def settings(request):
    return render(request, 'settings.html')

def update_profile(request):
    return render(request, 'update_profile.html')

def change_password(request):
    return render(request, 'change_password.html')

def site_settings(request):
    return render(request, 'site_settings.html')

def change_password(request):
    return render(request, 'change_password.html')

def employees(request):
    return render(request, 'employees.html')

def add_employee(request):
    return render(request, 'add_employee.html')

