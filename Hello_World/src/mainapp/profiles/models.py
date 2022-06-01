from django.db import models

TYPE_CHOICES = {
    ('Mr','Mr'),
    ('Mrs','Mrs'),
    ('Ms','Ms'),
    ('Miss','Miss'),
}


# Create your models here.
class Profile (models.Model):
    Prefixes = models.CharField(max_length=60, default="", choices= TYPE_CHOICES)
    Firstname = models.CharField(max_length=60, default="", blank=True, null=False)
    Lastname = models.CharField(max_length=60, default="", blank=True, null=False)
    e_mail = models.CharField(max_length=60, default="", blank=True, null=False)
    username = models.CharField(max_length=60, default="", blank=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return self.Firstname



