from django.shortcuts import render
from rest_framework.decorators import api_view
from . import models
from rest_framework.response import  Response
from rest_framework import status

@api_view(['GET'])
def get_all_misters(request):
    all_minsters = []
    Imageurl =''
    for minster in models.MinisterProfile.objects.all():
            try:Imageurl =minster.minister_image.url
            except:Imageurl=""
            all_minsters.append(
                {
                    "id":minster.id,
                    "position":minster.position,
                    "name":minster.name,
                    "paragraph":minster.paragraph,
                    "minister_image":Imageurl,
                }
            )


    return  Response({"message":True,"data":all_minsters},status=status.HTTP_200_OK)
@api_view(['GET'])
def get_sliders(request):
    all_sliders = []
    Imageurl =''
    for slider in models.Sliders.objects.all():
        try:Imageurl=slider.image.url
        except:Imageurl=''

        all_sliders.append(
            {"id":slider.id,"image":Imageurl}
        )
    
    return  Response({"message":True,"data":all_sliders},status=status.HTTP_200_OK)


# def get_all_publications(request):
#     data = []

#     imageurl =''
#     for publication in models.Publications
#     return Response({"message":True,"data":data},status=status.HTTP_200_OK)


@api_view(['GET'])
def get_all_events(request):
    Imageurl =''
    all_event =[]
    for event in models.Events.objects.all():
        try:Imageurl=event.image.url
        except:Imageurl=''

        all_event.append(
            {"id":event.id,'image':Imageurl}
        )

    return  Response({"message":True,"data":all_event},status=status.HTTP_200_OK)


@api_view(['GET'])
def get_all_gallery(request):
    all_gallery= []
    Imageurl =''

    for gallery in models.Gallery.objects.all():
        try:Imageurl=gallery.image.url
        except:Imageurl=''

        all_gallery.append({'id':gallery.id,'image':Imageurl})


    return Response({"message":True,"data":all_gallery},status=status.HTTP_200_OK)

@api_view(['GET'])
def get_our_church(self):
    data =dict()
    church = models.OurChurch.objects.all().first()
    if church is not None:
        data={
        "id":church.id,
        "heading":church.heading,
        "content":church.churchcontent_set.all().values()
    }
    
    return Response({'message':True,"data":data},status=status.HTTP_200_OK)

@api_view(['GET'])
def get_our_mission(self):
    mission = models.OurMission.objects.all().first()
    data=dict()
    if mission is not None:
        data={
        "id":mission.id,
        "heading":mission.heading,
        "content":mission.missioncontent_set.all().values()
    }
    return Response({'message':True,"data":data},status=status.HTTP_200_OK)


@api_view(['GET'])
def get_our_belief(self):
    our_belief = models.OurBelief.objects.all().first()
    data = dict()
    if our_belief is not None:
        data={
        "id":our_belief.id,
        "heading":our_belief.heading,
        "content":our_belief.beliefcontent_set.all().values()
    }

    return Response({'message':True,"data":data},status=status.HTTP_200_OK)