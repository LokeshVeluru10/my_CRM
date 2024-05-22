from user.views import *
from django.urls import path

urlpatterns = [

    path('', base, name='base'),
    path('activities/', activities, name='activities'),
    path('Opportunities/', Opportunities, name='Opportunities'),
    path('job_opportunities/', job_opportunities, name='job_opportunities'),
    path('internship_opportunities/', internship_opportunities, name='internship_opportunities'),
    path('hackathon/', hackathon, name='hackathon'),
    path('team_building/', team_building, name='team_building'),
    path('tech_talks/', tech_talks, name='tech_talks'),
    path('workshops/', workshops, name='workshops'),
    path('training_sessions/', training_sessions, name='training_sessions'),
    path('networking_events/', networking_events, name='networking_events'),
]

