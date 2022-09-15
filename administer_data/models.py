from django.db import models
import uuid
""" 
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()]) 
"""


class AbstractUUIDModel(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id = models.CharField(primary_key=True,
                          max_length=36,
                          default=uuid.uuid4,
                          editable=False)

    class Meta:
        abstract = True


class Prefecture(models.Model):
    pref_name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.pref_name


class City(models.Model):
    city_name = models.CharField(max_length=20, unique=True)
    # pref instance(pk=1) = 未設定用
    prefecture = models.ForeignKey(Prefecture,
                                   blank=True,
                                   on_delete=models.SET_DEFAULT,
                                   default=1)

    def __str__(self):
        return self.city_name


class Lecture(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    lecture_content = models.CharField(max_length=20, unique=True)
    is_target_old = models.BooleanField(blank=True, default=True)

    def __str__(self):
        return self.lecture_content


class ClassInfo(AbstractUUIDModel):
    created = models.DateTimeField(auto_now_add=True)
    class_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100, blank=True, default='')
    # city instance(pk=1) = 未設定用
    city = models.ForeignKey(City,
                             blank=True,
                             on_delete=models.SET_DEFAULT,
                             default=1)
    address = models.CharField(max_length=100, blank=True, default='')
    lecture = models.ManyToManyField(Lecture, related_name="class_info")
    evaluation = models.IntegerField(blank=True, default=0)
    price = models.IntegerField(blank=True, default=0)
    site_url = models.URLField(blank=True, default='')

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.class_name


class Review(AbstractUUIDModel):
    created = models.DateTimeField(auto_now_add=True)
    class_info = models.ForeignKey(ClassInfo,
                                   on_delete=models.CASCADE,
                                   related_name='reviews')
    review_text = models.TextField(max_length=200)
    faves = models.IntegerField(blank=True, default=0)
    author = models.CharField(max_length=20, blank=True, default='名無し')

    def __str__(self) -> str:
        return super().__str__() + ":" + self.review_text[:5]