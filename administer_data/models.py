from django.db import models
""" 
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()]) 
"""

class Prefecture(models.Model):
    pref_name = models.CharField(max_length=20)

    def __str__(self):
        return self.pref_name

class City(models.Model):
    city_name = models.CharField(max_length=20)
    prefecture = models.ForeignKey(Prefecture, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.city_name

class Lecture(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    lecture_content = models.CharField(max_length=20)
    is_target_old = models.BooleanField(blank=True, default=True)

    def __str__(self):
        return self.lecture_content

class ClassInfo(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    class_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100, blank=True, default='')
    address = models.CharField(max_length=100, blank=True, default='')
    evaluation = models.IntegerField(blank=True, default=0)
    price = models.IntegerField(blank=True, default=0)
    site_url = models.URLField(blank=True, default='')
    city = models.ForeignKey(City, on_delete=models.SET_DEFAULT, blank=True, null=True, default='')
    lecture = models.ManyToManyField(Lecture, related_name="class_info")

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.class_name

class Review(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    class_info = models.ForeignKey(ClassInfo, on_delete=models.CASCADE, related_name='reviews')
    review_text = models.TextField(max_length=200)
    faves = models.IntegerField(blank=True, default=0)
    author = models.CharField(max_length=20 ,blank=True, default="名無し")

    def __str__(self) -> str:
        return super().__str__() + ":" + self.review_text[:5]