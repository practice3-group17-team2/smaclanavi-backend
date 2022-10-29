from rest_framework import serializers
from administer_data.models import ClassInfo, Review, Lecture, City, ClassOrganizer, UpcomingLecInfos, LecSchedule
from administer_data.models import Prefecture
""" 
class PrefectureSerializer(serializers.ModelSerializer):
    class Meta:
            model  = Prefecture
            fields = ['id', 'pref_name']



class LectureSerializer(serializers.ModelSerializer):
    class Meta:
            model  = Lecture
            fields = ['id', 'lecture_content', 'is_target_old']
"""
class CitySerializer(serializers.ModelSerializer):
    prefecture = serializers.SlugRelatedField(queryset=Prefecture.objects.all(), slug_field='pref_name')
    class Meta:
            model  = City
            #fields = ['id','prefecture','city_name']
            fields = ['prefecture', 'city_name']


class ReviewSerializer(serializers.ModelSerializer):
    class_info = serializers.PrimaryKeyRelatedField(
        queryset=ClassInfo.objects.all())
    """
    class_info_url = serializers.HyperlinkedRelatedField(
        view_name='classinfo-detail', queryset=ClassInfo.objects.all())
    """

    class Meta:
        model = Review
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
        queryset=ClassOrganizer.objects.all(),
        slug_field='organizer_name',
        source='class_organizer')

    # city = serializers.SlugRelatedField(queryset=City.objects.all(),
    #                                    slug_field='city_name')
    city = CitySerializer()
    lecture = serializers.SlugRelatedField(queryset=Lecture.objects.all(),
                                           many=True,
                                           slug_field='lecture_content')

    class Meta:
        model = ClassInfo
        fields = [
            'id', 'class_name', 'organizer', 'phone_number', 'city', 'address',
            'lecture', 'evaluation', 'price', 'site_url', 'reviews'
        ]


class UpcomingLecInfoSerializer(serializers.ModelSerializer):
    # schedules = serializers.ListField(child=serializers.DateTimeField(source='LecSchedule.date'))
    class Meta:
        model = UpcomingLecInfos
        fields = [
            'id', 'lecture_content', 'which_class_held', 'is_personal_lec',
            'is_iphone', 'can_select_date', 'created', 'updated'
        ]