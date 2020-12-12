from django.db import models
from django.urls import reverse


# Create your models here.
# MVC - Model View Controller


def upload_location(instance, filename):
    filebase, extention = filename.split(".")
    return "%s/%s.%s" % (instance.id, instance.id, extention)
    return "%s/%s" % (instance.id, filename)


class Post(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to=upload_location, null=True, blank=True, width_field="width_field",
                              height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts_detail", kwargs={'id': self.id})

    class Meta:
        ordering = ['-timestamp', '-updated']
