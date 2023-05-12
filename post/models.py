from django.db import models
from django.utils import timezone
from django.urls import reverse

#modello del post
class post(models.Model):
    title = models.CharField(max_length=30)
    second_title = models.CharField(max_length=50)
    descriptions = models.TextField()
    cover = models.ImageField(upload_to='images')
    publis = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return  reverse('img', kwargs={'pk': self.pk})

#singola immagine
class image(models.Model):
    titolo = models.CharField(max_length=30)
    post = models.ForeignKey(post, on_delete=models.CASCADE, related_name='IMGG')
    img = models.ImageField(upload_to='imagess')
    img_publis = models.DateTimeField(default=timezone.now)
    

    def __str__(self):
        return self.titolo 
    
    def get_absolute_url(self):
        return  reverse('image', kwargs={'pk': self.pk})