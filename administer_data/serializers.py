from administer_data import models
from rest_framework import serializers
""" 
class PrefectureSerializer(serializers.ModelSerializer):
    class Meta:
            model  = models.Prefecture
            fields = ['id', 'pref_name']


class LectureSerializer(serializers.ModelSerializer):
    class Meta:
            model  = models.Lecture
            fields = ['id', 'lecture_content', 'is_target_old']
"""


class CitySerializer(serializers.ModelSerializer):
    prefecture = serializers.SlugRelatedField(
        queryset=models.Prefecture.objects.all(), slug_field='pref_name')

    class Meta:
        model = models.City
        #fields = ['id','prefecture','city_name']
        fields = ['prefecture', 'city_name']


class ReviewSerializer(serializers.ModelSerializer):
    class_info = serializers.PrimaryKeyRelatedField(
        queryset=models.ClassInfo.objects.all())
    """
    class_info_url = serializers.HyperlinkedRelatedField(
        view_name='classinfo-detail', queryset=ClassInfo.objects.all())
    """

    class Meta:
        model = models.Review
        fields = ['id', 'class_info', 'review_text', 'faves', 'author']


class ClassInfoSerializer(serializers.ModelSerializer):
    # reviews = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    """ # return url list
    review_urls = serializers.HyperlinkedRelatedField(read_only=True,
                                                  many=True,
                                                  view_name='review-detail')
    """
    organizer = serializers.SlugRelatedField(
        queryset=models.ClassOrganizer.objects.all(),
        slug_field='organizer_name',
        source='class_organizer')
    city = CitySerializer()
    lecture = serializers.SlugRelatedField(
        queryset=models.Lecture.objects.all(),
        many=True,
        slug_field='lecture_content')

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

    lecture_content = serializers.SlugRelatedField(
        queryset=models.Lecture.objects.all(),
        slug_field='lecture_content',  # Lectureのlecture_content fieldを指してる
    )

    class Meta:
        model = models.UpcomingLecInfos
        fields = [
            'id', 'lecture_content', 'which_class_held', 'schedules',
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
