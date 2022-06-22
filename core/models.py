from django.db import models
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField

# Create your models here.

class Tag(models.Model):

    name = models.CharField(max_length = 100, unique = True)

    def __str__(self) -> str:
        
        return self.name
class Article(models.Model):

    STATUS = (
        (0, 'Draft'),
        (1, 'Published')
    )

    title = models.CharField(max_length = 225, unique = True)

    slug = models.SlugField(max_length = 225, unique = True)

    thumbnail = CloudinaryField('thumbnail')

    meta_description = models.CharField(max_length = 225, blank = True)

    content = RichTextField()

    status = models.IntegerField(choices = STATUS, default = 0)

    tags = models.ManyToManyField(Tag, blank = True)

    date_created = models.DateTimeField(auto_now_add = True)

    date_published = models.DateTimeField(blank=True, null=True)

    date_modified = models.DateTimeField(auto_now = True)

    class Meta:

        ordering = ['-date_published']

    def __str__(self) -> str:
        
        return self.title

class KindWord(models.Model):

    person = models.CharField(max_length = 225)

    description = models.CharField(max_length = 2225)

    comments = models.TextField()

    def __str__(self) -> str:
        
        return f'{self.person} -> {self.description}'

class Project(models.Model):

    PROJECT_CATEGORY = (
        (0, 'Work'),
        (1, 'Personal')
    )

    image_context = CloudinaryField('thumbnail')

    project_name = models.CharField(max_length = 225, unique = True)

    slug = models.SlugField(max_length = 225, unique = True)

    project_category = models.IntegerField(choices = PROJECT_CATEGORY, default = 0)

    role_in_project = models.CharField(max_length = 225)

    project_url = models.URLField(max_length = 225, unique = True)

    github_url = models.URLField(max_length = 225, blank = True)

    comments = models.ManyToManyField(KindWord, blank = True)

    def __str__(self) -> str:
        
        return self.project_name