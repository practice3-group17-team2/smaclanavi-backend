from rest_framework import serializers
from administer_data.models import ClassInfo


class ClassInfoSerializer(serializers.ModelSerializer):
    """
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']
    """
    class Meta:
        model = ClassInfo
        fields = ['id', 'class_name', 'phone_number', 'address', 'evaluation', 'price', 'site_url']
        # city, lecture