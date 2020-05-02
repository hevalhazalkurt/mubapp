from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField



class PostCategory(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)


    class Meta:
        ordering = ('title',)
        verbose_name = 'post category'
        verbose_name_plural = 'post categories'


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('blog-category', args=[self.slug])


    def save(self, *args, **kwargs):
        self.slug = slugify(title)
        super().save(*args, **kwargs)



class Post(models.Model):
    image = models.ImageField(upload_to="images/")
    title = models.CharField(max_length=150)
    summary = models.CharField(max_length=250)
    category = models.ForeignKey(PostCategory, on_delete=models.CASCADE)
    content = RichTextUploadingField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=250, unique=True, blank = True)



    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('blog-detail', args=[self.slug])


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
