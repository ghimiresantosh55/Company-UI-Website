from rest_framework import serializers
from src.custom_lib.functions import current_user
from django.utils import timezone

from .models import Blog


class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = "__all__"
        read_only_fields = ['created_by', 'created_date_ad', 'created_date_bs']


    def create(self, validated_data):
        # provide current time
        date_now = timezone.now()
        validated_data['created_by'] = current_user.get_created_by(self.context)
        blog = Blog.objects.create(**validated_data, created_date_ad=date_now)
        return blog


    def to_representation(self, instance):
        my_fields = {'image'}
        data = super().to_representation(instance)
        for field in my_fields:
            try:
                if not data[field]:
                    data[field] = ""
            except KeyError:
                pass
        return data

