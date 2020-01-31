from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.

# 分类
class Category(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

    # class Meta:
    #     verbose_name = "分类"
    #     verbose_name_plural = "分类"

# 标签
class Tag(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

# 文章
class Post(models.Model):
    title = models.CharField(max_length = 70)
    content = models.TextField()
    time_create = models.DateTimeField(default = timezone.now)
    time_modify = models.DateTimeField()
    excerpt = models.CharField(max_length = 200, blank = True)
    category = models.ForeignKey(Category, models.CASCADE)
    tags = models.ManyToManyField(Tag, blank = True)
    author = models.ForeignKey(User, models.CASCADE)

    def get_absolute_url(self):
        # from . import views
        ret = reverse("HelloWorld:post", kwargs = {"id" : self.pk})
        # ret = reverse("post", kwargs = {"id" : self.pk})
        return ret

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.time_modify = timezone.now()
        return super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)

    def __str__(self):
        return self.title