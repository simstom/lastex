from django.db import models

# Create your models here.

# class FileUpload_1(models.Model):
#     title = models.TextField(max_length=40, null=True)
#     imgfile = models.ImageField(null=True, upload_to="", blank=True)
#     content = models.TextField()

#     def __str__(self):
#         return self.title


class Profile(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    # blank=True, upload_to="images", null=True
    
    def __str__(self):
        return self.title
