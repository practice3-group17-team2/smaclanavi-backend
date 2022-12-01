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
            'id', 'lecture', 'which_class_held', 'is_personal_lec',
            'target_unit_type', 'can_select_date', 'created', 'updated', 'schedules'
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

    def create(self, validated_data):
        """ validated_dataの形式メモ
        {'id': UUID('b9e0fe00-3f47-4617-8819-ccb8483c5ee4'),\n
        'lecture_content': OrderedDict([('id', 2)]),\n
        'which_class_held': <ClassInfo: ClassInfo object (d1013537-a869-4d1c-a444-513f6d3be5d9)>,\n
        'is_personal_lec': False, 'is_iphone': False,
        'can_select_date': False, 'schedules': []} 
        """
        # print("\n\n\n\n", validated_data)
        lec_data = validated_data.pop('lecture_content')
        which_class = validated_data.pop('which_class_held')
        lec = models.Lecture.objects.get(**lec_data)
        target_unit_type = validated_data.pop("target_unit_type")

        # print("\n\n\n\n", lec_data["id"], which_class.id, "\n\n\n\n")

        # フローコントロールに使うのは良く無さげだけど苦肉の策
        if models.UpcomingLecInfos.objects.filter(
                lecture_content=lec, which_class_held=which_class, target_unit_type=target_unit_type).exists():
            raise ValueError(
                "An instance of what you are trying to create already exists")
        if not lec in which_class.lecture.all():
            raise ValueError("This classroom does not handle this lecture")

        up_lecinfo = models.UpcomingLecInfos.objects.create(
            lecture_content=lec,
            which_class_held=which_class,
            target_unit_type=target_unit_type,
            **validated_data)
        return up_lecinfo

    def update(self, instance, validated_data):
        lec_data = validated_data.pop("lecture_content")
        lec = models.Lecture.objects.get(id=lec_data["id"])
        which_class = validated_data.pop("which_class_held")
        target_unit_type = validated_data.pop("target_unit_type")

        if models.UpcomingLecInfos.objects.filter(
                lecture_content=lec, which_class_held=which_class, target_unit_type=target_unit_type).exists():
            raise ValueError(
                "An instance of what you are trying to update already exists")

        if not lec in which_class.lecture.all():
            raise ValueError("This classroom does not handle this lecture")

        instance.lecture_content = lec
        instance.which_class_held = which_class
        instance.target_unit_type = target_unit_type
        return super().update(instance, validated_data)
