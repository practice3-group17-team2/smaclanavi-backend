from rest_framework import serializers
from administer_data.models import Class


class ClassSerializer(serializers.Serializer):
    """
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')
    """
    id = serializers.IntegerField(read_only=True)
    class_name = serializers.CharField()
    phone_number = serializers.CharField(required=False, allow_blank=True,max_length=100)
    address = serializers.CharField(required=False, allow_blank=True,max_length=100)
    evaluation = serializers.IntegerField()
    price = serializers.IntegerField()
    site_url = serializers.URLField()

    def create(self, validated_data):
        """
        Create and return a new `Class` instance, given the validated data.
        """
        return Class.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Class` instance, given the validated data.
        """
        instance.class_name = validated_data.get('class_name', instance.class_name)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.address = validated_data.get('address', instance.address)
        instance.evaluation = validated_data.get('evaluation', instance.evaluation)
        instance.price = validated_data.get('price', instance.price)
        instance.site_url = validated_data.get('site_url', instance.site_url)
        instance.save()
        return instance