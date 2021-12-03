
from django.urls import path
from . import views

urlpatterns  =[
    path('all-ministers/', views.get_all_misters),   
    path('all-sliders/', views.get_sliders),
    path('all-events/', views.get_all_events),
    path('church-detail/',views.get_our_church),
    path('mission-detail/',views.get_our_mission),
    path('belief-detail/',views.get_our_belief),
    path('all-gallery/', views.get_all_gallery),
    path('all_church_groups/',views.all_church_groups),
    path('getFrontPagePastorData/',views.getFrontPagePastorData),

]