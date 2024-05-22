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