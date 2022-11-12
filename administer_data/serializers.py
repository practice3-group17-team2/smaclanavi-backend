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


class OrganizerSerializer(serializers.ModelSerializer):
    org_id = serializers.IntegerField(source='id')
    org_name = serializers.CharField(source='organizer_name')

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


class ReviewSerializer(serializers.ModelSerializer):
    rev_id = serializers.UUIDField(source="id")
    class_info_id = serializers.PrimaryKeyRelatedField(
        queryset=models.ClassInfo.objects.all(), write_only=True)
    """
    class_info_url = serializers.HyperlinkedRelatedField(
        view_name='classinfo-detail', queryset=ClassInfo.objects.all())
    """
    author = serializers.CharField(default="no name", initial="no name")
    faves  = serializers.IntegerField(default=0, initial=0)

    class Meta:
        model = models.Review
        fields = ['rev_id', 'class_info_id', 'review_text', 'faves', 'author']


class ClassInfoSerializer(serializers.ModelSerializer):
    # reviews = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    """ # return url list
    review_urls = serializers.HyperlinkedRelatedField(read_only=True,
                                                  many=True,
                                                  view_name='review-detail')
    """
    # organizer = serializers.SlugRelatedField(
    #     queryset=models.ClassOrganizer.objects.all(),
    #     slug_field='organizer_name',
    #     source='class_organizer')
    organizer = OrganizerSerializer(source="class_organizer")

    city = CitySerializer()
    lecture = LectureSerializer(many=True)

    class Meta:
        model = models.ClassInfo
        fields = [
            'id', 'class_name', 'organizer', 'phone_number', 'city', 'address',
            'lecture', 'evaluation', 'price', 'site_url', 'reviews'
        ]


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
