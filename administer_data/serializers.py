from collections import OrderedDict
import uuid

from administer_data import models
from rest_framework import serializers
""" 
class PrefectureSerializer(serializers.ModelSerializer):
    pref_id = serializers.IntegerField(source='id')

    class Meta:
        model = models.Prefecture
        fields = ['pref_id', 'pref_name']
"""


class LectureSerializer(serializers.ModelSerializer):
    lec_id = serializers.IntegerField(source='id')

    class Meta:
        model = models.Lecture
        fields = ['lec_id', 'lecture_content', 'is_target_old']
        read_only_fields = ['lecture_content', 'is_target_old']


class OrganizerSerializer(serializers.ModelSerializer):
    org_id = serializers.IntegerField(source='id')
    org_name = serializers.CharField(source='organizer_name', read_only=True)

    class Meta:
        model = models.ClassOrganizer
        fields = ['org_id', 'org_name']


class CitySerializer(serializers.ModelSerializer):
    # prefecture = PrefectureSerializer()
    pref_obj = models.Prefecture.objects.all()

    pref_id = serializers.SlugRelatedField(queryset=pref_obj,
                                           slug_field='id',
                                           source='prefecture')

    pref_name = serializers.SlugRelatedField(queryset=pref_obj,
                                             slug_field='pref_name',
                                             source='prefecture')

    # migrationsファイルでBigAutoFieldに指定されているが
    # Big~ は IntegerFieldの拡張なのでこれでよい
    city_id = serializers.IntegerField(source='id')

    class Meta:
        model = models.City
        fields = ['pref_id', 'city_id', 'pref_name', 'city_name']
        read_only_fields = ['city_name']


class ReviewSerializer(serializers.ModelSerializer):
    """
    {
    "rev_id": "f03b9d08-64a7-4cf8-852c-5eaef0be17ce",
    "class_info_id": "c935a1d2-5f30-417f-81a0-e9294c2752cb",
    "author": "no name",
    "faves": 0,
    "review_text": "濃い口醤油"
    }
    post時、rev_id, author, faves, 省略可
    """
    rev_id = serializers.UUIDField(source="id",
                                   initial=uuid.uuid4,
                                   default=uuid.uuid4)
    class_info_id = serializers.PrimaryKeyRelatedField(
        queryset=models.ClassInfo.objects.all(), source="class_info")

    # class_info_url = serializers.HyperlinkedRelatedField(
    #     view_name='classinfo-detail', queryset=ClassInfo.objects.all())

    author = serializers.CharField(default="no name", initial="no name")
    faves = serializers.IntegerField(default=0, initial=0)

    class Meta:
        model = models.Review
        fields = ['rev_id', 'class_info_id', 'author', 'faves', 'review_text']

    # def create(self, validated_data):
    #     print("debug:", validated_data.get("id"))
    #     return super().create(validated_data)


class ClassInfoSerializer(serializers.ModelSerializer):
    # reviews = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    """ # return url list
    review_urls = serializers.HyperlinkedRelatedField(read_only=True,
                                                  many=True,
                                                  view_name='review-detail')
    """
    organizer = OrganizerSerializer(source="class_organizer")
    city = CitySerializer()
    lecture = LectureSerializer(many=True)
    lec_infos = serializers.SerializerMethodField(read_only=True)
    updated = serializers.SerializerMethodField()

    class Meta:
        model = models.ClassInfo
        fields = [
            'id', 'class_name', 'organizer', 'city', 'phone_number', 'address',
            'evaluation', 'price', 'site_url', 'created', 'updated', 'lecture',
            'lec_infos', 'reviews'
        ]

    # https://stackoverflow.com/questions/71721307/got-attributeerror-when-attempting-to-get-a-value-for-field-on-serializer
    def get_lec_infos(self, obj) -> OrderedDict:
        try:
            lec_info_query = models.UpcomingLecInfos.objects.filter(
                which_class_held=obj.id)
            serializer = UpcomingLecInfoSerializer(lec_info_query, many=True)
            return serializer.data
        except Exception:
            pass
        return None

    def get_updated(self, obj):
        """ 複数あるschedulesのupdatedを比較して最新のupdatedをUpcominglecInfoのupdatedに設定する """
        latest_date = obj.updated
        # 該当するインスタンスをget、modelで定義したrelatednameで逆参照をかける
        try:
            upcomeinfo = models.UpcomingLecInfos.objects.get(
                which_class_held=obj.id)
            upcomelecs = upcomeinfo.schedules.all()
        except Exception as e:
            pass
        else:
            for s in upcomelecs:
                if latest_date < s.updated:
                    latest_date = s.updated
        return latest_date


class LecScheduleSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.LecSchedule
        fields = ['id', 'date', 'updated']


class UpcomingLecInfoSerializer(serializers.ModelSerializer):
    """ 
    schedules = serializers.ListField(child=serializers.DateTimeField(
        source='LecSchedule.date'))
    """
    schedules = LecScheduleSerializer(many=True)
    # get_updatedに対応するmethodfield
    updated = serializers.SerializerMethodField()

    # lecture_content = serializers.SlugRelatedField(
    #     queryset=models.Lecture.objects.all(),
    #     slug_field='lecture_content',  # Lectureのlecture_content fieldを指してる
    # )
    lecture = LectureSerializer(source='lecture_content')

    class Meta:
        model = models.UpcomingLecInfos
        fields = [
            'id', 'lecture', 'which_class_held', 'schedules',
            'is_personal_lec', 'is_iphone', 'can_select_date', 'created',
            'updated'
        ]

    def get_updated(self, obj):
        """ 複数あるschedulesのupdatedを比較して最新のupdatedをUpcominglecInfoのupdatedに設定する """
        # 該当するインスタンスをget、modelで定義したrelatednameで逆参照をかける
        upcomeinfo = models.UpcomingLecInfos.objects.get(id=obj.id)
        related_schedules = upcomeinfo.schedules.all()

        latest_date = related_schedules[0].updated

        for s in related_schedules:
            if latest_date < s.updated:
                latest_date = s.updated
        return latest_date
