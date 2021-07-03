from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User # import django users
from django.urls import reverse
# from django_quill.fields import QuillField
# from tinymce.models import HTMLField
from ckeditor_uploader.fields import RichTextUploadingField

# from rest_framework.reverse import reverse

# Create your models here.

# Article

# Officer
class Officer(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null = True, blank = True)
    position = models.CharField(max_length=200, null = True, blank = True)
    image = models.ImageField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True) # created automatically
    viewOrder = models.IntegerField(null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200, null = True, blank = True)

    def __str__(self):
        return self.name

class Article(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    officer = models.ForeignKey(Officer, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200, null = True, blank = True)
    slug = models.SlugField(null = True, blank = True, unique_for_date='publishDate')
    body = models.TextField(null=True, blank=True, editable=False)
    # TinyMCE body
    content = RichTextUploadingField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True) # created automatically
    publishDate = models.DateTimeField(default=timezone.now)
    _id = models.AutoField(primary_key=True, editable=False)
    # tags = models.ManyToManyField(Tag, null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', null=True)

    class Meta:
        ordering = ('-publishDate',)

    def __str__(self):
        return self.title

    # -- TODO: define a URL that returns /article/year/month/day/slug
    # def get_url(self):
    #     return reverse('article_detail', 
    #                     args= [
    #                                 self.publishDate.year,
    #                                 self.publishDate.month,
    #                                 self.publishDate.day,
    #                                 self.slug
    #                             ])

    # -- Returns /api/article/year/month/day/slug --
    # -- use for Axios
    # def get_absolute_url(self):
    #     return reverse('article_detail', 
    #                     args= [
    #                         self.publishDate.year,
    #                         self.publishDate.month,
    #                         self.publishDate.day,
    #                         self.slug
    #                     ])





class Scholar(models.Model):
    officer = models.ForeignKey(Officer, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null = True, blank = True)
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=200, null = True, blank = True)
    content = models.TextField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True) # created automatically
    _id = models.AutoField(primary_key=True, editable=False)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

# QuillField demo model
# class QuillPost(models.Model):
#     content = QuillField()