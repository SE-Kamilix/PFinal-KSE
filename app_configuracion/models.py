from django.db import models

# Create your models here.

class SiteSettings(models.Model):
    site_name = models.CharField(max_length=100)
    site_description = models.TextField()
    contact_email = models.EmailField()

    def __str__(self):
        return self.site_name
