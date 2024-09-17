from django.db import models
from django.utils.text import slugify
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Language.
class Language(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(max_length=128, unique=True, null=True, blank=True)

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(self.name.lower())
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

# Category.
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(max_length=128, unique=True, null=True, blank=True)
    icon = models.CharField(max_length=50, null=True, blank=True)
    language = models.ForeignKey(to=Language, on_delete=models.CASCADE)

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(self.name.lower())
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'

# Phrase.
class Phrase(models.Model):
    text = models.TextField()
    translation = models.TextField()
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    language = models.ForeignKey(to=Language, on_delete=models.CASCADE)
    audio = models.FileField(upload_to='uploads/audios/', null=True, blank=True)
    pronunciation = models.TextField(null=True, blank=True)
    favorite = models.BooleanField(default=False)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.text