from rest_framework import serializers
from administer_data.models import ClassInfo, Lecture, Review
from administer_data.models import Prefecture, City


class PrefectureSerializer(serializers.ModelSerializer):
    class Meta:
            model = Prefecture
            fields = ['id', 'pref_name']

class CitySerializer(serializers.ModelSerializer):
    class Meta:
            model = City
            fields = ['id','city_name', 'prefecture']


class LectureSerializer(serializers.ModelSerializer):
    class Meta:
            model = Lecture
            fields = ['id', 'lecture_content', 'is_target_old']

# class ClassInfoSerializer(serializers.ModelSerializer):
class ClassInfoSerializer(serializers.HyperlinkedModelSerializer):
    """
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']
    """
    # reviews = serializers.PrimaryKeyRelatedField(many=True, queryset=Review.objects.all())
    reviews = serializers.HyperlinkedIdentityField(view_name='review-detail')
    
    city = CitySerializer(required=False)
    
    class Meta:
        model = ClassInfo
        fields = ['id', 'class_name', 'phone_number', 'address', 'evaluation', 'price', 'site_url', 'city', 'lecture', 'reviews']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'class_info', 'review_text', 'faves', 'author']