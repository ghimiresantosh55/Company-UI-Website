from rest_framework import serializers
from src.custom_lib.functions import current_user
from django.utils import timezone

from .models import Gallery


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = "__all__"
        read_only_fields = ['created_by', 'created_date_ad', 'created_date_bs']


    def create(self, validated_data):
        # provide current time
        date_now = timezone.now()
        validated_data['created_by'] = current_user.get_created_by(self.context)
        gallery= Gallery.objects.create(**validated_data, created_date_ad=date_now)
        return gallery
