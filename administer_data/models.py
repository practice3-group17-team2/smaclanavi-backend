from unittest.util import _MAX_LENGTH
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
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # 勘違いにより追加されたcharfieldくん
    """ id = models.CharField(primary_key=True,
                          max_length=36,
                          default=uuid.uuid4,
                          editable=False) """
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class TestSaveData(models.Model):
    """
    スレイピングしたデータの保存を試す用のモデル
    """
    title = models.CharField(max_length=40)
    url = models.URLField()


class Prefecture(models.Model):
    pref_name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        # return f"<Prefecture: {self.pref_name}>"
        return '%s object (%s)' % (self.__class__.__name__, self.pref_name)

class City(models.Model):
    city_name = models.CharField(max_length=20, unique=True)
    # pref instance(pk=1) = 未設定用
    prefecture = models.ForeignKey(Prefecture,
                                   blank=True,
                                   on_delete=models.SET_DEFAULT,
                                   default=1)

    def __str__(self):
        # return f"<City: {self.city_name}>"
        return '%s object (%s)' % (self.__class__.__name__, self.city_name)


class Lecture(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    lecture_content = models.CharField(max_length=20, unique=True)
    is_target_old = models.BooleanField(blank=True, default=True)

    def __str__(self):
        # return f"<Lecture: {self.lecture_content}>"
        return '%s object (%s)' % (self.__class__.__name__, self.lecture_content)


class ClassOrganizer(models.Model):
    # class_org instance(pk=1) = 個人運営
    organizer_name = models.CharField(unique=True, max_length=20)

    def __str__(self) -> str:
        # return f"<ClassOrganizer: {self.organizer_name}>"
        return '%s object (%s)' % (self.__class__.__name__, self.organizer_name)


class ClassInfo(AbstractUUIDModel):
    class_name = models.CharField(max_length=100)
    class_organizer = models.ForeignKey(ClassOrganizer,
                                        on_delete=models.SET_DEFAULT,
                                        default=1)
    phone_number = models.CharField(max_length=100, blank=True, default='')
    # city instance(pk=1) = 未設定用
    city = models.ForeignKey(City,
                             blank=True,
                             on_delete=models.SET_DEFAULT,
                             default=1)
    address = models.CharField(max_length=100, blank=True, default='')
    lecture = models.ManyToManyField(Lecture, related_name="class_info", blank=True)
    evaluation = models.IntegerField(blank=True, default=0)
    price = models.IntegerField(blank=True, default=0)
    site_url = models.URLField(blank=True, default='')
    has_parking = models.BooleanField(blank=True, default=False)
    is_barrier_free = models.BooleanField(blank=True, default=False)

    class Meta:
        ordering = ['created']

    def __str__(self):
        # return f"<Classinfo: {self.class_name}>"
        return '%s object (%s)' % (self.__class__.__name__, self.class_name)


class Review(AbstractUUIDModel):
    class_info = models.ForeignKey(ClassInfo,
                                   on_delete=models.CASCADE,
                                   related_name='reviews')
    review_text = models.TextField(max_length=200)
    faves = models.IntegerField(blank=True, default=0)
    author = models.CharField(max_length=20, blank=True, default='名無し')

    def __str__(self) -> str:
        # return f"<Review: {self.review_text[:5]}>"
        return '%s object (%s)' % (self.__class__.__name__, self.review_text[:5])


class UpcomingLecInfos(AbstractUUIDModel):
    lecture_content = models.ForeignKey(Lecture,
                                        on_delete=models.CASCADE,
                                        related_name='upcoming_lecs')
    which_class_held = models.ForeignKey(ClassInfo,
                                         on_delete=models.CASCADE,
                                         related_name="upcoming_lecs")
    #updated = 複数スケジュールの最新日時を取るようにしたい
    is_personal_lec = models.BooleanField(blank=True, default=True)
    is_iphone = models.BooleanField(blank=True, default=True)
    can_select_date = models.BooleanField(blank=True, default=False)

    def __str__(self) -> str:
        # return f'<UpcomeLecInfos object ({self.lecture_content.lecture_content}, {self.which_class_held.class_name})>'
        return '%s object (%s, %s)' % (self.__class__.__name__, self.lecture_content.lecture_content, self.which_class_held.class_name)


class LecSchedule(AbstractUUIDModel):
    lec_info = models.ForeignKey(UpcomingLecInfos,
                                 on_delete=models.CASCADE,
                                 related_name="schedules")
    date = models.DateTimeField()

    def __str__(self) -> str:
        # return f"<LecSchedule: {self.lec_info}>"
        return '%s object (%s, %s)' % (self.__class__.__name__, self.date, self.lec_info)
