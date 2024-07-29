from django.db import models

# Create your models here.
class Image(models.Model):
    user = models.CharField(max_length=100, null=True, blank=True)
    tags = models.CharField(max_length=100, null=False, blank=False)
    pageURL = models.URLField(max_length=300, null=False, blank=False)
    views = models.PositiveIntegerField(null=False, blank=False)
    likes = models.PositiveIntegerField(null=False, blank=False)
    comments = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"Image by {self.user} with {self.likes} likes"
