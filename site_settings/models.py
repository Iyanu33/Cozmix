from django.db import models
from colorfield.fields import ColorField
# Create your models here.

class SiteLogo(models.Model):
    logo = models.ImageField(upload_to='site_logo',null=True,blank=True)

class Banner(models.Model):
    image = models.ImageField(upload_to='banners')
    title = models.CharField(max_length=255)
    description = models.TextField()

class SiteInfo(models.Model):
    contact_email = models.EmailField(default='YourEmail')
    contact_phone = models.CharField(max_length=20,default='YourPhoneNo')
    about_us = models.TextField(null=True,blank=True)
    brand=models.CharField(max_length=255,default='MyBrand')
    nav_col=ColorField(default='#c9c3c3')
    footer_bg_col=ColorField(default='#c9c3c3')
    bg_col=ColorField(default='#ffffff')

class Footer(models.Model):
    copyright_text = models.CharField(max_length=255,null=True,blank=True)

class SocialMedia(models.Model):
    platform=models.CharField(max_length=50)
    link=models.URLField()
    footer=models.ForeignKey('Footer',on_delete=models.CASCADE,related_name='social_media_links')
    
