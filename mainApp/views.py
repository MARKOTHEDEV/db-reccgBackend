from django.shortcuts import render
from rest_framework.decorators import api_view
from . import models
from rest_framework.response import  Response
from rest_framework import status







@api_view(['GET'])
def resourcePage(request):

    data = models.Resource.objects.all().values()



    return Response({"message":True,"data":data},status=status.HTTP_200_OK)




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
            {"id":event.id,'image':Imageurl,"name":event.name}
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


@api_view(['GET'])
def get_our_beliefDetail(request,id=None):
    "get our belief detail"
    data = dict()
    if not models.OurBelief.objects.filter(id=id).exists():return Response({'message':False},status=status.HTTP_404_NOT_FOUND)
    our_belief = models.OurBelief.objects.get(id=id)
    data ={
        "id":our_belief.id,
        'all_content':our_belief.beliefcontent_set.all().values()
    }

    return Response({'message':True,"data":data},status=status.HTTP_200_OK)

@api_view(['GET'])
def all_church_groups(request):
    data =[]
    

    for church_group in models.Ourgroups.objects.all():
        data.append({"id":church_group.id,"heading":church_group.heading,"phone_number":church_group.phone_number,
            "content":church_group.content
        })
    

    return  Response({"message":True,"data":data},status=status.HTTP_200_OK)


@api_view(['GET'])
def getFrontPagePastorData(request):
    pastor_front_data = models.PastorAndWifeDetailAtFrontPage.objects.all().first()
    data = dict()
    pastor_image=''
    pastor_wife_image=''

    if pastor_front_data is not None:
        try:pastor_wife_image=pastor_front_data.pastor_wife_image.url
        except:pastor_wife_image=''

        try:pastor_image=pastor_front_data.pastor_image.url
        except:pastor_image=''
        data={
            "pastor_wife_image":pastor_wife_image,
            "pastor_image":pastor_image,
            "id":pastor_front_data.id,
            "content":pastor_front_data.content,
            "header":pastor_front_data.header
        }

    
    return  Response({"message":True,"data":data},status=status.HTTP_200_OK)
