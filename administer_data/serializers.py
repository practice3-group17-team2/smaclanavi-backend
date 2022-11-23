import uuid
from administer_data import models
from rest_framework import serializers
from rest_framework.utils.serializer_helpers import ReturnDict
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

    # pref_id = serializers.SlugRelatedField(queryset=pref_obj,
    pref_id = serializers.SlugRelatedField(read_only=True,
                                           slug_field='id',
                                           source='prefecture')

    pref_name = serializers.SlugRelatedField(read_only=True,
                                             slug_field='pref_name',
                                             source='prefecture')

    # migrationsファイルでBigAutoFieldに指定されているが
    # Big~ は IntegerFieldの拡張なのでこれでよい
    city_id = serializers.IntegerField(source='id', label='ID')

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

    author = serializers.CharField(default="no name", initial="no name")
    faves = serializers.IntegerField(default=0, initial=0)

    class Meta:
        model = models.Review
        fields = ['rev_id', 'class_info_id', 'author', 'faves', 'review_text']


class ClassInfoSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(initial=uuid.uuid4,
                               default=uuid.uuid4,
                               read_only=True)
    organizer = OrganizerSerializer(source="class_organizer")
    city = CitySerializer()
    evaluation = serializers.IntegerField(default=0, initial=0)
    price = serializers.IntegerField(default=0, initial=0)
    updated = serializers.SerializerMethodField()
    lecture = LectureSerializer(many=True)
    lec_infos = serializers.SerializerMethodField(read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = models.ClassInfo
        fields = [
            'id', 'class_name', 'organizer', 'city', 'phone_number', 'address',
            'evaluation', 'price', 'site_url', 'has_parking',
            'is_barrier_free', 'created', 'updated', 'lecture', 'lec_infos',
            'reviews'
        ]
        read_only_fields = ['created', 'updated']

    # https://stackoverflow.com/questions/71721307/got-attributeerror-when-attempting-to-get-a-value-for-field-on-serializer
    def get_lec_infos(self, obj) -> ReturnDict:
        ret = ReturnDict(serializer=self)
        try:
            lec_info_query = models.UpcomingLecInfos.objects.filter(
                which_class_held=obj.id)
            serializer = UpcomingLecInfoSerializer(lec_info_query, many=True)
            ret = serializer.data
        except Exception:
            pass
        return ret

    def get_updated(self, obj):
        """ 複数あるschedulesのupdatedを比較して最新のupdatedをUpcominglecInfoのupdatedに設定する """
        latest_date = obj.updated
        # 該当するインスタンスをget、modelで定義したrelatednameで逆参照をかける
        try:
            upcomeinfo = models.UpcomingLecInfos.objects.get(
                which_class_held=obj.id)
            upcomelecs = upcomeinfo.schedules.all()
        except Exception:
            pass
        else:
            for sche in upcomelecs:
                if latest_date < sche.updated:
                    latest_date = sche.updated
        return latest_date

    def create(self, validated_data):
        """ 
        {
            "class_name": "post test",
            "organizer": {
                "org_id": 1
            },
            "city": {
                "city_id": 1
            },
            "lecture": [
                {"lec_id": 1},
                {"lec_id": 2}
            ]
        }
        """
        org_data = validated_data.pop('class_organizer')
        city_data = validated_data.pop('city')
        lec_datas = validated_data.pop('lecture')
        org = models.ClassOrganizer.objects.get(**org_data)
        city = models.City.objects.get(**city_data)

        instance = models.ClassInfo.objects.create(class_organizer=org,
                                                   city=city,
                                                   **validated_data)

        for lec_data in lec_datas:
            lec = models.Lecture.objects.get(**lec_data)
            instance.lecture.add(lec)
        return instance

    def update(self, instance, validated_data):
        """
        id, created, updated, lec_infos, reviewsは自動更新or他APIから更新のため、read_onlyなど適応
        """
        """
        reviews        : administer_data.Review.None
        upcoming_lecs  : administer_data.UpcomingLecInfos.None
        id             : 34a331b6-e224-18a6-f13e-d8dc74ccaeea
        created        : 2022-09-15 09:45:52.304000+00:00
        updated        : 2022-09-15 09:45:52.304000+00:00
        class_name     : あいうえお
        class_organizer: ClassOrganizer object (1)
        phone_number   :
        city           : 未設定
        address        :
        evaluation     : 0
        price          : 0
        site_url       : https://www.yahoo.co.jp/
        has_parking    : False
        is_barrier_free: False
        lecture        : administer_data.Lecture.None
        """
        # organizer, city, lectureをいい感じに、他は親クラスで処理
        org_data = validated_data.pop('class_organizer')
        city_data = validated_data.pop('city')
        instance.class_organizer = models.ClassOrganizer.objects.get(
            **org_data)
        instance.city = models.City.objects.get(**city_data)

        lec_datas = validated_data.pop('lecture')
        instance_lec_ids = {i.id for i in instance.lecture.all()}
        data_lec_ids = {lec["id"] for lec in lec_datas}

        ids_to_add = data_lec_ids - instance_lec_ids
        ids_to_remove = instance_lec_ids - data_lec_ids

        if ids_to_add:
            for id in ids_to_add:
                lec = models.Lecture.objects.get(id=id)
                instance.lecture.add(lec)
        if ids_to_remove:
            for id in ids_to_remove:
                lec = models.Lecture.objects.get(id=id)
                instance.lecture.remove(lec)

        instance.save()
        return super().update(instance, validated_data)


class LecScheduleSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(initial=uuid.uuid4, default=uuid.uuid4)
    lec_info_id = serializers.PrimaryKeyRelatedField(
        source="lec_info", queryset=models.UpcomingLecInfos.objects.all())

    class Meta:
        model = models.LecSchedule
        fields = ['id', 'lec_info_id', 'date', 'updated']


class UpcomingLecInfoSerializer(serializers.ModelSerializer):
    """ 
    schedules = serializers.ListField(child=serializers.DateTimeField(
        source='LecSchedule.date'))
    """
    id = serializers.UUIDField(initial=uuid.uuid4,
                               default=uuid.uuid4,
                               read_only=True)
    lecture = LectureSerializer(source='lecture_content')
    updated = serializers.SerializerMethodField()
    schedules = LecScheduleSerializer(many=True, read_only=True)

    class Meta:
        model = models.UpcomingLecInfos
        fields = [
            'id', 'lecture', 'which_class_held', 'is_personal_lec',
            'is_iphone', 'can_select_date', 'created', 'updated', 'schedules'
        ]
        read_only_fields = ['created', 'updated']

    def get_updated(self, obj):
        """ 複数あるschedulesのupdatedを比較して最新のupdatedをUpcominglecInfoのupdatedに設定する """
        # 該当するインスタンスをget、modelで定義したrelatednameで逆参照をかける
        upcomeinfo = models.UpcomingLecInfos.objects.get(id=obj.id)
        related_schedules = upcomeinfo.schedules.all()

        latest_date = obj.updated

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

        # print("\n\n\n\n", lec_data["id"], which_class.id, "\n\n\n\n")

        # フローコントロールに使うのは良く無さげだけど苦肉の策
        if models.UpcomingLecInfos.objects.filter(
                lecture_content=lec, which_class_held=which_class).exists():
            raise ValueError(
                "An instance of what you are trying to create already exists")
        if not lec in which_class.lecture.all():
            raise ValueError("This classroom does not handle this lecture")

        up_lecinfo = models.UpcomingLecInfos.objects.create(
            lecture_content=lec,
            which_class_held=which_class,
            **validated_data)
        return up_lecinfo

    def update(self, instance, validated_data):
        lec_data = validated_data.pop("lecture_content")
        lec = models.Lecture.objects.get(id=lec_data["id"])
        which_class = validated_data.pop("which_class_held")

        if models.UpcomingLecInfos.objects.filter(
                lecture_content=lec, which_class_held=which_class).exists():
            raise ValueError(
                "An instance of what you are trying to update already exists")

        if not lec in which_class.lecture.all():
            raise ValueError("This classroom does not handle this lecture")

        instance.lecture_content = lec
        instance.which_class_held = which_class
        return super().update(instance, validated_data)
