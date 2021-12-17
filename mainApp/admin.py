from django.contrib import admin
from django.contrib.auth.models import Group
from .models import (BeliefContent, Gallery, MinisterProfile,OurBelief,
    MissionContent,OurMission,
    OurChurch,ChurchContent, PaymentMethods, Resource, Sliders,Events,
    Sermon,SermonContent,
    PastorAndWifeDetailAtFrontPage,Ourgroups
    )
# Register your models here.


admin.site.site_header ="Admin Dashboard"
admin.site.site_title = "Admin Dashboard"
admin.site.index_title = "Welcome to Your Admin Dashboard"

admin.site.unregister(Group)
admin.site.register(Ourgroups)


class OurBeliefContent(admin.TabularInline):
    model =BeliefContent
    extra=1

class OurBeliefAdmin(admin.ModelAdmin):
    fieldsets=[(None,{'fields':['heading',]})]
    inlines=[OurBeliefContent]





admin.site.register(OurBelief,OurBeliefAdmin)



class OurMissionContent(admin.TabularInline):
    model =MissionContent
    extra=1

class OurMissionAdmin(admin.ModelAdmin):
    fieldsets=[(None,{'fields':['heading',]})]
    inlines=[OurMissionContent]




admin.site.register(OurMission,OurMissionAdmin)




class OurChurchContent(admin.TabularInline):
    model =ChurchContent
    extra=1

class OurChurchAdmin(admin.ModelAdmin):
    fieldsets=[(None,{'fields':['heading',]})]
    inlines=[OurChurchContent]



class SermonContent(admin.TabularInline):
    model =  SermonContent
    extra=1

class SermonAdmin(admin.ModelAdmin):
    fieldsets=[(None,{'fields':['title',]})]
    inlines=[SermonContent]



admin.site.register(Sermon,SermonAdmin)

admin.site.register(OurChurch,OurChurchAdmin)



admin.site.register(MinisterProfile)

admin.site.register(Sliders)

admin.site.register(Gallery)
admin.site.register(PaymentMethods)


admin.site.register(Events)
# PastorAndWifeDetailAtFrontPage,Ourgroups
admin.site.register(PastorAndWifeDetailAtFrontPage)



admin.site.register(Resource)