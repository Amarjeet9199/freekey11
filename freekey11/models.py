from django.db import models
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    Name=models.CharField(max_length=200)
    Email=models.EmailField(max_length=140,blank=False)
    Message=models.TextField(max_length=500,default='type query here.....')

    def __str__(self):
        return self.Name

    def get_absolute_url(self):
        return reverse('home')

# Create your models here.
class ImgView(models.Model):
    img_name = models.CharField(max_length=50)
    img_uplaod = models.ImageField(upload_to='images')

    def __str__(self):
        return(self.img_name)

class Detail_View(models.Model):
     Message=models.TextField(max_length=2000,default='type query here.....')