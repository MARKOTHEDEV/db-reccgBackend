from django.db import models



"ABout Page"
class OurBelief(models.Model):
    "for our Belief"
    # models.CharField
    heading=models.CharField(max_length=100,default='OUR BELIEFS')
    
    def __str__(self):return f'{self.heading}'

class BeliefContent(models.Model):
    ourbelief = models.ForeignKey(OurBelief,on_delete=models.CASCADE)
    paragraph = models.TextField()
    heading = models.CharField(max_length=400,default="..title")
    


class Sermon(models.Model):
    title = models.CharField(max_length=400)

    def __str__(self):return f'{self.title}'


class  SermonContent(models.Model):
    sermon = models.ForeignKey(Sermon,on_delete=models.CASCADE)
    paragraph = models.TextField()

class OurMission(models.Model):
    "for our Belief"
    heading=models.CharField(max_length=100,default='MISSION')
    
    def __str__(self):return f'{self.heading}'
    
class MissionContent(models.Model):
    paragraph = models.TextField()
    ourmission = models.ForeignKey(OurMission,on_delete=models.CASCADE)




class OurChurch(models.Model):
    "for our Belief"
    heading=models.CharField(max_length=100,default='Church')
    
    def __str__(self):return f'{self.heading}'
    
class ChurchContent(models.Model):
    ourbelief = models.ForeignKey(OurChurch,on_delete=models.CASCADE)
    paragraph = models.TextField()


"End of ABout Page"


"Minster Proifles"
class MinisterProfile(models.Model):
    minister_image = models.ImageField(upload_to='minister_profile/',blank=True)
    position = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    paragraph = models.TextField()
     

    def __str__(self):
        return f'{self.position} {self.name}'



class Sliders(models.Model):
    "hompage Slider"
    image =models.ImageField(upload_to='sldiers/')
    name =models.CharField(max_length=40)

    def __str__(self):return f'Slider {self.name}'


    class Meta:
        # verbose_name = "Registered Data"
        verbose_name_plural = "Home Page Sliders"


class Events(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to ='events/')
    
    def __str__(self):return f'{self.name}'


class Publications(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to ='events/')
    
    def __str__(self):return f'{self.name}'



class Gallery(models.Model):
    image=models.ImageField(upload_to='gallery')
    name = models.CharField(max_length=40)

    def __str__(self):return f'{self.name}'


class PaymentMethods(models.Model):
    text = models.CharField(max_length=250)
    payment_link = models.TextField()

    def __str__(self):return f'{self.payment_link}'

    class Meta:
        verbose_name_plural = "Payment Methods"
        

class PastorAndWifeDetailAtFrontPage(models.Model):
    pastor_image =models.ImageField(upload_to='PastorAndWifeDetailAtFrontPage/pastor_image/',blank=True)
    pastor_wife_image =models.ImageField(upload_to='PastorAndWifeDetailAtFrontPage/pastor_wife_image/',blank=True)
    content=models.TextField()
    header = models.CharField(max_length=200,default='Mr and Miss Anthony Aro')

    def __str__(self):return self.header


class Ourgroups(models.Model):
    "meaning list of department"
    heading=models.CharField(max_length=300,default='Enter the Depart Name')
    phone_number = models.CharField(max_length=13)
    content = models.TextField()

    def __str__(self):return self.heading




class Resource(models.Model):
    heading=models.CharField(max_length=200)
    content = models.TextField()


    def __str__(self):
        return f'{self.heading}'