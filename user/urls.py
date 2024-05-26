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
    path('About_us/', About_us, name='About_us'),
    path('signin/', signin, name='signin'),
    path('signup/', signup, name='signup'),
    path('admin_home/', admin_home, name='admin_home'),
    path('settings/', settings, name='settings'),
    path('update_profile/', update_profile, name='update_profile'),
    path('change_password/', change_password, name='change_password'),
    path('site_settings/', site_settings, name='site_settings'),
    path('change_password/', change_password, name='change_password'),
    path('employees/', employees, name='employees'),
    path('add_employee/', add_employee, name='add_employee'),

    
    
]

