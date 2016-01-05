from __future__ import unicode_literals

from django.db import models
from django.core.validators import RegexValidator
from django_markdown.models import MarkdownField
from profiles.models import Profile

class News(models.Model):
    CHOICE = [('C', 'Campus News'),
            ('N', 'In the News'),
            ('S', 'Spotlight'),
            ]
    title = models.CharField(max_length=300)
    details = models.CharField(max_length=2000)
    category = models.CharField(max_length=1, choices=CHOICE)
    timestamp = models.DateTimeField(auto_now_add=True)
    pinned = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Club(models.Model):
    user = models.ForeignKey(Profile)
    convenor = models.CharField(max_length=100)
    strength = models.IntegerField()

    def __str__(self):
        return self.user.user.get_full_name

class Member(models.Model):
    user = models.ForeignKey(Profile)
    BRANCH_LIST = [('CH', 'Chemical Engineering'),
                   ('CO', 'Computer Engineering'),
                   ('CV', 'Civil Engineering'),
                   ('EC', 'Electronics and Communications Engineering'),
                   ('EE', 'Elelctrical and Electronics Engineering'),
                   ('IT', 'Information Technology'),
                   ('ME', 'Mechanical Engineering'),
                   ('MN', 'Mining Engineering'),
                   ('MT', 'Materials and Metallurgical Engineering'),
                   ]
    branch = models.CharField(max_length=2, choices=BRANCH_LIST)
    email = models.EmailField()
    address = models.CharField(max_length=1000)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(max_length=15, validators=[phone_regex], blank=True)

    def __str__(self):
        return self.user.user.get_full_name


class Events(models.Model):
    title = models.CharField(max_length=200)
    organizer = models.ForeignKey(Club)
    details = models.CharField(max_length=2000)
    date = models.DateTimeField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    contact = models.CharField(max_length=15, validators=[phone_regex], blank=True)

    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=50)
    prof_pic = models.ImageField(upload_to='author_profile_pics/%Y-%m-%d/',null=True,blank=True)
    blurb = MarkdownField()

    def __str__(self):
        return self.name

class Articles(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author)
    content = MarkdownField()
    published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Complaint(models.Model):
    choice = [('H', 'HCC'),
            ('S', 'Security'),
            ('L', 'LAN'),
            ('P', 'Sports'),
            ('E', 'Eateries'),
            ('I', 'Independent Bodies'),
            ('A', 'Academics'),
            ('M', 'Miscellaneous'),
            ]
    complaint = models.CharField(max_length=300)
    details = models.CharField(max_length=2000)
    date = models.DateTimeField(auto_now_add=True)
    ctype = models.CharField(max_length=1, choices=choice)

    def __str__(self):
        return self.complaint
