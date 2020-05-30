from django.db import models
from django.urls import reverse
from django.utils import timezone
# Create your models here

        

class AnthemUser(models.Model):
    name = models.CharField(max_length=200)
    department = models.CharField(max_length=200, blank=True, null=True)
    internal_ext = models.IntegerField(blank=True, null=True)
    manager = models.CharField(max_length=200, null=True)
    # picture = models.ImageField(upload_to='user_picture')

    class Meta:
        ordering = ["name"]
    

    def __str__(self):
        return self.name



class AnthemAsset(models.Model):
    asset_type = models.CharField(max_length=255, unique=False)
    asset_number = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, default='')
    anthem_user = models.OneToOneField(AnthemUser, related_name='anthem_users', on_delete=models.CASCADE,unique=True,blank=True,null=True)
    asset_picture = models.ImageField(upload_to='leet/equipment_pics',blank=True, null=True)
    manufacture_date = models.DateTimeField(blank=True, null=True)



    def __str__(self):
        return self.asset_number

    def get_absolute_url(self):
        return reverse("leet:detail", kwargs={"pk": self.pk})


    
